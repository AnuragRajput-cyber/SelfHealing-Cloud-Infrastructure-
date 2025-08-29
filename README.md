# 🔄 Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible (Dockerized)

## 📌 Objective
Automatically detect service failures and **self-heal** by triggering automation scripts.  
This project demonstrates how monitoring + alerting + automation can ensure high availability with minimal manual intervention — all running in **Docker containers**.

---

## 🛠️ Tools & Technologies
- **Docker + Docker Compose** → Service orchestration  
- **Prometheus** → Metrics collection & monitoring  
- **Alertmanager** → Alert handling & routing  
- **Ansible** → Automation & remediation  
- **Flask Webhook** → To trigger Ansible playbook  
- **NGINX** → Sample service under monitoring  

---

## ⚙️ Architecture
1. **Prometheus (Docker)** scrapes metrics (e.g., NGINX uptime, CPU usage).  
2. **Alertmanager (Docker)** triggers when thresholds are breached.  
3. **Alertmanager Webhook → Flask App (Docker)** calls an **Ansible Playbook**.  
4. **Ansible** executes corrective actions (e.g., restart NGINX container).  

## Build & Run
**docker-compose up --build -d**

## 🔎Test Self-Healing
1. **Open Prometheus** → http://localhost:9090
2. **Open Alertmanager** → http://localhost:9093
3. **Stop the NGINX container manually:
    ## docker stop nginx_service
4. Wait ~30s → Alert fires → Alertmanager → Webhook → Ansible.
5. NGINX container auto-restarts:
    ## docker ps