import streamlit as st
from commanders.repository import CommanderRepository


class CommanderService():

    def __init__(self):
        self.commander_repository = CommanderRepository()

    def get_commanders(self):
        if 'commanders' in st.session_state:
            return st.session_state.commanders
        commanders = self.commander_repository.get_commanders()
        st.session_state.commanders = commanders
        return commanders

    def create_commander(self, name, **kwargs):
        birth = kwargs.get('birth')
        death = kwargs.get('death')
        procedence = kwargs.get('procedence')

        commander = dict(
            name=name,
            birth=birth,
            death=death,
            procedence=procedence,
        )
        new_commander = self.commander_repository.create_commander(commander)
        st.session_state.actors.append(new_commander)
        return new_commander
