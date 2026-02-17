import streamlit as st
import datetime

def render_memory_card(memory_data):
    """
    Renders a single memory card component.

    Args:
        memory_data (dict): A dictionary containing memory data with keys:
                            'id', 'document', 'metadata' (title, status, created_at, source, confidence)
    """
    mem_id = memory_data.get("id", "unknown")
    document = memory_data.get("document", "")
    metadata = memory_data.get("metadata", {})
    
    title = metadata.get("title", "Untitled Memory")
    status = metadata.get("status", "active").lower()
    created_at = metadata.get("created_at", "Unknown Date")
    source = metadata.get("source", "Unknown Source")
    confidence = metadata.get("confidence", 0.0)

    # Status Badge Logic
    status_color = "🟢"
    if status == "expiring":
        status_color = "🟡"
    elif status == "archived":
        status_color = "🔴"
    
    status_badge = f"{status_color} {status.capitalize()}"

    # Container styling (Simulated with a border)
    with st.container(border=True):
        # Header: Badge | Title | Date
        col1, col2, col3 = st.columns([2, 6, 3])
        
        with col1:
             st.markdown(f"**{status_badge}**")
        with col2:
            st.markdown(f"### {title}")
        with col3:
            st.markdown(f"_{created_at}_")

        st.divider()

        # Body: Content
        # Truncate preview if too long (simple logic, or rely on expander)
        if len(document) > 200:
            st.markdown(document[:200] + "...")
            with st.expander("Read More"):
                st.markdown(document)
        else:
            st.markdown(document)
            
        st.divider()

        # Footer: Metadata Bar
        # Using columns for tags
        f_col1, f_col2, f_col3 = st.columns(3)
        with f_col1:
             st.caption(f"💾 **Source:** {source}")
        with f_col2:
             st.caption(f"🆔 **Ref ID:** {mem_id}")
        with f_col3:
             st.caption(f"🎯 **Confidence:** {confidence:.2f}")

        # Actions: Buttons
        st.markdown("---")
        a_col1, a_col2, a_col3 = st.columns(3)
        
        with a_col1:
            if st.button("✏️ Edit", key=f"edit_{mem_id}"):
                st.toast(f"Edit requested for {mem_id}")
        
        with a_col2:
            if st.button("🗑️ Forget", key=f"forget_{mem_id}"):
                st.toast(f"Forget requested for {mem_id}")
                
        with a_col3:
            if st.button("⚠️ Outdated", key=f"outdate_{mem_id}"):
                st.toast(f"Marked as outdated: {mem_id}")
