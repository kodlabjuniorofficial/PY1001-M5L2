import streamlit as st

st.set_page_config(layout="wide")

st.title("🚀 Spor Kulübü Portalı")
st.write("Kulübümüzün yıldız oyuncularıyla tanışın!")

# GÖREV 1: Sayfayı 3 eşit sütuna bölün.
# İpucu: st.columns(3) bir liste döndürür. Her bir elemanı bir sütunu temsil eder.
# Örnek: col1, col2, col3 = st.columns(3)

# ############## KODU AŞAĞIDAKİ YORUM SATIRINDAN ÇIKARIN ###############
# col1, col2, col3 = st.columns(3)
# ######################################################################


# --- Oyuncu 1 ---
# GÖREV 2: 'with col1:' bloğu oluşturun ve içine oyuncunun bilgilerini yazın.
# st.subheader() ile oyuncunun adını yazın.
# st.write() ile oyuncunun pozisyonunu belirtin.
# st.markdown() ile oyuncuya havalı bir emoji ekleyin (ör: "🏆 Şampiyon").
# KODU BURAYA YAZIN

# --- Oyuncu 2 ---
# GÖREV 3: 'with col2:' bloğu oluşturun ve içine ikinci oyuncunun bilgilerini yazın.
# KODU BURAYA YAZIN

# --- Oyuncu 3 ---
# GÖREV 4: 'with col3:' bloğu oluşturun ve içine üçüncü oyuncunun bilgilerini yazın.
# KODU BURAYA YAZIN

st.success("Tebrikler! Oyuncu kartlarını başarıyla oluşturdun.")
