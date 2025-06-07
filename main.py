import streamlit as st

st.set_page_config(page_title="Analyse Fondamentale", page_icon="📊")

st.title("📊 Analyse Fondamentale Automatisée")
st.markdown("Bienvenue Lucien 👑")

actif = st.text_input("💹 Actif à analyser")
pays = st.text_input("🌍 Zone économique")

if actif:
    st.success(f"Actif sélectionné : {actif}")
if pays:
    st.info(f"Zone : {pays}")
