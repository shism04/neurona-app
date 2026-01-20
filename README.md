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

The easiest way to run this project is using **Docker**, which handles all dependencies and environment configurations automatically.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.

### Steps to Run

1. **Clone the repository:**

    ```Bash
    git clone https://github.com/shism04/neurona-app.git
    cd hola-neurona-app
    ```
2. **Launch the application:**
Run the following command in the root directory:

    ```Bash
    docker-compose up --build
    ```
3. **Access the app:**
Once the containers are running, open your browser and go to:
`http://localhost:8501`

---

### 🛠 Alternative: Local Development (Manual)

If you prefer to run it without Docker, follow these steps:

1. **Create and activate a virtual environment:**
    ```Bash
    python -m venv venv
    ```
    On Windows: venv\Scripts\activate | On Unix: source venv/bin/activate`
    
2. **Install dependencies:**
    ```Bash
    pip install -r requirements.txt
    ```
3. **Run the Streamlit app:**
    ```Bash
    streamlit run app.py
    ```

> Note: Ensure you have the necessary assets (like neurona.png) in the root directory as specified in the Dockerfile.

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