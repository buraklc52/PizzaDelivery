import streamlit as st
import sqlite3


conn = sqlite3.connect("pizza.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS pizzalar(isim text, smPrice real, mdPrice real, lgPrice real, icindekiler text, resim text)")
conn.commit()

st.header("Pizza Ekle")

with st.form("pizzaekle",clear_on_submit=True):
    isim = st.text_input("Pizza İsmi: ")
    smPrice = st.number_input("Küçük Boy Fiyat: ")
    mdPrice = st.number_input("Orta Boy Fiyat: ")
    lgPrice = st.number_input("Büyük Boy Fiyat: ")
    icindekiler = st.multiselect("İçindekiler",["Mantar","Jambon","Pastırma","Zeytin","Mısır","Sucuk","Salam","Sosis","Tavuk"])

    resim = st.file_uploader("Pizza Resmi Ekle")
    ekle = st.form_submit_button("Pizza Ekle")

    if ekle:
        icindekiler = str(icindekiler)
        icindekiler = icindekiler.replace("[","")
        icindekiler = icindekiler.replace("]","")
        icindekiler = icindekiler.replace("'","")
        

    resimurl = "img/" + resim.name
    
    open(resimurl,"wb").write(resim.read())

    c.execute("INSERT INTO pizzalar VALUES(?,?,?,?,?,?)",(isim,smPrice,mdPrice,lgPrice,icindekiler,resimurl))
    conn.commit()

    st.success("Pizza Başarıyla Eklendi")