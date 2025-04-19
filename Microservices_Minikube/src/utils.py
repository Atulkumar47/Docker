import os
import json

PROJECTS_DIR = "projects"

def get_available_projects():
    """Fetches available projects from the 'projects' directory."""
    if not os.path.exists(PROJECTS_DIR):
        return []
    return [d for d in os.listdir(PROJECTS_DIR) if os.path.isdir(os.path.join(PROJECTS_DIR, d))]

def get_reports_for_project(project):
    """Fetches available reports for a given project."""
    reports_dir = os.path.join(PROJECTS_DIR, project, "reports")
    if not os.path.exists(reports_dir):
        return []
    return [f for f in os.listdir(reports_dir) if f.endswith(".json")]

def load_report(project, report):
    """Loads the JSON report file."""
    report_path = os.path.join(PROJECTS_DIR, project, "reports", report)
    try:
        with open(report_path, "r") as f:
            return json.load(f)
    except Exception:
        return None
