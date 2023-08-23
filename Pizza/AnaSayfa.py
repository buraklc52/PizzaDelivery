import streamlit as st
import sqlite3
import pandas as pd

st.header("Anasayfa")

conn = sqlite3.connect("pizza.db")
c = conn.cursor()

c.execute("SELECT * FROM siparisler")
siparisler = c.fetchall()

df = pd.DataFrame(siparisler)

df.columns = ("isim","adres","pizza","boy","icecek","toplamPrice")

st.table(df)


