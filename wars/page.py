import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from commanders.service import CommanderService
from factions.service import FactionService
from wars.service import WarService


def show_wars():
    war_service = WarService()
    wars = war_service.get_wars()

    if wars:
        st.write('Wars List')
        wars_df = pd.json_normalize(wars)
        wars_df = wars_df.drop(columns=['id', 'belligerents', 'commanders', 'victor.id'])
        AgGrid(
            data=wars_df,
            reload_data=True,
            key='wars_grid'
        )
    else:
        st.warning('No wars found.')

    st.title('Register New War')

    name = st.text_input('War name')

    start_date = st.date_input(
        label='War start date, in Ad Urbe Condita (AUC) counting. If only the year is known, register both day and month as 1.',
        value=datetime(111, 11, 1).date(),
        min_value=datetime(1, 1, 1).date(),
        max_value=datetime(727, 1, 1).date(),
        format='DD/MM/YYYY',
    )
    end_date = st.date_input(
        label='War end date, in Ad Urbe Condita (AUC) counting. If only the year is known, register both day and month as 1.',
        value=datetime(111, 11, 1).date(),
        min_value=datetime(1, 1, 1).date(),
        max_value=datetime(800, 1, 1).date(),
        format='DD/MM/YYYY',
    )

    faction_service = FactionService()
    factions = faction_service.get_factions()
    faction_names = {faction['name']: faction['id'] for faction in factions}
    selected_belligerents_names = st.multiselect('Belligerents', list(faction_names.keys()))
    selected_belligerents_ids = [faction_names[name] for name in selected_belligerents_names]
    selected_victor_name = st.selectbox('Victor', list(faction_names.keys()))

    commander_service = CommanderService()
    commanders = commander_service.get_commanders()
    commander_names = {commander['name']: commander['id'] for commander in commanders}
    selected_commanders_names = st.multiselect('Commanders', list(commander_names.keys()))
    selected_commanders_ids = [commander_names[name] for name in selected_commanders_names]

    if st.button('Register'):
        new_war = war_service.create_war(
            name=name,
            start_date=start_date,
            end_date=end_date,
            belligerents=selected_belligerents_ids,
            victor=faction_names[selected_victor_name],
            commanders=selected_commanders_ids,
        )
        if new_war:
            st.rerun()
        else:
            st.error('Error registering a new commander. Check the fields.')
