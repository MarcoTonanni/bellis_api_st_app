import requests
import streamlit as st
from login.service import logout


class WarRepository():

    def __init__(self):
        self.__base_url = 'https://MTonanni.pythonanywhere.com/api/v1/'
        self.__wars_url = f'{self.__base_url}wars/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_wars(self):
        response = requests.get(
            self.__wars_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout
            return None
        raise Exception(f'Error communicating with the API. Status code: {response.status_code}')

    def create_war(self, war):
        response = requests.post(
            self.__wars_url,
            headers=self.__headers,
            data=war,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Error communicating with the API. Status code: {response.status_code}')

    def get_war_stats(self):
        response = requests.get(
            f'{self.__wars_url}stats/',
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Error communicating with the API. Status code: {response.status_code}')
