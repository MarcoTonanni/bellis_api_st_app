import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from battles.service import BattleService
from commanders.service import CommanderService
from factions.service import FactionService
from wars.service import WarService


def show_battles():
    battle_service = BattleService()
    battles = battle_service.get_battles()

    if battles:
        st.write('Battles List')
        battles_df = pd.json_normalize(battles)
        battles_df = battles_df.drop(columns=[
            'belligerents', 'commanders', 'war.id', 'war.sources_reliability', 'war.start_date', 'war.end_date',
            'war.victor', 'war.belligerents', 'war.commanders', 'victor.id'
        ])

        AgGrid(
            data=battles_df,
            reload_data=True,
            key='battles_grid'
        )

    st.title('Register New Battle')

    name = st.text_input('Battle name')
    date = st.date_input(
        label='Battle date, in Ad Urbe Condita (AUC) counting. If only the year is known, register both day and month as 1.',
        value=datetime(111, 11, 1).date(),
        min_value=datetime(1, 1, 1).date(),
        max_value=datetime(727, 1, 1).date(),
        format='DD/MM/YYYY',
    )

    war_service = WarService()
    wars = war_service.get_wars()
    war_names = {war['name']: war['id'] for war in wars}
    war_selected_name = st.selectbox('War', list(war_names.keys()))

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
        new_battle = battle_service.create_battle(
            name=name,
            date=date,
            war=war_names[war_selected_name],
            belligerents=selected_belligerents_ids,
            victor=faction_names[selected_victor_name],
            commanders=selected_commanders_ids,
        )
        if new_battle:
            st.rerun()
        else:
            st.error('Error registering a new battle. Check the fields.')
