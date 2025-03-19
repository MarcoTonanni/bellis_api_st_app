import requests
import streamlit as st
from login.service import logout


class FactionRepository:

    def __init__(self):
        self.__base_url = 'https://MTonanni.pythonanywhere.com/api/v1/'
        self.__factions_url = f'{self.__base_url}factions/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_factions(self):
        response = requests.get(
            self.__factions_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            logout()
            return None
        raise Exception(f'Error communicating with the API. Status code: {response.status_code}')

    def create_faction(self, faction):
        response = requests.post(
            self.__factions_url,
            headers=self.__headers,
            data=faction,
        )
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 401:
            logout()
            return None
        raise Exception(f'Error communicating with the API. Status code: {response.status_code}')
