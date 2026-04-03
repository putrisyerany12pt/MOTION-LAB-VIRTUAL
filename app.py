import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# CONFIG
st.set_page_config(page_title="Motion Lab", page_icon="🚀")

# TITLE
st.title("🚀 Motion Lab")
st.caption("Belajar Fisika Gerak Interaktif")

# MENU
menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["🏃 GLB", "🚗 GLBB", "📊 Grafik", "🎯 Amunisi", "🎮 Quiz"]
)

# ================= GLB =================
if menu == "🏃 GLB":
    st.header("Gerak Lurus Beraturan")

    st.info("Rumus: v = s / t")

    s = st.number_input("Jarak (m)")
    t = st.number_input("Waktu (s)")

    if st.button("Hitung"):
        if t != 0:
            v = s / t
            st.success(f"🚀 Kecepatan = {v:.2f} m/s")
        else:
            st.error("Waktu tidak boleh nol!")

# ================= GLBB =================
elif menu == "🚗 GLBB":
    st.header("Gerak Lurus Berubah Beraturan")

    st.info("Rumus: v = v₀ + a·t")

    v0 = st.number_input("Kecepatan awal (m/s)")
    a = st.number_input("Percepatan (m/s²)")
    t = st.number_input("Waktu (s)")

    if st.button("Hitung"):
        v = v0 + a * t
        st.success(f"🚗 Kecepatan akhir = {v:.2f} m/s")

# ================= GRAFIK =================
elif menu == "📊 Grafik":
    st.header("Grafik Gerak (Jarak vs Waktu)")

    v = st.slider("Kecepatan (m/s)", 1, 50, 10)

    t = np.linspace(0, 10, 100)
    s = v * t

    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.set_xlabel("Waktu (s)")
    ax.set_ylabel("Jarak (m)")
    ax.set_title("Grafik GLB")

    st.pyplot(fig)

# ================= AMUNISI =================
elif menu == "🎯 Amunisi":
    st.header("🎯 Latihan Harian")

    st.write("🚗 Mobil menempuh 120 meter dalam 10 detik.")
    st.write("Berapa kecepatannya?")

    if st.button("Lihat Jawaban"):
        st.success("Jawaban: 12 m/s")
        st.info("Kecepatan = jarak ÷ waktu")

# ================= QUIZ =================
elif menu == "🎮 Quiz":
    st.header("🎮 Quiz Fisika")

    jawaban = st.radio(
        "Jika kecepatan 5 m/s selama 4 detik, berapa jaraknya?",
        ["10 m", "20 m", "25 m"]
    )

    if st.button("Cek Jawaban"):
        if jawaban == "20 m":
            st.success("Benar! 🎉")
        else:
            st.error("Salah, coba lagi!")

# FOOTER
st.markdown("---")
st.caption("Made with ❤️ | Motion Lab")
