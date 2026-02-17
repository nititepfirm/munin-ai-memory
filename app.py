import streamlit as st
from components.memory_card import render_memory_card
from utils.data_mock import get_mock_memory_data

st.set_page_config(page_title="Munin Memory Card", page_icon="🐦")

st.title("🐦 Munin: Memory Manager")
st.markdown("Review and manage your AI's long-term memory.")

# Fetch Mock Data
memories = get_mock_memory_data()

# Render Grid
st.subheader(f"Stored Memories ({len(memories)})")

# Loop through mock data and render cards
for mem in memories:
    render_memory_card(mem)
    st.write("") # Spacer
