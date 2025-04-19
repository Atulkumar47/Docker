# 🌉 Docker Bridge Networking: Secure & Efficient Communication

## 🎯 Objective
This guide aims to explore **network isolation** in Docker containers. We will demonstrate how containers within a **custom bridge network** can communicate while remaining **isolated** from those on different networks. Mastering this concept is essential for securing **microservices** and containerized applications.

---

## 🌎 Understanding Docker Networking
Docker networking enables **containerized applications** to interact while maintaining **security and isolation**. Docker supports multiple network types:

### 📌 Docker Network Types:
- **Bridge Network (Default)** – Allows internal IP-based communication unless restricted.
- **Custom Bridge Network** – Enhances control and enables name-based resolution.
- **Host Network** – Directly connects containers to the host’s network.
- **Overlay Network** – Facilitates multi-host communication in **Docker Swarm**.
- **Macvlan Network** – Assigns each container a unique **MAC address**, making them appear as separate devices.
- **None Network** – Completely disables networking.

For this demonstration, we focus on **custom bridge networks**, which provide better **control and isolation**.

---

## ⚡ Why Choose a Custom Bridge Network?
A **custom bridge network** offers multiple benefits:
✔️ **Enhanced Security** – Containers on separate networks remain isolated.
✔️ **Optimized Performance** – Reduces host networking stack overhead.
✔️ **DNS-Based Communication** – Enables name-based interactions instead of relying on IP addresses.
✔️ **Greater Control** – Customizable **subnets, IP ranges, and gateways**.

To illustrate, we create a **custom bridge network** named `Atul-bridge` and connect multiple containers to it.

---

## 🔧 1. Creating a Custom Bridge Network
```bash
docker network create --driver bridge --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 Atul-bridge
```
### 🔍 Breakdown:
- `--driver bridge` → Implements **bridge networking**.
- `--subnet 172.20.0.0/16` → Defines the network’s **IP range**.
- `--ip-range 172.20.240.0/20` → Assigns **dynamic IPs** within the specified range.

---

## 🚀 2. Running Containers on the Custom Network
### Running **Redis Container** (`Atul-database`)
```bash
docker run -itd --net=Atul-bridge --name=Atul-database redis
```
### Running **BusyBox Container** (`Atul-server-A`)
```bash
docker run -itd --net=Atul-bridge --name=Atul-server-A busybox
```

### 🔍 Verifying Container IPs
```bash
docker network inspect Atul-bridge
```
Expected Output:
```
 Atul-database: 172.20.240.1
 Atul-server-A: 172.20.240.2
```

---

## 🔄 3. Testing Container Communication
### Checking Connectivity: `Atul-database` to `Atul-server-A`
```bash
docker exec -it Atul-database ping 172.20.240.2
```
### Checking Connectivity: `Atul-server-A` to `Atul-database`
```bash
docker exec -it Atul-server-A ping 172.20.240.1
```
✔️ **Expected Outcome:** Both containers should successfully **ping** each other.

---

## 🚧 4. Testing Isolation with a Third Container
A new container (`Atul-server-B`) is launched on the **default bridge network**.
```bash
docker run -itd --name=Atul-server-B busybox
```
### 🔍 Retrieving IP of `Atul-server-B`
```bash
docker inspect -format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' Atul-server-B
```
(Sample Output: `172.17.0.2`)

---

## ❌ 5. Checking Cross-Network Communication
Ping from `Atul-database` to `Atul-server-B`:
```bash
docker exec -it Atul-database ping 172.17.0.2
```
🚨 **Expected Outcome:** The ping should **fail**, indicating network isolation.

---

## 🔍 6. Validating Network Configuration
### Inspect Networks
```bash
docker network inspect Atul-bridge
docker network inspect bridge
```
✔️ `Atul-bridge` should include `Atul-database` & `Atul-server-A`.
✔️ `bridge` should contain `Atul-server-B`.

---

## 🏁 Conclusion
- Containers on the **same network** can communicate effortlessly.
- Containers on **separate networks** are **isolated** by default.
- Docker’s **networking model** ensures robust security unless explicitly overridden.

🎉 **Congratulations! You've mastered Docker Bridge Networking!** 🚢

