import streamlit as st

st.title("🚀 Motion Lab")

menu = st.selectbox("Pilih Menu", ["GLB", "GLBB", "Amunisi"])

# ================= GLB =================
if menu == "GLB":
    st.header("Gerak Lurus Beraturan")

    s = st.number_input("Jarak (m)")
    t = st.number_input("Waktu (s)")

    if st.button("Hitung GLB"):
        if t != 0:
            v = s / t
            st.success(f"Kecepatan = {v} m/s")
        else:
            st.error("Waktu tidak boleh nol!")

# ================= GLBB =================
elif menu == "GLBB":
    st.header("Gerak Lurus Berubah Beraturan")

    v0 = st.number_input("Kecepatan awal (m/s)")
    a = st.number_input("Percepatan (m/s²)")
    t = st.number_input("Waktu (s)")

    if st.button("Hitung GLBB"):
        v = v0 + a * t
        st.success(f"Kecepatan akhir = {v} m/s")

# ================= AMUNISI =================
elif menu == "Amunisi":
    st.header("🎯 Amunisi Harian")

    st.write("Mobil menempuh 100 meter dalam 10 detik")

    if st.button("Lihat Jawaban"):
        st.success("Jawaban: 10 m/s")
