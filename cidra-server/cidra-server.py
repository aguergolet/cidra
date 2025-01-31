import os
import json
import redis
import subprocess
import sys
import logging
from dotenv import load_dotenv

load_dotenv()
# Obtendo configurações de variáveis de ambiente
company = os.getenv("COMPANY", "Desconhecida")
repository = os.getenv("REPOSITORY", "local")
redis_host = os.getenv("REDIS_SERVER", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)
data_timeout = int(os.getenv("DATA_TIMEOUT", 30))

logging.info(f"Configurações carregadas para {company}")

# ==============================
# 2️ CONEXÃO COM O REDIS
# ==============================
try:
    r = redis.Redis(host=redis_host, port=int(redis_port), socket_timeout=data_timeout)
    r.ping()  # Testa a conexão
    logging.info("Conexão com Redis estabelecida")
except Exception as e:
    logging.error(f"Erro ao conectar-se ao Redis: {e}")
    sys.exit(1)

# ==============================
# 3️ CLONANDO O REPOSITÓRIO
# ==============================
if repository.lower() != "local":
    REPO_DIR = "./code/"
    os.makedirs(REPO_DIR, exist_ok=True)  # Garante que a pasta existe

    # Pegando credenciais SSH de variáveis de ambiente
    SSH_PRIVATE_KEY = os.getenv("GIT_SSH_PRIVATE_KEY")
    SSH_KNOWN_HOSTS = os.getenv("GIT_KNOWN_HOSTS")

    if not SSH_PRIVATE_KEY:
        logging.error("Erro: Chave SSH não encontrada em GIT_SSH_PRIVATE_KEY.")
        sys.exit(1)

    # Criando um diretório temporário para as chaves (se necessário)
    SSH_DIR = os.path.expanduser("~/.ssh")
    os.makedirs(SSH_DIR, exist_ok=True)

    private_key_path = os.path.join(SSH_DIR, "id_rsa")
    known_hosts_path = os.path.join(SSH_DIR, "known_hosts")

    # Salvando a chave SSH no arquivo
    with open(private_key_path, "w") as key_file:
        key_file.write(SSH_PRIVATE_KEY)

    os.chmod(private_key_path, 0o600)  # Protegendo a chave

    # Salvando os hosts conhecidos (se existirem)
    if SSH_KNOWN_HOSTS:
        with open(known_hosts_path, "w") as hosts_file:
            hosts_file.write(SSH_KNOWN_HOSTS)

    logging.info(f"Chave SSH salva com sucesso em {private_key_path}")

    # Configurar o GIT para usar a chave SSH temporária
    os.environ["GIT_SSH_COMMAND"] = f"ssh -i {private_key_path} -o UserKnownHostsFile={known_hosts_path}"

    # Clonar repositório
    repo_url = repository
    repo_name = repository.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(REPO_DIR, repo_name)

    if os.path.exists(repo_path):
        logging.warning(f"Repositório já existe em {repo_path}. Ignorando clone.")
    else:
        try:
            subprocess.run(["git", "clone", repo_url, repo_path], check=True)
            logging.info(f"Repositório clonado com sucesso em {repo_path}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Erro ao clonar repositório: {e}")
            sys.exit(1)

logging.info("Configuração finalizada com sucesso!")
