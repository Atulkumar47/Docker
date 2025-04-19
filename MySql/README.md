# 🏗 Setting Up MySQL in a Docker Container with an Initialization Script 🐳

## 🔹 Prerequisites

✔ Install Docker on your system.  
✔ Ensure Docker is running.  
✔ Create an SQL initialization script (`Atul.sql`) with database and table definitions.

---

## 📂 Project Structure

```
MySql/
│── Dockerfile
│── Atul.sql
│── README.md
```

This structure keeps all necessary files organized.

---

## 🔧 Step 1: Create a Dockerfile

Create a `Dockerfile` inside the `MySql/` directory:

```dockerfile
# Use MySQL as the base image
FROM mysql:latest

# Copy the SQL script to the container
COPY Atul.sql /docker-entrypoint-initdb.d/

# Expose MySQL default port
EXPOSE 3306
---

## 📜 Step 2: Create an SQL Initialization Script

Create a file named `Atul.sql` with:

```sql
CREATE DATABASE Atul;
USE Atul;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

INSERT INTO students (name, age) VALUES ('Alice', 20), ('Bob', 24);
```

---

## 🏗 Step 3: Build the Docker Image

Run the command:

```sh
docker build -t mysql-custom .
```

💡 This creates a custom MySQL image named `mysql-custom`.

---

## 🚀 Step 4: Run MySQL Container

Start a MySQL container using:

```sh
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -d mysql-custom
```

### Explanation:
- 🏷 Creates a container named `mysql-container`.
- 🔑 Sets the root password to `root`.
- 🏃 Runs the container in detached mode (`-d`).
- 🔧 Uses the `mysql-custom` image.

---

## 🖥 Step 5: Access the Running Container

To enter the container shell:

```sh
docker exec -it mysql-container bash
```

---

## 💻 Step 6: Connect to MySQL

Once inside, connect to MySQL:

```sh
mysql -u root -p
```

🔑 Enter the password `root`.

---

## 🏗 Step 7: Verify Database and Tables

To check available databases:

```sql
SHOW DATABASES;
```

Switch to the `Atul` database:

```sql
USE Atul;
```

Query the `students` table:

```sql
SELECT * FROM students;
```

---

## 🎯 Conclusion

✅ You have successfully set up MySQL in a Docker container with an initialization script. Now your database is automatically initialized when the container starts! 🚢

---

## 📤 Pushing to GitHub

### **Step 1: Create a Repository on GitHub**
1. Log in to [GitHub](https://github.com/).
2. Click on **New repository**.
3. **Repository Name:** `Docker` (or any name you prefer).
4. **Visibility:** Choose Public or Private.
5. Click **Create Repository**.

### **Step 2: Set Up Git Locally**

Initialize Git:

```sh
cd D:\Full Docker
mkdir Docker
cd Docker
git init
```

Clone the empty repository:

```sh
git clone https://github.com/Atulkumar47/Docker.git
cd Docker
```

### **Step 3: Add the MySQL Experiment**

Create a directory:

```sh
mkdir MySql
cd MySql
```

Copy `Dockerfile`, `Atul.sql`, and `README.md` into `MySql/`.

### **Step 4: Commit and Push to GitHub**

1. **Go back to the main repo**:

```sh
cd ..
```

2. **Add all files to Git tracking**:

```sh
git add .
```

3. **Commit the changes**:

```sh
git commit -m "Added MySQL Docker setup experiment"
```

4. **Push to GitHub**:

```sh
git branch -M main
git remote add origin https://github.com/Atulkumar47/Docker.git
git push -u origin main
```

---
