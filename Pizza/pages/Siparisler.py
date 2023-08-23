import streamlit as st
import sqlite3

conn = sqlite3.connect("pizza.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS siparisler(isim text, adres text, pizza text, boy text, icecek text, fiyat real)")
conn.commit()

c.execute("SELECT isim FROM pizzalar")
isimler = c.fetchall()

isimlerlist = []
for i in isimler:
    isimlerlist.append(i[0])

st.header("Siparişler")

with st.form("siparis",clear_on_submit=True):
    isim = st.text_input("İsim Soyisim: ")
    adres = st.text_area("Adres: ")
    pizza = st.selectbox("Pizza Seç",isimlerlist)
    boy = st.selectbox("Boyut Seç",["Küçük","Orta","Büyük"])
    icecek = st.selectbox("İçecek Seç",["Ayran","Kola","Sprite","Fanta","Ice Tea"])
    siparisver = st.form_submit_button("Sipariş Ver")

    if siparisver:
        if boy == "Küçük":
            c.execute("SELECT smPrice FROM pizzalar WHERE isim=?",(pizza,))
            fiyat = c.fetchone()
        elif boy == "Orta":
            c.execute("SELECT mdPrice FROM pizzalar WHERE isim=?",(pizza,))
            fiyat = c.fetchone()
        elif boy == "Büyük":
            c.execute("SELECT lgPrice FROM pizzalar WHERE isim=?",(pizza,))
            fiyat = c.fetchone()

        icecekler = {
            "Ayran":15,
            "Kola":25,
            "Fanta":25,
            "Sprite":25,
            "Ice Tea":25
        }  

        icecekPrice = icecekler[icecek]
        toplamPrice = fiyat[0] + icecekPrice

        c.execute("INSERT INTO siparisler VALUES(?,?,?,?,?,?)",(isim,adres,pizza,boy,icecek,toplamPrice)) 
        conn.commit()

        st.success(f"Siparişiniz Alındı , Toplam Fiyat : {toplamPrice} ₺") 

        st.write(toplamPrice)
