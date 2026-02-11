import streamlit as st

st.set_page_config(layout="wide")

# --- YAN MENÜ (SIDEBAR) ---
# GÖREV 1: st.sidebar kullanarak bir başlık ekleyin.
# KODU BURAYA YAZIN
# st.sidebar.title("Kontrol Paneli")

# GÖREV 2: Takımın forma rengini seçmek için bir renk seçici (color_picker) ekleyin.
# KODU BURAYA YAZIN
# seçilen_renk = st.sidebar.color_picker("Forma Rengi Seç", "#FFFFFF")

# GÖREV 3: Takımın oyun modunu seçmek için bir seçim kutusu (selectbox) ekleyin.
# KODU BURAYA YAZIN
# oyun_modu = st.sidebar.selectbox("Oyun Modu Seç", ["Hücum", "Dengeli", "Savunma"])

# GÖREV 4: Seçilen renk ve oyun modu bilgisini yan menüye yazdırın.
# KODU BURAYA YAZIN
# st.sidebar.write("Seçilen Forma Rengi:", seçilen_renk)
# st.sidebar.write("Seçilen Oyun Modu:", oyun_modu)


# --- ANA SAYFA ---
st.title("🚀 Spor Kulübü Portalı")
st.write("Kulübümüzün yıldız oyuncularıyla tanışın!")

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
