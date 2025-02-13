# @copyright: Martin Rayan Rojas Ksiri


# Importamos las librerías necesarias

import pandas as pd
from datetime import datetime
#from docxtpl import DocxTemplate
import streamlit as st

def main():
    
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📋 Registro de Datos</h1>", unsafe_allow_html=True)
    st.write("### Por favor, completa los siguientes datos:")

    with st.form(key="seleccion_datos"):
            
            global dni, nombre, conductas, articulos, correccion

            dni = st.text_input("🔹 Ingresa tu DNI")
            nombre = st.text_input("🔹 Ingresa tu Nombre")
            conductas = st.selectbox("⚠️ Elige la Conducta", ["Conducta 1", "Conducta 2", "Conducta 3"])
            articulos = st.selectbox("📜 Elige el Artículo", ["Artículo 1", "Artículo 2", "Artículo 3"])
            correccion = st.selectbox("✅ Elige la Corrección", ["Corrección 1", "Corrección 2", "Corrección 3"])
            boton_enviar = st.form_submit_button(label="📩 Enviar")

    if boton_enviar:
        st.success(f"✅ ¡Hola **{nombre}**! Tus datos han sido registrados correctamente.")
        st.balloons()  

if __name__ == '__main__':
    main()

