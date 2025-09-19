# DevOps Pre-Interview Practical Test

This repository contains the solution for the DevOps practical test. It includes a containerized Python web service, a GitLab CI/CD pipeline, monitoring with Prometheus/Alertmanager, and network configuration examples.

## 🚀 Setup and Run

1.  **Prerequisites:**
    * Docker and Docker Compose
    * Git

2.  **Clone the repository:**
    ```bash
    git clone https://github.com/Elyasdj/Devops_Blueprint
    cd devops-test
    ```

3.  **Run the application stack:**
    ```bash
    docker-compose up --build
    ```
    * Web Service: `http://localhost:5000`
    * Prometheus: `http://localhost:9090`
    * Alertmanager: `http://localhost:9093`

## ⚙️  CI/CD Pipeline

The CI/CD pipeline is defined in `.gitlab-ci.yml`. It is automatically triggered on every push to the `main` branch.

**Stages:**
1.  **Build:** Builds the Docker image and pushes it to the GitLab Container Registry.
2.  **Test:** Runs placeholder tests.
3.  **Deploy:** Simulates deploying the application.

## 🚨 Failure and Recovery

* **Container Failure:** The web service is configured with `restart: unless-stopped`. If the container crashes, Docker will automatically restart it. You can test this with `docker kill python_web_app`.
* **iptables Rule:** An `iptables` rule can be added to block external traffic to port 5000.
    * **To add the rule:** `sudo iptables -I INPUT -p tcp --dport 5000 ! -s 127.0.0.1 -j DROP`
    * **To remove the rule:** `sudo iptables -D INPUT 1` (assuming it's the first rule).
