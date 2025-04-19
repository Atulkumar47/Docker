import streamlit as st

def display_sidebar_header():
    """Displays branding and navigation in the sidebar."""
    st.sidebar.title("📊 Evidently AI Dashboard")
    st.sidebar.markdown("---")
    st.sidebar.write("Monitor your ML models efficiently!")
