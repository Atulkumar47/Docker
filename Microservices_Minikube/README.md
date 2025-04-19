## 🌊 Deploying Evidently AI in Docker: A Data Monitoring Guide 💀📊

### 📌 Overview
This guide provides a structured approach to setting up a Streamlit-based Evidently AI dashboard inside a Docker container. The application:

- Utilizes Evidently AI for machine learning model monitoring.
- Features an interactive Streamlit dashboard.
- Systematically organizes reports and projects.
- Uses Docker for seamless deployment and management.

### 🗂 Project Structure
Ensure that the following directory structure is in place:

```
📁 evidently-ai-streamlit
 ├── 📁 projects                # Contains various ML monitoring projects
 │    ├── 📁 project_1
 │    │    ├── 📁 reports       # Stores monitoring reports
 │    │    ├── ...
 │    ├── 📁 project_2
 │    │    ├── 📁 reports
 │    │    ├── ...
 │    ├── ...
 │
 ├── 📁 src                     # Houses Python scripts for UI and utilities
 │    ├── ui.py                 # UI components
 │    ├── utils.py              # Utility functions
 │    ├── ...
 │
 ├── 📁 static                  # Stores static assets (CSS, images, etc.)
 │    ├── style.css             # Custom styling
 │    ├── ...
 │
 ├── 📅 app.py                   # Main Streamlit application script
 ├── 📅 Dockerfile               # Docker image configuration
 ├── 📅 requirements.txt          # Lists dependencies
 ├── 📅 README.md                 # Project documentation
```

### 📝 Main Application (`app.py` - Overview)
The `app.py` script:

- Dynamically loads available projects and reports.
- Allows users to select a project, timeframe, and report.
- Renders Evidently AI reports within Streamlit.
- Handles missing projects or reports gracefully.
- Utilizes `src/ui.py` for UI elements and `src/utils.py` for helper functions.

#### Key Functions:
- `display_sidebar_header()`: Displays sidebar branding and navigation.
- `select_project()`: Enables project selection.
- `select_period()`: Allows report timeframe selection.
- `select_report()`: Retrieves available reports.
- `display_report()`: Loads and displays the selected report.

### 🛠️ Dockerfile (Containerizing Streamlit App)
```dockerfile
# Use the official Python base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt /app/
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose the Streamlit port
EXPOSE 8501

# Execute the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 🐍 Python Dependencies (`requirements.txt`)
```
category_encoders==2.6.0
evidently==0.2.6
jupyter==1.0.0
jupyter_contrib_nbextensions==0.7.0
matplotlib==3.7.0
numpy==1.24.2
pandas==1.5.3
pyarrow==11.0.0
python-box==5.4.1
requests==2.28.2
streamlit==1.19.0
pyyaml==5.1
scikit-learn==1.2.1
scipy==1.10.1
seaborn==0.12.2
altair==4.0
```

### 🛠️ Running the Application

1. **Clone the repository and navigate to the project:**
   ```sh
   git clone <repo-link>
   cd evidently-ai-streamlit
   ```

2. **Build and run the Docker container:**
   ```sh
   docker build -t evidently-streamlit .
   docker run -p 8501:8501 evidently-streamlit
   ```

3. **Access the Streamlit application:**
   Open a browser and visit: [http://localhost:8501](http://localhost:8501)

### 🔖 Conclusion
✅ Successfully deployed an Evidently AI dashboard using Streamlit inside Docker.
✅ Integrated dynamic report selection across projects.
✅ Leveraged Docker for easy deployment and scalability.
✅ Maintained a modular code structure with UI and utility functions.

### 🚀 Next Steps
- 🔐 Add authentication for project access.
- 📈 Implement report comparisons over different periods.
- 🌐 Deploy the application on a cloud platform (AWS/GCP).

🌟 Keep innovating and happy coding! 🚀

