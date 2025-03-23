---
title: Support Ticket Classifier
emoji: 🌖
colorFrom: gray
colorTo: pink
sdk: streamlit
sdk_version: 1.43.2
app_file: app.py
pinned: false
license: mit
short_description: Clasificador de tickets de soporte en español
---
# 🧠 Support Ticket Classifier

Clasificador inteligente de tickets de soporte usando Machine Learning y NLP (Procesamiento del Lenguaje Natural). Esta aplicación permite predecir la categoría de un ticket de soporte a partir del texto proporcionado, facilitando su gestión automática.

## 🚀 ¿Qué hace esta app?

Utiliza un modelo de clasificación entrenado con `TfidfVectorizer` y `MultinomialNB` para asignar automáticamente una categoría a un ticket de soporte.

Ejemplo de entrada:

"El sistema no me deja acceder con mis credenciales"

Salida esperada:

"Problemas de acceso"


## 🛠️ Tecnologías usadas

- Python 🐍
- scikit-learn 🤖
- TfidfVectorizer + MultinomialNB
- Hugging Face Spaces
- Streamlit


## ▶️ Cómo ejecutar localmente

1. Instala las dependencias:

`pip install -r requirements.txt`

2. Entrena el modelo (si no lo has hecho ya):

`python train.py`


3. Accede a la interfaz web en: http://localhost:8000

## 🌐 Hugging Face Space

Puedes probar la app directamente en Hugging Face:

🔗 [Pruébalo haciendo clic aqui](huggingface.co/spaces/AgusDev1981/support-ticket-classifier)

## 📄 Licencia
Este proyecto está bajo la licencia MIT.

Consulta el archivo LICENSE para más detalles.

## 🧑‍💻 Autor

AgusDev

[Web](https://www.agusdev.es/)

[GitHub](https://github.com/AgustinZP) – [Hugging Face](https://huggingface.co/spaces/AgusDev1981)