import streamlit as st
import pandas as pd

df = pd.read_csv("Data/Forests carbon stored.csv")

st.title("Total carbon stored")
st.write("Using the carbon calculations of before and the forest classification, the amount of carbon stored on the island was calculated.")

st.space(size="small")

st.subheader("Carbon per hectare")
st.write("To do the calculations, the carbon per hectare needed to be calculated first. This was done by calculating the plot size in hectares (height*width/10000) and then summarising all the carbon per plot. The total carbon in kilograms per plot was then divided by the plot size in hectares. The results were as follows:")
c_ha = df[["Forest type", "Carbon per ha (kg)"]]
st.dataframe(c_ha, hide_index=True)

st.space(size="small")

st.subheader("Area per forest type")
st.write("The second part which was needed was to calculate the area per forest type in hectares. In order to do so,  the number of pixels were first counted per forest type, then, by multiplying this number with the the pixel size in hectares (pixel height*pixel width/10000) resulted in the total area in hectares per forest type. These were as follows:")
a_ft = df[["Forest type", "Pixel count", "Area (ha)"]]
st.dataframe(a_ft, hide_index=True)

st.space(size="small")

st.subheader("Total amount of carbon per forest type")
st.write("The last two calculations were then combined to calculate the total amount of carbon per forest type. This was done by multiplying the total area in hectares per forest type and the carbon per hectares. The result can be viewed in the table below:")
tc_ft = df[["Forest type", "Total carbon (kg)"]]
tc_ft_total = pd.DataFrame({
    "Total carbon (kg)": [tc_ft["Total carbon (kg)"].sum()]
})
st.dataframe(tc_ft, hide_index=True)
st.write("By combining the total carbon per forest type the  total carbon storage was calculated, as seen in the table below:")
st.dataframe (tc_ft_total, hide_index=True)

st.space(size="small")

st.subheader("Click below to read ideas for further research and further improvements")
st.page_link(
    "pages/6_Further_research.py",
    label="-> Further research"

)

