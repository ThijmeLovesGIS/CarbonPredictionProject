import streamlit as st
import pandas as pd

df = pd.read_csv("Data/Forests carbon stored.csv")

st.title("Total carbon stored")
st.write("Using the carbon calculations done before and the forest classification, the amount of carbon stored on the island can be calculated.")

st.space(size="small")

st.subheader("Carbon per hectare")
st.write("To be able to do the calculations first the carbon per hectare needs to be calculated. This is done by calculating the plot size in hectares (height*width/10000) then summarising all the carbon per plot. Using this the total carbon in kg per plot can then be divided by the plot size in hectares. This results in the following:")
c_ha = df[["Forest type", "Carbon per ha (kg)"]]
st.dataframe(c_ha, hide_index=True)

st.space(size="small")

st.subheader("Area per forest type")
st.write("The second part which is needed is to calculate the area per forest type in hectares. First it is needed to count the number of pixels per forest type. Using this together with the pixel size in hectares (pixel height*pixel width/10000). It results in the total area in hectares per forest type. As seen in the table below:")
a_ft = df[["Forest type", "Pixel count", "Area (ha)"]]
st.dataframe(a_ft, hide_index=True)

st.space(size="small")

st.subheader("Total amount of carbon per forest type")
st.write("The last two calculations can be combined to calculate the total amount of carbon per forest type. This is done by multiplying the total area in hectares per forest type and the carbon per hectares. The result can be viewed in the table below:")
tc_ft = df[["Forest type", "Total carbon (kg)"]]
tc_ft_total = pd.DataFrame({
    "Total carbon (kg)": [tc_ft["Total carbon (kg)"].sum()]
})
st.dataframe(tc_ft, hide_index=True)
st.write("By combing the total carbon per forest type it leads to a total carbon storage seen in the table below:")
st.dataframe (tc_ft_total, hide_index=True)

st.space(size="small")

st.subheader("Click below to read ideas for further research and further improvements")
st.page_link(
    "pages/6_Further_research.py",
    label="-> Further research"

)
