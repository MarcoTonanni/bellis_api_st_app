import streamlit as st
from citations.repository import CitationRepository


class CitationService:

    def __init__(self):
        self.citation_repository = CitationRepository()

    def get_citations(self):
        if 'citations' in st.session_state:
            return st.session_state.citations
        citations = self.citation_repository.get_citations()
        st.session_state.citations = citations
        return citations

    def create_citation(self, author, war, reliability, text, book):
        citation = dict(
            author=author,
            war=war,
            reliability=reliability,
            text=text,
            book=book,
        )
        new_citation = self.citation_repository.create_citation(citation)
        st.session_state.citations.append(new_citation)
        return new_citation
