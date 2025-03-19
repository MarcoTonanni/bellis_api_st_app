import streamlit as st
from wars.repository import WarRepository


class WarService():

    def __init__(self):
        self.war_repository = WarRepository()

    def get_wars(self):
        if 'wars' in st.session_state:
            return st.session_state.wars
        wars = self.war_repository.get_wars()
        st.session_state.wars = wars
        return wars

    def create_war(self, name, start_date, end_date, belligerents, victor, commanders):
        war = dict(
            name=name,
            start_date=start_date,
            end_date=end_date,
            belligerents=belligerents,
            victor=victor,
            commanders=commanders,
        )
        new_war = self.war_repository.create_war(war)
        st.session_state.wars.append(new_war)
        return new_war

    def get_war_stats(self):
        if 'war_stats' in st.session_state:
            return st.session_state.war_stats
        war_stats = self.war_repository.get_war_stats()
        st.session_state.war_stats = war_stats
        return war_stats
