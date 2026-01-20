import streamlit as st
from functools import reduce

def calcular_salida(pesos, entradas, sesgo=0):
    result_list = [(pesos[i] * entradas[i]) for i in range(len(entradas))]
    result_list.append(sesgo)
    return reduce(lambda element, result: result + element, result_list, 0)

st.image("./neurona.png", width=400)
st.title('Hola neurona!')

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    w0 = st.slider("Peso w0", 0.0, 4.0, key="w0_tab1")
    x0 = st.number_input("Entrada x0", key="x0_tab1")
    if st.button("Calcular la salida", key="button_tab1"):
        st.write(f"La salida de la neurona es {calcular_salida([w0], [x0])}")
with tab2:
    col1, col2= st.columns(2)
    with col1:
        w0 = st.slider("Peso w0", 0.0, 4.0, key="w0_tab2")
        x0 = st.number_input("Entrada x0", key="x0_tab2")
    with col2:
        w1 = st.slider("Peso w1", 0.0, 4.0, key="w1_tab2")
        x1 = st.number_input("Entrada x1", key="x1_tab2")
    if st.button("Calcular la salida", key="button_tab2"):
        st.write(f"La salida de la neurona es {calcular_salida([w0, w1], [x0, x1])}")
with tab3:
    col1, col2, col3 = st.columns(3)
    with col1:
        w0 = st.slider("Peso w0", 0.0, 4.0, key="w0_tab3")
        x0 = st.number_input("Entrada x0", key="x0_tab3")
    with col2:
        w1 = st.slider("Peso w1", 0.0, 4.0, key="w1_tab3")
        x1 = st.number_input("Entrada x1", key="x1_tab3")
    with col3:
        w2 = st.slider("Peso w2", 0.0, 4.0, key="w2_tab3")
        x2 = st.number_input("Entrada x2", key="x2_tab3")
    sesgo = st.number_input("Introduzca el valor del sesgo")
    if st.button("Calcular la salida", key="button_tab3"):
        st.write(f"La salida de la neurona es {calcular_salida([w0, w1, w2], [x0, x1, x2], sesgo)}")