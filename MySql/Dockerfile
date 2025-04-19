# 🏗 Use the official MySQL image
FROM mysql:latest

# 📂 Copy initialization script to the container
COPY Atul.sql /docker-entrypoint-initdb.d/

# 🔥 Expose MySQL port
EXPOSE 3306