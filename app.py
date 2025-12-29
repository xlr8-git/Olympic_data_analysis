import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from llm_explainer import explain_graph

st.set_page_config(
    page_title="Olympics EDA (1896–2016)",
    layout="wide"
)

sns.set(style="darkgrid")

@st.cache_data
def load_data():
    data = pd.read_csv("athlete_events.csv")
    regions = pd.read_csv("noc_regions.csv")
    return pd.merge(data, regions, on="NOC", how="left")

merged = load_data()

def explain_button(prompt: str, key: str):
    if st.button("🧠 Explain this graph", key=key):
        with st.spinner("AI is analyzing the visualization..."):
            st.info(explain_graph(prompt))

st.sidebar.subheader("🎛️ Filters")

year_range = st.sidebar.slider(
    "Select Year Range",
    int(merged['Year'].min()),
    int(merged['Year'].max()),
    (1896, 2016)
)

countries = sorted(merged['region'].dropna().unique())
selected_country = st.sidebar.selectbox("Select Country", ["All"] + countries)

sports = sorted(merged['Sport'].unique())
selected_sport = st.sidebar.selectbox("Select Sport", ["All"] + sports)

filtered = merged[
    (merged['Year'] >= year_range[0]) &
    (merged['Year'] <= year_range[1])
]

if selected_country != "All":
    filtered = filtered[filtered['region'] == selected_country]

if selected_sport != "All":
    filtered = filtered[filtered['Sport'] == selected_sport]

st.sidebar.title("🏅 Olympics EDA")

section = st.sidebar.radio(
    "Select Section",
    [
        "Overview",
        "Age Distribution of Gold Medalists",
        "Women in Olympics",
        "Medals per Country",
        "Height vs Weight",
        "Evolution Over Time",
        "Gymnastics Analysis",
        "Weightlifting Analysis",
        "World Medal Map",
        "Conclusions"
    ]
)

if section == "Overview":
    st.title("🏟️ Olympic Games Dashboard")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Athletes", filtered['ID'].nunique())
    c2.metric("Countries", filtered['region'].nunique())
    c3.metric("Editions", filtered['Year'].nunique())
    c4.metric("Medals", filtered['Medal'].notna().sum())

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("📈 Participation Over Time")
        part = filtered.groupby('Year')['ID'].nunique()
        st.line_chart(part)

        explain_button(
            f"Explain Olympic participation trend from {year_range[0]} to {year_range[1]}.",
            "overview_participation"
        )

    with right:
        st.subheader("♀️♂️ Gender Split")
        fig, ax = plt.subplots()
        filtered['Sex'].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
        st.pyplot(fig)

        explain_button(
            "Explain gender distribution in Olympic participation.",
            "overview_gender"
        )

elif section == "Age Distribution of Gold Medalists":
    st.header("🥇 Age Distribution of Gold Medalists")

    gold = merged[(merged['Medal'] == 'Gold') & (merged['Age'].notna())]

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(gold['Age'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

    explain_button(
        "Explain age distribution of Olympic gold medalists and peak performance age.",
        "age_gold"
    )

elif section == "Women in Olympics":
    st.header("♀️ Women in Summer Olympics")

    women = merged[(merged['Sex'] == 'F') & (merged['Season'] == 'Summer')]

    fig, ax = plt.subplots(figsize=(12, 5))
    sns.countplot(x='Year', data=women, ax=ax)
    ax.tick_params(axis='x', rotation=90)
    st.pyplot(fig)

    explain_button(
        "Explain the trend of women's participation in the Olympics.",
        "women_trend"
    )

elif section == "Medals per Country":
    st.header("🌍 Medals per Country")

    medal_df = merged[merged['Medal'].notna()]
    unique_medals = medal_df.drop_duplicates(['Year', 'Event', 'NOC', 'Medal'])

    top10 = unique_medals.groupby('region').size().sort_values(ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=top10.index, y=top10.values, ax=ax)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    explain_button(
        "Explain why certain countries dominate Olympic medal counts.",
        "medals_country"
    )

elif section == "Height vs Weight":
    st.header("📏 Height vs Weight of Gold Medalists")

    gold = merged[
        (merged['Medal'] == 'Gold') &
        (merged['Height'].notna()) &
        (merged['Weight'].notna())
    ]

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='Height', y='Weight', data=gold, ax=ax)
    st.pyplot(fig)

    explain_button(
        "Explain relationship between height and weight among gold medalists.",
        "height_weight"
    )

elif section == "Evolution Over Time":
    st.header("📈 Evolution of Participation")

    men = merged[(merged['Sex'] == 'M') & (merged['Season'] == 'Summer')]
    women = merged[(merged['Sex'] == 'F') & (merged['Season'] == 'Summer')]

    fig, ax = plt.subplots(figsize=(12, 5))
    men.groupby('Year').size().plot(ax=ax, label="Men")
    women.groupby('Year').size().plot(ax=ax, label="Women")
    ax.legend()
    st.pyplot(fig)

    explain_button(
        "Explain male vs female participation trends over time.",
        "evolution_gender"
    )

elif section == "World Medal Map":
    st.header("🌍 Olympic Medal Map")

    medal_df = filtered[filtered['Medal'].notna()]
    unique_medals = medal_df.drop_duplicates(['Year', 'Event', 'NOC', 'Medal'])

    country_medals = unique_medals.groupby('region').size().reset_index(name='Total')

    fig = px.choropleth(
        country_medals,
        locations="region",
        locationmode="country names",
        color="Total",
        color_continuous_scale="Plasma"
    )

    st.plotly_chart(fig, use_container_width=True)

    explain_button(
        "Explain global Olympic medal distribution shown on the map.",
        "world_map"
    )

elif section == "Conclusions":
    st.header("📝 Conclusions")

    st.markdown("""
    - Olympic participation expanded globally  
    - Female inclusion increased consistently  
    - Physical specialization evolved by sport  
    - Medal dominance reflects investment & infrastructure  
    """)
