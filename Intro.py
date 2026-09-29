import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Gradientes")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace usaremos una aplicación de IA para explorar cómo las derivadas y el gradiente convierten un problema matemático en un proceso de búsqueda y optimización.") 
 url = "https://imultimod.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Lógica, Big-O y Vectorización")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En el siguiente enlace usaremos una aplicación de IA para explorar la cadena que une la lógica, la complejidad Big-O y la vectorización, pilares para construir sistemas de IA eficientes y escalables.") 
 url = "https://yolov5cmc.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Aplicación Preparación de datos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace usaremos una aplicación de IA para trabajar con datos ambientales reales de la plataforma MARCO de Cornare, accedidos mediante APIs y endpoints de estaciones de monitoreo.") 
 url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Regresión Lineal")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace usaremos una aplicación de IA para estudiar la regresión lineal simple y múltiple, una técnica clave del Machine Learning para predecir valores numéricos a partir de datos históricos.") 
 url = "https://traductorw.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Series de Tiempo.")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace usaremos una aplicación de IA para aprender a pronosticar el futuro a partir de datos históricos mediante series de tiempo..") 
 url = "https://dataagente.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Predicción y modelado de la calidad de aire.")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace usaremos una aplicación de IA para predecir y modelar la calidad del aire, en particular el material particulado PM2.5 y PM10, que afecta la salud humana.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Clasificación Knn")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace usaremos una aplicación de IA para conocer el algoritmo K vecinos más cercanos (KNN), un método simple e intuitivo que captura fronteras no lineales en clasificación y regresión.") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Clasificación de fertilidad de  suelos")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace usaremos una aplicación de IA para clasificar la fertilidad de suelos de AGROSAVIA (baja, media o alta) a partir de sus análisis químicos con K vecinos más cercanos (KNN).") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Visualización de Datos, Story telling y PCA para datos energéticos")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace usaremos una aplicación de IA para analizar y presentar datos de consumo energético mediante visualización de datos, storytelling y PCA.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")





