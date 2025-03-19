import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from commanders.service import CommanderService


def show_commanders():
    commander_service = CommanderService()
    commanders = commander_service.get_commanders()

    if commanders:
        st.write('Commanders List')
        commanders_df = pd.json_normalize(commanders)

        AgGrid(
            data=commanders_df,
            reload_data=True,
            key='commanders_grid',
        )
    else:
        st.warning('No commanders found.')

    st.title('Register New Commander')
    name = st.text_input('Commander name')
    birth = st.date_input(
        label='Birth date, in Ad Urbe Condita (AUC) counting. If only the year is known, register both day and month as 1.',
        value=datetime(111, 11, 1).date(),
        min_value=datetime(1, 1, 1).date(),
        max_value=datetime(727, 1, 1).date(),
        format='DD/MM/YYYY',
    )
    death = st.date_input(
        label='Date of death, in Ad Urbe Condita (AUC) counting. If only the year is known, register both day and month as 1.',
        value=datetime(111, 11, 1).date(),
        min_value=datetime(1, 1, 1).date(),
        max_value=datetime(850, 1, 1).date(),
        format='DD/MM/YYYY',
    )
    procedence_dropdown = [
        'ROM', 'GRK', 'CAR', 'ITA', 'HIS', 'GAU', 'GER',
        'BRI', 'PON', 'ARM', 'PER', 'EGP', 'MAU',
        'NUM', 'PAR', 'MAK', 'UNK'
    ]

    procedence = st.selectbox(
        label='Procedence',
        options=procedence_dropdown,
        index=None,
    )

    if st.button('Register'):
        new_commander = commander_service.create_commander(
            name=name,
            birth=birth,
            death=death,
            procedence=procedence,
        )
        if new_commander:
            st.rerun()
        else:
            st.error('Error registering the new commander. Check the fields.')
