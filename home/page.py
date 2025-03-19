import streamlit as st
import plotly.express as px
from wars.service import WarService


def show_home():
    war_service = WarService()
    war_stats = war_service.get_war_stats()

    st.title('Ancient Roman Wars Statistics')

    if len(war_stats['wars_by_victor']) > 0:
        st.subheader('Wars by Victor')
        fig = px.pie(
            war_stats['wars_by_victor'],
            values='count',
            names='victor__name',
            title='Wars by Victor'
        )
        st.plotly_chart(fig)

    st.subheader('Total ammount of Wars Registered')
    st.write(war_stats['total_wars'])

    st.subheader('Ammount of Wars by Victor')
    for victor in war_stats['wars_by_victor']:
        st.write(f"{victor['victor__name']}: {victor['count']}")

    st.subheader('Fonts Average Reliability')
    st.write(war_stats['sources_average_reliability'])
