import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="AeroPersonalize", layout="wide")
st.title("🎯 AeroPersonalize – Experiencia de Pasajero Personalizada con IA")

# Introducción
st.markdown("""
### ¿Qué es AeroPersonalize?
AeroPersonalize es una solución de inteligencia artificial que personaliza la experiencia del pasajero en tiempo real, desde la reserva hasta el post-vuelo. Esta demo simula los módulos clave de personalización y predicción del sistema.
""")

# Simulación de Datos de Cliente
st.header("👤 Datos del Pasajero")
data = {
    'ID Cliente': ['USR2045'],
    'Tipo pasajero': ['Frecuente Gold'],
    'Último vuelo': ['MAD → MEX'],
    'Preferencia comida': ['Vegetariana'],
    'Idioma': ['Español'],
    'Historial incidencias': ['Retraso 3h en 2023'],
    'Check-in digital': [True]
}
df = pd.DataFrame(data)
st.dataframe(df)

# IA de Personalización
st.header("🧠 Motor de IA de Personalización")
st.markdown("""
La IA analiza estos datos para personalizar:
- Comunicación (idioma, tono, canal)
- Servicios ofrecidos (comida, transfer, asientos)
- Recomendaciones de entretenimiento
- Propuestas de upgrade o promociones
""")

# Resultados simulados del sistema
results = {
    'Mensaje app': ["Hola, te hemos reservado menú vegetariano y FastTrack en MEX. ¡Buen vuelo!"],
    'Contenido sugerido a bordo': ["Películas en español y documentales de viaje"],
    'Oferta personalizada': ["Upgrade a business con 25% de descuento"]
}
st.subheader("🎁 Personalización generada")
st.table(pd.DataFrame(results))

# Panel de satisfacción esperada
st.header("📊 Predicción de Satisfacción y Engagement")
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("😊 NPS estimado", "82", "+12")
kpi2.metric("💬 Prob. clic en oferta", "43%", "+40%")
kpi3.metric("📩 Apertura de email", "61%", "+25%")

# Footer
st.markdown("""
---
Aplicación demo desarrollada con [Streamlit](https://streamlit.io/) | Repositorio: [GitHub - AeroPersonalize](https://github.com/tuusuario/aeropersonalize-demo)
""")
