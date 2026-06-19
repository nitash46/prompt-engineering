import streamlit as st

# 1. App Configuration & Page Title
st.set_page_config(page_title="Football Stat Tracker", page_icon="⚽", layout="centered")
st.title("⚽ Football Player Stat Tracker")
st.write("Search or select a player to instantly view their season metrics.")

# 2. Hardcoded Player Database
player_database = {
    "Bukayo Saka": {"Goals": 16, "Assists": 13, "Matches": 35, "Position": "Winger"},
    "Martin Ødegaard": {"Goals": 11, "Assists": 10, "Matches": 33, "Position": "Midfielder"},
    "Kai Havertz": {"Goals": 14, "Assists": 7, "Matches": 37, "Position": "Forward"}
}

# 3. User Interface: Selection Components
selected_player = st.selectbox("Select a player to view stats:", list(player_database.keys()))

# 4. Metric Layout & Rendering Logic
if selected_player:
    stats = player_database[selected_player]
    
    st.markdown(f"### {selected_player} — *{stats['Position']}*")
    st.write("---")
    
    # Splitting the layout into 3 equal columns for clean visual metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Matches Played", value=stats["Matches"])
    with col2:
        st.metric(label="Goals Scored ⚽", value=stats["Goals"])
    with col3:
        st.metric(label="Assists Provided 🅰️", value=stats["Assists"])
