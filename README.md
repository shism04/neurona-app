# 🧠 ¡Hola Neurona! - Streamlit App

**¡Hola Neurona!** is an educational web application built with **Streamlit** designed to visualize and calculate the output of a basic artificial neuron. Users can interactively adjust weights, inputs, and bias to see how the mathematical model responds.

[Click here](https://neurona-app-fpdbs3mhuktxhp4afqfvfw.streamlit.app/) to see the app running.

The app demonstrates the fundamental calculation of a neuron:

$$Output = \sum_{i}(w_{i} \cdot x_{i}) + b$$

---

## ✨ Features

- **Multi-Input Configurations:** Three distinct modes organized by tabs:
    - **One Input:** Simple $w_0 \cdot x_0$ calculation.
    - **Two Inputs:** Calculation for $w_0, w_1$ and $x_0, x_1$.
    - **Three Inputs & Bias:** Full calculation including a custom bias (sesgo) value.
- **Interactive UI:** * 🎚️ **Sliders:** Precisely adjust weights ($w$) between 0.0 and 4.0.
    - 🔢 **Number Inputs:** Enter specific values for inputs ($x$) and bias.
- **Real-time Logic:** Uses Python's `functools.reduce` to efficiently process the weighted sums.

---

## 🛠️ Installation & Setup

To run this project locally, follow these steps:

1. **Clone the repository:**Bash
    
    `git clone https://github.com/shism04/hola-neurona-app.git
    cd hola-neurona-app`
    
2. **Create a virtual environment:**Bash
    
    `python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate`
    
3. **Install dependencies:**Bash
    
    `pip install streamlit`
    
4. **Add Assets:** Ensure you have an image named `neurona.png` in the root directory for the app header.

---

## 🚀 How to Run

Launch the application by running the following command in your terminal:

Bash

`streamlit run app.py`

---

## 📁 Project Structure

Plaintext

`.
├── app.py                # Main application logic
├── neurona.png           # Visual diagram of a neuron
└── README.md             # Project documentation`

---

## 📊 Technical Stack

- **Language:** Python 3.x
- **Web Framework:** [Streamlit](https://streamlit.io/)
- **Functional Programming:** Used `functools.reduce` for the summation logic.

---

## 👤 Author

**Ismael Sihammou Anahnah** - *CPIFP Alan Turing*