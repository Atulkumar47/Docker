import streamlit as st
import json
from src.ui import display_sidebar_header
from src.utils import get_available_projects, get_reports_for_project, load_report

# Set page configuration
st.set_page_config(page_title="Evidently AI Dashboard", layout="wide")

# Load custom CSS
def load_css():
    with open("static/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    load_css()
    display_sidebar_header()
    
    # Load available projects
    projects = get_available_projects()
    if not projects:
        st.warning("No projects found. Please add a project and restart the app.")
        return
    
    # Project selection
    project = st.sidebar.selectbox("Select a Project", projects)
    reports = get_reports_for_project(project)
    
    if not reports:
        st.warning("No reports available for this project.")
        return
    
    # Report selection
    report = st.sidebar.selectbox("Select a Report", reports)
    
    if report:
        report_data = load_report(project, report)
        if report_data:
            st.subheader(f"Report: {report}")
            st.json(report_data, expanded=True)
        else:
            st.error("Failed to load the report. Please check the file format.")

if __name__ == "__main__":
    main()
