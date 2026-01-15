import streamlit as st

st.title("Carbon prediction project")
st.write("Welcome to the Streamlit, which will take you through the project I have been working on during my time at the Archipelagos Institute of Marine Conservation (01/09/2025-30/01/2026).")

st.space(size="small")

st.header("Who am I")
st.write("My name is Thijme Jonckers, I am 20 years old and from the Netherlands. I am currently in my final year of my Bsc International Forest and Nature Management, specialising in Tropical Forestry at Van Hall Larenstein University of Applied Sciences.")
st.write("During my final year at university it is required to complete a 5 month internship. I got the opportunity to follow an internship at Archipelagos Institute of Marine Conservation with the GIS team. During my study I discovered my interest in GIS and data analysis, and using these methods to solve real-world environmental problems. As such, the GIS-internship I got offered at Archipelagos was perfect for me.")

st.space(size="small")

st.header("Goal")
st.write("During my time here I worked on a project to estimate how much carbon is stored on the island of Samos, Greece. This work contributes to some of the conservation goals that Archipelagos aims to achieve. Moreover, this served as a  final project  that showed how I could apply the knowledge I gained at my university while additionally  developing my skills further During my stay at Archipelagos,I also needed to work on personal goals that were set up by the university. As such, I decided to do this project in Python since I had no previous knowledge on using the programming language while it plays an essential part in the GIS sphere. Thus, I decided to learn how to adapt my GIS knowledge by using Python.")

st.space(size="small")

st.header("The project")
st.write("The following steps were undertaken to complete this project:")

st.page_link(
    "pages/1_Field_measurements.py",
    label="-> Field measurements in the Nightingale Valley"
)

st.page_link(
    "pages/2_Statistics.py",
    label="-> Statistics run on the field measurements"
)

st.page_link(
    "pages/3_Carbon_calculations.py",
    label="-> Carbon calculation based on the field measurements"
)

st.page_link(
    "pages/4_Classification.py",
    label="-> Random forest classification of Sentinel-2 imagery"
)

st.page_link(
    "pages/5_Total_carbon_stored.py",
    label="-> Use classification map and carbon calculations to predict total carbon stored"
)

st.space(size="small")

st.subheader("Disclaimer")

st.write("The results of this project are a prediction and not a precise conclusion on the total amount of carbon stored. It is meant to give an estimate, rather than a final conclusion.")

