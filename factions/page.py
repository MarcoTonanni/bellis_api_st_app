import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from factions.service import FactionService


def show_factions():
    faction_service = FactionService()
    factions = faction_service.get_factions()

    if factions:
        st.write('Factions List')
        factions_df = pd.json_normalize(factions)
        AgGrid(
            data=factions_df,
            reload_data=True,
            key='factions_grid',
        )
    else:
        st.warning('No factions found.')

    st.title('Register New Faction')
    name = st.text_input('Faction name')
    if st.button('Register'):
        new_faction = faction_service.create_faction(
            name=name,
        )
        if new_faction:
            st.rerun()
        else:
            st.error('Error registering the new faction. Check the fields.')
