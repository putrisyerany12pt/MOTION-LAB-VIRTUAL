import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Motion Lab", page_icon="🚀")

st.title("🚀 Motion Lab")
st.caption("Aplikasi Belajar Fisika Gerak")

menu = st.sidebar.selectbox(
    "Menu",
    ["🏃 GLB", "🚗 GLBB", "📊 Grafik", "🎯 Amunisi", "🎮 Quiz"]
)

# ================= GLB =================
if menu == "🏃 GLB":
    st.header("Gerak Lurus Beraturan")
    st.info("Rumus: v = s / t")

    s = st.number_input("Jarak (m)", min_value=0.0)
    t = st.number_input("Waktu (s)", min_value=0.0)

    if st.button("Hitung GLB"):
        if t != 0:
            v = s / t
            st.success(f"Kecepatan = {v:.2f} m/s")
        else:
            st.error("Waktu tidak boleh nol!")

# ================= GLBB =================
elif menu == "🚗 GLBB":
    st.header("Gerak Lurus Berubah Beraturan")
    st.info("Rumus: v = v₀ + a·t")

    v0 = st.number_input("Kecepatan awal", value=0.0)
    a = st.number_input("Percepatan", value=0.0)
    t = st.number_input("Waktu", value=0.0)

    if st.button("Hitung GLBB"):
        v = v0 + a * t
        st.success(f"Kecepatan akhir = {v:.2f} m/s")

# ================= GRAFIK =================
elif menu == "📊 Grafik":
    st.header("Grafik Jarak vs Waktu")

    v = st.slider("Kecepatan", 1, 50, 10)

    t = np.linspace(0, 10, 100)
    s = v * t

    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.set_xlabel("Waktu (s)")
    ax.set_ylabel("Jarak (m)")

    st.pyplot(fig)

# ================= AMUNISI =================
elif menu == "🎯 Amunisi":
    st.header("Latihan Harian")

    st.write("Mobil menempuh 100 m dalam 10 detik")

    if st.button("Lihat Jawaban"):
        st.success("Jawaban: 10 m/s")

# ================= QUIZ =================
elif menu == "🎮 Quiz":
    st.header("Quiz Fisika")

    jawaban = st.radio(
        "Kecepatan 5 m/s selama 4 detik, jarak?",
        ["10 m", "20 m", "25 m"]
    )

    if st.button("Cek"):
        if jawaban == "20 m":
            st.success("Benar!")
        else:
            st.error("Salah!")

st.markdown("---")
st.caption("Motion Lab 🚀")
