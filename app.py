import streamlit as st
import requests

st.set_page_config(page_title="Clasificador de Tickets", layout="centered")

st.title("🗂️ Clasificador de Tickets de Soporte")
st.markdown("Introduce el mensaje de un ticket y predice su categoria automáticamente.")

# Examples
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

# Examples selector
ejemplo_seleccionado = st.selectbox("📌 Ejemplos de tickets frecuentes:", [""] + ejemplos)

message = st.text_area("Escribe el mensaje del ticket", value=ejemplo_seleccionado, height=150)

if st.button("🔍 Clasificar"):
    if message.strip() == "":
        st.warning("⚠️ Por favor, escribe un mensaje.")
    else:
        try:
            with st.spinner("Clasificando..."):
                response = requests.post(
                    "http://localhost:8000/predict",
                    json={"message": message}
                )

            if response.status_code == 200:
                prediction = response.json()["category"]
                st.success(f"🧠 Categoria predicha: **{prediction}**")
            else:
                st.error(f"Error en la predicción: {response.text}")

        except requests.exceptions.ConnectionError:
            st.error("❌ No se pudo conectar con la API. ¿Está corriendo FastAPI en http://localhost:8000?")