# 👟 ShoeVsion

**ShoeVsion** is a Streamlit-based web app that classifies shoe types (e.g. Boot, Sneaker, Sandal) and detects their dominant colors using a custom-trained image classification model.

## 🚀 Features

- Upload an image of a shoe and get the predicted class
- Visual display of dominant color
- Interactive and clean frontend built with Streamlit
- Powered by a deep learning model (CNN-based)

## 🧠 Model

The model is stored locally due to size constraints. You can specify the model filename in the app interface.

If you want to train and use your own model:

- Use the notebooks provided in the `notebooks/` folder as a starting point
- The dataset used for training is available here:  
  [Shoe vs Sandal vs Boot Dataset (15k images)](https://www.kaggle.com/datasets/hasibalmuzdadid/shoe-vs-sandal-vs-boot-dataset-15k-images)
- Once trained, drop your model file (`.h5`, `.pt`, etc.) into the `main app/` folder
- Specify the filename in the input box on the web app to load your model

---

## 🧰 Deployment

This project is deployed using [Streamlit Cloud](https://streamlit.io/cloud).

---

[Try ShoeVsion live!](https://shoevision.streamlit.app/) ✨

---

## 📦 Installation

```bash
pip install -r requirements.txt
streamlit run app.py
