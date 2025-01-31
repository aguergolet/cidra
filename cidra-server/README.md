# CIDRA Server - Command Execution & Storage

CIDRA Server is a core component of the CIDRA platform responsible for **executing commands**, **cloning repositories**, and **storing results in Redis** for easy access and retrieval.

## 🚀 Features

- **Automated Repository Cloning**: Dynamically clones repositories from configured sources.
- **Command Execution**: Runs predefined commands and stores structured outputs.
- **Redis Integration**: Utilizes Redis to store and serve execution results efficiently.
- **Secure SSH Handling**: Uses environment variables to manage secure SSH connections.
- **Logging & Error Handling**: Implements robust logging for monitoring execution processes.

## 🛠️ Tech Stack

- **Language**: Python
- **Storage**: Redis
- **Environment Management**: dotenv
- **Containerization**: Docker

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```sh
git clone https://github.com/YOUR_GITHUB_USER/cidra-server.git
cd cidra-server
virtualenv venv
. ./venv/bin/activate
```

### 2️⃣ Install dependencies

```sh
pip install -r requirements.txt
```

### 3️⃣ Start Services (via Docker)

Ensure Docker and Docker Compose are installed, then run:

```sh
cd ..
cd redis
docker-compose up -d
```

This will start **Redis** as specified in `docker-compose.yml`.

### 4️⃣ Run the Server

```sh
cd ..
cd cidra-server

python cidra-server.py
```

## ⚙️ Configuration

CIDRA Server relies on environment variables managed via a `.env` file:

```ini
COMPANY=YourCompanyName
REPOSITORY=https://github.com/example/repository.git
REDIS_SERVER=localhost
REDIS_PORT=6379
DATA_TIMEOUT=30
GIT_SSH_PRIVATE_KEY=your_ssh_key
GIT_KNOWN_HOSTS=your_known_hosts
CODE_FOLDER=code_sample
```

## 🔧 How It Works

1. **Loads environment configurations** for company settings, Redis, and repository details.
2. **Establishes a connection to Redis** for storing and retrieving execution results.
3. **Clones the specified repository** using SSH authentication if required.
4. **Executes commands** as configured and stores structured responses.
5. **Outputs are logged** for debugging and monitoring.

## 📄 Docker Compose Configuration

The `docker-compose.yml` file includes:

```yaml
version: '3.8'

services:
  redis:
    image: redis:latest
    ports:
      - "6379:6379"
```

This ensures Redis is available for CIDRA Server.

## 🔜 Future Enhancements

- Advanced command execution pipeline.
- API support for external integrations.
- AI-powered analysis of stored execution data.

## 📄 License

CIDRA Server is released under the **MIT License**.



# CODE OR LOCAL FOLDER STRUCTURE

config.json
