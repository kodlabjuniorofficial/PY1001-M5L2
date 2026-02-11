import streamlit as st

st.set_page_config(layout="wide")

# --- (Önceki aşamalardan gelen kodlar) ---
st.sidebar.title("Kontrol Paneli")
st.sidebar.color_picker("Forma Rengi Seç", "#FF0000")
st.sidebar.selectbox("Oyun Modu Seç", ["Hücum", "Dengeli", "Savunma"])
logo_col, stats_col = st.columns([1, 4])
with logo_col:
    st.image("M5L2/img/1.png", width=150)
with stats_col:
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("🏆 Kazanma Oranı", "85%", "+2.5%")
    with m2: st.metric("⚽ Atılan Gol", "112")
    with m3: st.metric("⭐ Puan", "99")
st.title("🚀 Spor Kulübü Portalı")
st.write("Kulübümüzün yıldız oyuncularıyla tanışın!")
# --- (Kod sonu) ---


col1, col2, col3 = st.columns(3)

# --- Oyuncu 1 ---
with col1:
    st.subheader("Arda Güler")
    st.write("Pozisyon: Ofansif Orta Saha")
    st.markdown("🏆 Genç Yetenek")
    
    # GÖREV 1: "Detayları Gör" başlıklı bir expander oluşturun.
    # with st.expander("Detayları Gör"):
        # GÖREV 2: Expander içine oyuncunun istatistiklerini yazın.
        # st.write("Bu sezon 15 gol ve 20 asist ile oynadı.")
        # st.bar_chart({"data": [15, 20]}) # Bonus: Grafik ekleme
        # KODU BURAYA YAZIN


# --- Oyuncu 2 ---
with col2:
    st.subheader("Hakan Çalhanoğlu")
    st.write("Pozisyon: Merkez Orta Saha")
    st.markdown("🎯 Oyun Kurucu")
    
    # GÖREV 3: İkinci oyuncu için de bir expander oluşturun ve bilgi ekleyin.
    # KODU BURAYA YAZIN


# --- Oyuncu 3 ---
with col3:
    st.subheader("Zeki Çelik")
    st.write("Pozisyon: Sağ Bek")
    st.markdown("🛡️ Kaya Gibi Defans")
    
    # GÖREV 4: Üçüncü oyuncu için de bir expander oluşturun ve bilgi ekleyin.
    # KODU BURAYA YAZIN