import streamlit as st
from battles.page import show_battles
from citations.page import show_citations
from commanders.page import show_commanders
from factions.page import show_factions
from home.page import show_home
from login.page import show_login
from wars.page import show_wars


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('De Bellis Rei Publicae Romanae App')

        menu_option = st.sidebar.selectbox(
            'Select an Option',
            ['Main Page', 'Factions', 'Commanders',
                'Wars', 'Battles', 'Citations']
        )

        if menu_option == 'Main Page':
            show_home()

        if menu_option == 'Factions':
            show_factions()

        if menu_option == 'Commanders':
            show_commanders()

        if menu_option == 'Wars':
            show_wars()

        if menu_option == 'Battles':
            show_battles()

        if menu_option == 'Citations':
            show_citations()


if __name__ == '__main__':
    main()
