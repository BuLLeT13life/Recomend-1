import streamlit as st
import pandas as pd
import time
st.title('Рекомендательная программа ')


def load_file():
    uploaded_file = st.file_uploader(label="Выберите файл для загрузки")
    if uploaded_file is not None:
        # st.balloons()
        uploaded_file = pd.read_csv(uploaded_file, sep=" \t ")

        return uploaded_file
    else:
        return None


data = load_file()

# tab1, tab2 = st.tabs( ["ГГ", "ГГ"] , "<h1 style='text-align: center;</h1>")
col1, col2 = st.columns(2)
with col1:
    st.header("Первый способ ")
    with st.expander("See explanation"):
        st.write("Анотация к способу ")
        st.image("https://static.streamlit.io/examples/dice.jpg")
    if st.button("За работу"):
        st.table(data)


with col2:
    st.header("Второй способ")

    with st.expander("See explanation"):
        st.write("Анотация к способу ")
        st.image("https://static.streamlit.io/examples/dice.jpg")
    if st.button("За работу "):
        st.table(data)


