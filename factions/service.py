import streamlit as st
from factions.repository import FactionRepository


class FactionService:

    def __init__(self):
        self.faction_repository = FactionRepository()

    def get_factions(self):
        if 'factions' in st.session_state:
            return st.session_state.factions
        factions = self.faction_repository.get_factions()
        st.session_state.factions = factions
        return factions

    def create_faction(self, name):
        faction = dict(
            name=name,
        )
        new_faction = self.faction_repository.create_faction(faction)
        st.session_state.factions.append(new_faction)
        return new_faction
