import streamlit  as st
import pandas as pd  
from PIL import Image
st.title("Titanic Dataset")
img = Image.open("dataset-cover (1).jpg")
st.image(img)




data = pd.read_csv("Titanic-Dataset.csv")




data_t , missing , encoding , filtring = st.tabs(["data" , 'missing' , "encoding" , "filtring"])

data_t.dataframe(data)
#data_t.dataframe(data.info())
data_t.text("describe for numeric data")
if data_t.button("numeric data") :
    data_t.dataframe(data.describe())

if data_t.button("qategorical data") :
    data_t.dataframe(data.describe(include = "object"))
missing.dataframe(data.isna().sum())
