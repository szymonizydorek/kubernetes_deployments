# Kubernetes Deployments Lab

This project contains a collection of Kubernetes deployment manifests for learning, testing, and demonstrating how various common services run in a Kubernetes environment. It includes example configurations for applications like NGINX, HTTPD, WordPress, and more.

## 📦 Contents

The repository is structured with directories for each application, containing their respective deployment and service manifests.

### Currently Included:

- **NGINX** – Basic NGINX web server deployment with a NodePort service.
- **HTTPD** – Apache HTTP server setup for static site hosting.
- **WordPress** – Full WordPress + MySQL deployment using StatefulSets and PersistentVolumes.
- **Jenkins** – CI/CD server running as a StatefulSet with persistent storage.
- **Elasticsearch & Kibana** – A basic EFK-style setup for log and search demo.
- **Custom Apps** – Other custom pods or services for testing (e.g., `frontend`, `webapp`, etc.)

## 🛠 Project Goals

- Practice writing and managing Kubernetes manifests
- Learn how different applications behave inside a Kubernetes cluster
- Understand concepts like:
  - Deployments vs StatefulSets
  - Services (ClusterIP, NodePort, LoadBalancer)
  - PersistentVolumes and PersistentVolumeClaims
  - Scaling and rolling updates
  - Resource requests & limits

## 🗂 Directory Structure

```bash
Kuberenetes_deployment/
├── nginx/
│   ├── nginx-deployment.yaml
│   └── nginx-service.yaml
├── httpd/
│   ├── httpd-deployment.yaml
│   └── httpd-service.yaml
├── wordpress/
│   ├── wordpress-deployment.yaml
│   ├── mysql-deployment.yaml
│   └── wordpress-service.yaml
├── jenkins/
│   ├── jenkins-deployment.yaml
│   └── jenkins-service.yaml
├── elasticsearch/
│   ├── elasticsearch-statefulset.yaml
│   └── kibana-deployment.yaml
└── ...

