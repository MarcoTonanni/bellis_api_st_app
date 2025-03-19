import requests
import streamlit as st
from login.service import logout


class CitationRepository:

    def __init__(self):
        self.__base_url = 'https://MTonanni.pythonanywhere.com/api/v1/'
        self.__citations_url = f'{self.__base_url}citations/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_citations(self):
        response = requests.get(
            self.__citations_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Error communicating with the API. Status code: {response.status_code}')

    def create_citation(self, citation):
        response = requests.post(
            self.__citations_url,
            headers=self.__headers,
            data=citation
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Error communicating with the API. Status code: {response.status_code}')
