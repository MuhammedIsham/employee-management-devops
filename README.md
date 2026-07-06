# 🚀 Employee Management System with End-to-End DevOps CI/CD Pipeline

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?logo=jenkins&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazonaws)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-F46800?logo=grafana)

</p>

---

# 📖 Overview

This project is a **production-inspired Employee Management System** demonstrating a complete **DevOps CI/CD workflow** from development to deployment.

The application is developed using **Flask** and **PostgreSQL**, containerized with **Docker**, automated using **Jenkins**, orchestrated with **Kubernetes**, deployed on **AWS EC2**, and monitored using **Prometheus** and **Grafana**.

Every code push automatically triggers a GitHub Webhook that starts a Jenkins Pipeline to build and deploy the latest version of the application.

---

# ✨ Features

- 👨 Employee Management
- ➕ Add Employee
- 🔍 Search Employee
- ❌ Delete Employee
- 📋 View Employee Records
- 🐳 Dockerized Application
- ⚙️ Jenkins CI/CD Pipeline
- 🔗 GitHub Webhook Integration
- ☸ Kubernetes Deployment
- 🌐 Nginx Reverse Proxy
- ☁ AWS EC2 Deployment
- 📊 Grafana Monitoring
- 📈 Prometheus Metrics
- 🐘 PostgreSQL Database

---

# 🛠 Technology Stack

| Category | Technologies |
|-----------|--------------|
| Backend | Python, Flask |
| Database | PostgreSQL |
| Containerization | Docker, Docker Compose |
| CI/CD | Jenkins |
| Version Control | Git, GitHub |
| Orchestration | Kubernetes |
| Monitoring | Prometheus, Grafana |
| Reverse Proxy | Nginx |
| Cloud | AWS EC2 |
| Operating System | Ubuntu Linux |

---

# 🏗 Architecture

```text
                Developer
                   │
             Visual Studio Code
                   │
                   ▼
             Git Commit & Push
                   │
                   ▼
          GitHub Repository
                   │
            GitHub Webhook
                   │
                   ▼
          Jenkins CI/CD Pipeline
                   │
        Build Docker Image
                   │
                   ▼
        Docker Compose Deploy
                   │
                   ▼
             Kubernetes Cluster
                   │
         ┌─────────┴─────────┐
         │                   │
         ▼                   ▼
      Flask App         PostgreSQL
         │
         ▼
       Nginx
         │
         ▼
      AWS EC2 Server

         │
         ▼
    Prometheus
         │
         ▼
      Grafana
```

---

# ⚙️ CI/CD Pipeline

```
Developer

↓

Git Commit

↓

Git Push

↓

GitHub Repository

↓

GitHub Webhook

↓

Jenkins Pipeline Triggered

↓

Source Code Checkout

↓

Docker Image Build

↓

Docker Compose Deployment

↓

Application Updated Automatically

↓

Monitoring via Prometheus & Grafana
```

---

# ☸ Kubernetes Deployment

The project includes Kubernetes manifests for:

- Deployment
- Service
- ConfigMap
- Secret
- Namespace

allowing the application to be deployed in a Kubernetes environment.

---

# 📊 Monitoring

Monitoring is implemented using:

- Prometheus
- Grafana
- Node Exporter

These tools provide:

- CPU Usage
- Memory Usage
- Container Metrics
- System Health
- Application Availability

---

# ☁ AWS Deployment

The application is deployed on an AWS EC2 Ubuntu instance.

Deployment includes:

- Docker
- Docker Compose
- Jenkins
- Kubernetes
- Nginx
- PostgreSQL
- Prometheus
- Grafana

---

# 📂 Project Structure

```
employee-management-devops/

├── app.py
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── requirements.txt
├── create_db.py
├── templates/
├── nginx/
├── prometheus/
├── grafana/
├── jenkins/
├── k8s/
├── screenshots/
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/MuhammedIsham/employee-management-devops.git
```

Navigate into the project

```bash
cd employee-management-devops
```

Build and start containers

```bash
docker compose up -d --build
```

Open

```
http://localhost
```

---

# 📸 Project Screenshots

### Dashboard

(Add Dashboard Screenshot)

### Jenkins Pipeline

(Add Jenkins Build Screenshot)

### Kubernetes Deployment

(Add Kubernetes Screenshot)

### Grafana Dashboard

(Add Grafana Screenshot)

### Prometheus Metrics

(Add Prometheus Screenshot)

---

# 🎯 Project Highlights

✅ GitHub Webhooks

✅ Jenkins CI/CD

✅ Docker

✅ Docker Compose

✅ Kubernetes

✅ AWS EC2

✅ PostgreSQL

✅ Flask

✅ Nginx

✅ Prometheus

✅ Grafana

✅ Linux

---

# 📚 Learning Outcomes

Through this project I gained practical experience with:

- Docker Image Creation
- Docker Compose
- Jenkins Pipelines
- GitHub Webhooks
- Kubernetes Deployments
- Reverse Proxy using Nginx
- AWS EC2 Administration
- Linux Server Management
- Monitoring with Prometheus & Grafana
- End-to-End CI/CD Automation

---

# 🚀 Future Improvements

- Helm Charts
- Terraform
- Ansible Automation
- GitHub Actions
- ArgoCD GitOps
- SSL using Let's Encrypt
- Horizontal Pod Autoscaling

---

# 👨‍💻 Author

**Muhammed Isham**

🎓 MCA Graduate

💻 Aspiring DevOps Engineer

GitHub:
https://github.com/MuhammedIsham

LinkedIn:
https://www.linkedin.com/in/muhammed-isham-51b05a1a2

---

⭐ If you found this project helpful, don't forget to Star the repository.