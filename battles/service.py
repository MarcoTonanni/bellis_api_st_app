import streamlit as st
from battles.repository import BattleRepository


class BattleService():

    def __init__(self):
        self.battle_repository = BattleRepository()

    def get_battles(self):
        if 'battles' in st.session_state:
            return st.session_state.battles
        battles = self.battle_repository.get_battles()
        st.session_state.battles = battles
        return battles

    def create_battle(self, name, date, war, belligerents, victor, commanders):
        battle = dict(
            name=name,
            date=date,
            war=war,
            belligerents=belligerents,
            victor=victor,
            commanders=commanders,
        )
        new_battle = self.battle_repository.create_battle(battle)
        st.session_state.battles.append(new_battle)
        return new_battle
