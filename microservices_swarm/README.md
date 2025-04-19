# 🚀 **Microservices Deployment with Docker Swarm** 🌊  

This guide explains how to deploy a **microservices architecture** using **Docker Swarm**, featuring an **API Gateway** and a **Backend Service**.

---

## 📌 **Prerequisites** 🛠  
Before you begin, ensure the following:  
✔ Docker is installed (**Check with:** `docker --version`)  
✔ Docker Desktop is running (for **Swarm Mode**)  

---

## **🔹 Step 1: Initialize Docker Swarm** 🏗  

Enable **Swarm mode** on your system:  

```sh
docker swarm init
```  

This sets up your machine as the **Swarm Manager**, responsible for orchestrating containers.

---

## **📁 Step 2: Project Structure** 📂  

```
microservices_swarm/
│── backend-service/
│   ├── backend.py
│   ├── Dockerfile
│
│── api-gateway/
│   ├── api_gateway.py
│   ├── Dockerfile
│
│── docker-compose.yml
│── README.md
```

---

## **🖥️ Step 3: Backend Service Setup** 🏗  

Create `backend.py` inside the `backend-service/` folder:  

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Atul"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

### **Dockerfile for Backend Service** 📜  

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY backend.py /app
RUN pip install flask
CMD ["python", "backend.py"]
```

---

## **🛠️ Step 4: API Gateway Setup** 🌐  

Create `api_gateway.py` inside the `api-gateway/` folder:  

```python
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    backend_response = requests.get('http://backend-service:5000')
    return f"API Gateway: {backend_response.text}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
```

### **Dockerfile for API Gateway** 📜  

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY api_gateway.py /app
RUN pip install flask requests
CMD ["python", "api_gateway.py"]
```

---

## **📦 Step 5: Build Docker Images** 🔨  

Run the following commands to **build** both services:  

```sh
docker build -t backend-service ./backend-service
docker build -t api-gateway ./api-gateway
```  

Verify the images:  

```sh
docker images
```

---

## **📜 Step 6: Define Services in Docker Compose** 📝  

Create `docker-compose.yml` in the root directory:  

```yaml
version: '3.7'

services:
  backend-service:
    image: backend-service
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure
    networks:
      - app-network
    ports:
      - "5000:5000"

  api-gateway:
    image: api-gateway
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure
    networks:
      - app-network
    ports:
      - "8080:8080"
    depends_on:
      - backend-service

networks:
  app-network:
    driver: overlay
```

---

## **🚀 Step 7: Deploy Services to Docker Swarm** 🌍  

Deploy the stack using:  

```sh
docker stack deploy -c docker-compose.yml my_microservices
```

---
## 📸 Screenshot of 1
![1](images/Screenshot%202025-03-19%20112335.png)
## **📊 Step 8: Verify Running Services** 🔍  

Check running services:  

```sh
docker stack services my_microservices
```  

View running containers:  

```sh
docker ps
```

---
![2](images/Screenshot%202025-03-19%20113213.png)
## **🌐 Step 9: Access the Microservices** 🌍  

Test the API Gateway:  

```sh
curl http://localhost:8080
```

Expected Output:  

```
API Gateway: Atul
```

---
![3](images/Screenshot%202025-03-19%20113300.png)
## **📈 Step 10: Scaling Services** 🚀  

Increase the number of backend replicas to **5**:  

```sh
docker service scale my_microservices_backend-service=5
```  

Verify scaling:  

```sh
docker stack services my_microservices
```

---

## **🛠️ Step 11: Updating Services** 🔄  

If you update `backend.py`, **rebuild and update** the service:  

```sh
docker build -t backend-service ./backend-service
docker service update --image backend-service:latest my_microservices_backend-service
```

---

## **🛑 Step 12: Remove the Stack** ❌  

To remove all running services:  

```sh
docker stack rm my_microservices
```

To **exit Swarm mode**:  

```sh
docker swarm leave --force
```

---

## **📌 Summary** ✅  

✔ **Docker Swarm initialized**  
✔ **Microservices (Backend & API Gateway) created**  
✔ **Services deployed & verified**  
✔ **Scalability & service updates tested**  
✔ **Cleaned up resources**  

Now you have a **fully functional microservices architecture** running on **Docker Swarm**! 🚀🎯