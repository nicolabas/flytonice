
import streamlit as st
from PIL import Image
import base64

# -------- CONFIGURATION --------
st.set_page_config(page_title="FlyToNiCE", page_icon="✈️", layout="wide")

# -------- BACKGROUND IMAGE / SUNSET COLOR --------
def set_bg():
    page_bg_img = f"""
    <style>
    body {{
    background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/A%C3%A9roport_de_Nice_C%C3%B4te_d%27Azur_%28vue_du_ciel%29.jpg/1280px-A%C3%A9roport_de_Nice_C%C3%B4te_d%27Azur_%28vue_du_ciel%29.jpg");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
    filter: blur(2px);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_bg()

# -------- LOGO --------
st.markdown(
    """
    <div style="position: absolute; top: 25px; left: 30px;">
        <img src="https://raw.githubusercontent.com/streamlit/streamlit/develop/examples/data/logo.png" width="100">
    </div>
    """,
    unsafe_allow_html=True
)

# -------- SIDEBAR MENU --------
st.sidebar.title("📌 Menu FlyToNiCE")
menu = st.sidebar.radio("Naviguer vers :", ["🏠 Accueil", "📸 Galerie", "🧠 Quiz", "🛬 Arrivées"])

# -------- MODULES --------
if menu == "🏠 Accueil":
    st.markdown("<h1 style='color:#ffffff;'>🛫 Bienvenue sur FlyToNiCE</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#ffffff;'>Le carnet de bord interactif des voyageurs qui atterrissent à Nice ✨</h3>", unsafe_allow_html=True)

elif menu == "📸 Galerie":
    st.markdown("## 📸 Galerie photo (bientôt dynamique)")
    cols = st.columns(3)
    urls = [
        "https://upload.wikimedia.org/wikipedia/commons/e/e4/Nice_vue_g%C3%A9n%C3%A9rale.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/3/3b/Nice_baie_des_anges.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/7/75/Nice_Promenade_du_Paillon_2016.jpg"
    ]
    for i, url in enumerate(urls):
        with cols[i % 3]:
            st.image(url, use_column_width=True)

elif menu == "🧠 Quiz":
    st.markdown("## 🧠 Es-tu un·e vrai·e Niçois·e de cœur ?")
    score = 0

    q1 = st.radio("Ta première envie quand tu poses le pied à Nice ?", ["Aller à la plage", "Boire un café en terrasse", "Dormir", "Faire un tour sur la promenade"])
    if q1 == "Aller à la plage":
        score += 1

    q2 = st.radio("Ton moyen de transport préféré ?", ["Avion", "Train", "Bus", "Vélo"])
    if q2 == "Train":
        score += 1

    q3 = st.radio("Tu n'oublies jamais dans ta valise :", ["Lunettes de soleil", "Ton chargeur", "Un livre", "Du parmesan"])
    if q3 == "Lunettes de soleil":
        score += 1

    if st.button("Voir mon profil ☀️"):
        if score == 3:
            st.success("Tu es 100% soleil, 100% Niçois·e 💛")
        elif score == 2:
            st.success("Presque local·e, mais encore un peu touriste 😄")
        else:
            st.success("Tu es en route pour découvrir le vrai goût du Sud 🌊")

elif menu == "🛬 Arrivées":
    st.markdown("## ✈️ Tableau des arrivées")
    st.write("Fonction à venir : formulaire + tableau interactif des arrivées.")
    st.info("Ce module sera bientôt activé.")
