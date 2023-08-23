import streamlit as st
import sqlite3

st.header("Katalog")

conn = sqlite3.connect("pizza.db")
c = conn.cursor()

c.execute("SELECT * FROM pizzalar")
pizzalar = c.fetchall()

for pizza in pizzalar:
    col1,col2,col3 = st.columns(3)
    with col1:
        st.image(pizza[5])
    with col2:
        st.subheader(pizza[0])
        st.write(pizza[4])
    with col3:
        st.write("Küçük boy" , pizza[1] , "₺")
        st.write("Orta boy" , pizza[2] , "₺")
        st.write("Büyük boy" , pizza[3] , "₺")    
