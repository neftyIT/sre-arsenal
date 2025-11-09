# SRE Arsenal 🔥

Python automation toolkit for infrastructure monitoring and management.

## Tech Stack

- Python 3.x
- Requests library for API interactions
- PyYAML for configuration generation
- Environment variables for sensitive data

### Health Monitoring
- **Service Health Checker** - Monitors service availability and reports status
- Supports environment-based configuration
- Extensible for multiple service types

### Configuration Management
- **Prometheus Config Generator** - Dynamically generates Prometheus configurations from server lists
- Eliminates manual YAML editing
- Supports multiple target types

## Project Structure
```
sre-arsenal/
├── src/
│   ├── health_checks/       # Service monitoring scripts
│   └── config_generator/    # Configuration automation
├── .env.example             # Environment variable template
└── requirements.txt         # Python dependencies
```

## Development

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Setup
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/sre-arsenal.git
cd sre-arsenal

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your service URLs
```

### Running Scripts
```bash
# Health checker
python src/health_checks/service_checker.py

# Config generator
python src/config_generator/prometheus_generator.py
```

## More to Come!

- 🚨 Discord alerting integration
- 📊 Prometheus query automation
- 💾 Automated backup systems
- 🔄 Self-healing service management
- 🐳 Containerized deployments
- ☸️ Kubernetes CronJob automation

---

*Building infrastructure automation, one script at a time.*