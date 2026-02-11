import streamlit as st

st.set_page_config(layout="wide")

# --- YAN MENÜ (SIDEBAR) ---
st.sidebar.title("Kontrol Paneli")
seçilen_renk = st.sidebar.color_picker("Forma Rengi Seç", "#FF0000")
oyun_modu = st.sidebar.selectbox("Oyun Modu Seç", ["Hücum", "Dengeli", "Savunma"])
st.sidebar.write("Seçilen Forma Rengi:", seçilen_renk)
st.sidebar.write("Seçilen Oyun Modu:", oyun_modu)

# --- ANA SAYFA ---

# GÖREV 1: Sayfanın en üstüne iki sütun oluşturun. Biri logo, diğeri istatistikler için.
# Sütun genişliklerini ayarlayabilirsiniz. Örnek: logo_col, stats_col = st.columns([1, 3])
# KODU BURAYA YAZIN
# logo_col, stats_col = st.columns([1, 3]) # Yorumdan çıkarın

# with logo_col:
    # GÖREV 2: st.image kullanarak 'M5L2/img/1.png' dosyasını gösterin.
    # Genişliğini 150 piksel yapabilirsiniz: width=150
    # KODU BURAYA YAZIN
    # st.image("M5L2/img/1.png", width=150)

# with stats_col:
    # GÖREV 3: st.metric kullanarak takımın istatistiklerini gösterin.
    # 3'lü bir sütun daha oluşturarak metrikleri yan yana dizebilirsiniz.
    # KODU BURAYA YAZIN
    # m1, m2, m3 = st.columns(3)
    # with m1:
        # st.metric("🏆 Kazanma Oranı", "85%", " +2.5%")
    # with m2:
        # st.metric("⚽ Atılan Gol", "112")
    # with m3:
        # st.metric("⭐ Puan", "99")


st.title("🚀 Spor Kulübü Portalı")
st.write("Kulübümüzün yıldız oyuncularıyla tanışın!")

# ... (Oyuncu kartları kodu aşağıda aynı kalacak)
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Arda Güler")
    st.write("Pozisyon: Ofansif Orta Saha")
    st.markdown("🏆 Genç Yetenek")
with col2:
    st.subheader("Hakan Çalhanoğlu")
    st.write("Pozisyon: Merkez Orta Saha")
    st.markdown("🎯 Oyun Kurucu")
with col3:
    st.subheader("Zeki Çelik")
    st.write("Pozisyon: Sağ Bek")
    st.markdown("🛡️ Kaya Gibi Defans")
