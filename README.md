# CIDRA - Centralized Intelligent Diagnostics and Response Automation

CIDRA is an **open-source platform** designed to provide a **scalable and extensible support automation framework**. It enables users to request **simple yet powerful automations**, such as **system diagnostics**, aggregating data from multiple sources with minimal input.

## 🌟 Features
- **Minimalist Frontend**: Supports authentication and can be secured behind Google IAP.
- **Automated Repository Execution**: Runs scripts from a structured repository or locally.
- **Redis Integration**: Stores and serves structured responses from executed commands.
- **Expandable**: Designed for future AI-powered modules and additional automation capabilities.
- **Open Source**: Available on GitHub for contribution and customization.

## 🛠️ Tech Stack
- **Backend**: Python
- **Data Storage**: Redis
- **Containerization**: Docker + Docker Compose
- **Environment Configuration**: dotenv

## 🚀 Getting Started

### 1️⃣ Clone the repository
```sh
git clone https://github.com/YOUR_GITHUB_USER/cidra.git
cd cidra
```

### 2️⃣ Install dependencies
Ensure you have Python installed, then install the required packages:
```sh
pip install -r requirements.txt
```

### 3️⃣ Start Redis (via Docker)
If you don't have Redis installed locally, you can start it using Docker Compose:
```sh
docker-compose up -d
```

### 4️⃣ Run the Server
```sh
python cidra-server.py
```

## 🛠 Configuration
Environment variables are managed using a `.env` file:
```ini
COMPANY=YourCompanyName
REPOSITORY=https://github.com/example/repository.git
REDIS_SERVER=localhost
REDIS_PORT=6379
DATA_TIMEOUT=30
GIT_SSH_PRIVATE_KEY=your_ssh_key
GIT_KNOWN_HOSTS=your_known_hosts
```

## 📌 How It Works
1. CIDRA **clones or updates** the configured repository.
2. The **executed scripts** return structured data.
3. Data is **stored in Redis** for easy access via the frontend.

## 💜 Future Enhancements
- AI-powered diagnostics and recommendations.
- Expanded automation modules.
- API for external integrations.

## 📝 License
CIDRA is released under the **MIT License**.