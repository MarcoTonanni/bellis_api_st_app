import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from citations.service import CitationService
from wars.service import WarService


def show_citations():
    citation_service = CitationService()
    citations = citation_service.get_citations()

    if citations:
        st.write('Citations List')
        citations_df = pd.json_normalize(citations)
        citations_df = citations_df.drop(columns=[
            'id', 'text', 'war.id', 'war.sources_reliability', 'war.start_date', 'war.end_date',
            'war.victor', 'war.belligerents', 'war.commanders',
        ])

        AgGrid(
            data=citations_df,
            reload_data=True,
            key='citations_grid'
        )
    else:
        st.warning('No citations found.')

    st.title('Register New Citation')

    author = st.text_input('Author')

    war_service = WarService()
    wars = war_service.get_wars()
    war_names = {war['name']: war['id'] for war in wars}
    selected_war_name = st.selectbox('War', list(war_names.keys()))

    reliability = st.number_input(
        label='Reliability',
        min_value=0,
        max_value=5,
        step=1,
    )

    text = st.text_input('Citation')
    book = st.text_input('Book')

    if st.button('Cadastrar'):
        new_citation = citation_service.create_citation(
            author=author,
            war=war_names[selected_war_name],
            reliability=reliability,
            text=text,
            book=book,
        )
        if new_citation:
            st.rerun()
        else:
            st.error('Error registering a new citation. Check the fields.')
