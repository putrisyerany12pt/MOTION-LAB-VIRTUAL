import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🚀 Motion Lab")

menu = st.selectbox("Menu", ["GLB", "GLBB", "Grafik"])

if menu == "GLB":
    s = st.number_input("Jarak")
    t = st.number_input("Waktu")

    if st.button("Hitung"):
        if t != 0:
            st.success(s/t)
        else:
            st.error("Waktu nol")

elif menu == "GLBB":
    v0 = st.number_input("v0")
    a = st.number_input("a")
    t = st.number_input("t")

    if st.button("Hitung GLBB"):
        st.success(v0 + a*t)

elif menu == "Grafik":
    v = 10
    t = np.linspace(0,10,100)
    s = v*t

    fig, ax = plt.subplots()
    ax.plot(t,s)
    st.pyplot(fig)
