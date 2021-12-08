# Cloud Native Python

Simple K8S Deployment prepared for the Pytech Summit conference in 2021

## Project built with:

🧊 minikube

📦 K8S Deployment

🚢 docker

🐍 Python 3.9

🥬 celery


# Useful commands:

```
eval $(minikube docker-env)
kubectl apply -f worker-deployment.yaml
kubectl scale deployment/worker-deployment --replicas=3
kubectl port-forward api-deployment-774b8cbbf7-dp9xv 8000:8000
```

