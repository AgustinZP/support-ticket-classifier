# app.py
import streamlit as st
import joblib

# Cargar el modelo
model = joblib.load("model/ticket_model.pkl")

st.set_page_config(page_title="Clasificador de Tickets", layout="centered")

st.title("🗂️ Clasificador de Tickets de Soporte")
st.markdown("Introduce el mensaje de un ticket y predice su categoría automáticamente.")

# Ejemplos
ejemplos = [
    "No puedo acceder a mi cuenta",
    "¿Por qué me cobraron dos veces?",
    "La aplicación no carga",
    "Quiero actualizar mi tarjeta",
    "Mi pedido no ha llegado",
    "El sistema se cayó hoy",
    "Deseo cambiar mi dirección de envío",
    "No reconozco este cargo en mi tarjeta",
]

# Selector de ejemplos
ejemplo_seleccionado = st.selectbox("📌 Ejemplos de tickets frecuentes:", [""] + ejemplos)

message = st.text_area("Escribe el mensaje del ticket", value=ejemplo_seleccionado, height=150)

if st.button("🔍 Clasificar"):
    if message.strip() == "":
        st.warning("⚠️ Por favor, escribe un mensaje.")
    else:
        with st.spinner("Clasificando..."):
            prediction = model.predict([message])[0]
            st.success(f"🧠 Categoría predicha: **{prediction}**")
