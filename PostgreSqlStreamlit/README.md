Here’s your consolidated **README.md** with **main.py** included at the beginning:  

---

# 🚀 Deploying a Streamlit App with PostgreSQL in Docker  


## 📌 Overview  
This project deploys a **Streamlit application** that connects to a **PostgreSQL database** using **Docker**. The app retrieves and displays passenger data from PostgreSQL in a fully containerized environment.  

---

## 📁 Project Structure 🏗  
```
Streamlit-Postgres-Docker/
│── 🐳 Dockerfile
│── 🐍 main.py
```

### 🔹 File Descriptions:  
- **📜 main.py** – Streamlit app connecting to PostgreSQL.  
- **🐳 Dockerfile** – Configuration for containerizing the Streamlit app.  

---

## 🛠 Setting Up PostgreSQL in Docker  
### Step 1: Pull the PostgreSQL Docker Image  
```sh
docker pull postgres
```

### Step 2: Create a Docker Network 🌐  
```sh
docker network create my_postgres_network
```
This allows PostgreSQL and the Streamlit app to communicate.  

### Step 3: Run the PostgreSQL Container 🗄  
```sh
docker run --name my_postgres_container --network my_postgres_network \
-e POSTGRES_USER=Atul -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=testdb \
-p 5432:5432 -d postgres
```
This starts a PostgreSQL container with authentication settings.  

---

## 📊 Creating and Populating the Database  
### Step 4: Access PostgreSQL  
```sh
docker exec -it my_postgres_container psql -U Atul -d testdb
```

### Step 5: Create the `passengers` Table 🏷  
```sql
CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);
```

### Step 6: Insert Sample Data ✍️  
```sql
INSERT INTO passengers (name, location) VALUES
('Atul', 'Ghaziabad'),
('Rahul', 'Karnal'),
('Kushagra', 'Rohini');
```

---

## 🐳 Dockerizing the Streamlit Application  
### Step 7: Create a `Dockerfile`  
```dockerfile
FROM python:3.9
WORKDIR /app
COPY main.py .
RUN pip install streamlit psycopg2
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---
## 📜 `main.py`
```python
import streamlit as st
import psycopg2

# Custom CSS for a professional look
st.markdown("""
    <style>
        body {
            background-color: #f4f6f9;
            font-family: 'Arial', sans-serif;
        }
        .title {
            color: #333;
            font-size: 36px;
            font-weight: bold;
        }
        .subtitle {
            color: #555;
            font-size: 24px;
            margin-bottom: 20px;
        }
        .card {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .data {
            font-size: 18px;
            line-height: 1.6;
            color: #444;
        }
        .data span {
            color: #0073e6;
        }
        .error {
            color: #e74c3c;
        }
        .success {
            color: #2ecc71;
        }
        .warning {
            color: #f39c12;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 PostgreSQL Connection with Streamlit through Docker")

DB_HOST = "my_postgres_container"
DB_NAME = "testdb"
DB_USER = "Atul"
DB_PASSWORD = "secret"

def fetch_data():
    try:
        st.write("🔄 Connecting to database...")
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        st.write("<p class='success'>✅ Connected to PostgreSQL!</p>", unsafe_allow_html=True)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM passengers;")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        st.write(f"<p class='error'>❌ Database connection error: {str(e)}</p>", unsafe_allow_html=True)
        return []

data = fetch_data()

if data:
    st.subheader("📊 Data Retrieved:")
    for row in data:
        st.markdown(f"""
            <div class="card">
                <p class="data"><strong>🆔 ID:</strong> {row[0]} <strong>🏷 Name:</strong> {row[1]} <strong>📍 Location:</strong> {row[2]}</p>
            </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("<p class='warning'>⚠️ No data found in the `passengers` table.</p>", unsafe_allow_html=True)
```

---

## 🚀 Running the Streamlit Application in Docker  
### Step 8: Build the Docker Image 🔨  
```sh
docker build -t streamlit_app .
```

### Step 9: Run the Streamlit Container 🏃‍♂️  
```sh
docker run --name my_streamlit_container --network my_postgres_network -p 8501:8501 -d streamlit_app
```
This ensures that the Streamlit app can communicate with PostgreSQL.  

---

## 🔗 Access the Application 🌍  
Open a browser and navigate to:  
👉 **[http://localhost:8501](http://localhost:8501)**  

You should see the list of passengers displayed in the app.  

---

## 🎯 Summary  
✅ PostgreSQL container stores passenger data.  
✅ Streamlit container fetches and displays data from PostgreSQL.  
✅ Both containers communicate over **my_postgres_network**.  
✅ Application accessible at **http://localhost:8501**.  

This project provides a **containerized solution** for data visualization using **Streamlit and PostgreSQL**. 🚀🔥  

---

