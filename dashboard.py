# dashboard.py

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

from twin import DigitalTwin
from simulator import generate_telemetry
from anomaly import detect_anomalies
from simulation import simulate_future
from decision import recommend
from ai_model import RiskPredictor


# Configuración visual
st.set_page_config(layout="wide", page_title="Centro de Control Ambulancia")
st.markdown("""<style>body{background-color:#0E1117;color:white;}</style>""",unsafe_allow_html=True)


# Cargar modelo IA
@st.cache_resource
def load_model():
    return RiskPredictor()

predictor = load_model()


# Estado del gemelo y historial
if "twin" not in st.session_state:
    st.session_state.twin = DigitalTwin()
if "history" not in st.session_state:
    st.session_state.history = []

twin = st.session_state.twin


# Controles de simulación
st.title(" Centro de Control – Gemelo Digital Ambulancia")
colA, colB, colC = st.columns(3)

if colA.button(" Avanzar 1 paso"):
    telemetry = generate_telemetry(twin.state)
    twin.update(telemetry)
    st.session_state.history.append(twin.state.copy())

if colB.button(" Avanzar 10 pasos"):
    for _ in range(10):
        telemetry = generate_telemetry(twin.state)
        twin.update(telemetry)
        st.session_state.history.append(twin.state.copy())

if colC.button(" Reset simulación"):
    st.session_state.twin = DigitalTwin()
    st.session_state.history = []

# Limitar historial
if len(st.session_state.history) > 100:
    st.session_state.history = st.session_state.history[-100:]


# Cálculo de riesgos y IA
risk = twin.risk_level()
mech_risk, patient_risk = predictor.predict(twin.state)
anomalies = detect_anomalies(twin.state)
actions = recommend(twin.state, risk)


# Panel de métricas principales
c1,c2,c3,c4 = st.columns(4)
c1.metric(" Código", twin.state["emergency_code"])
c2.metric(" Combustible", f"{twin.state['fuel']:.1f}%")
c3.metric(" Temp Motor", f"{twin.state['engine_temp']:.1f}°C")
c4.metric(" Oxígeno", f"{twin.state['oxygen_level']:.1f}%")
st.progress(risk)


# IA predictiva
st.subheader(" Predicción IA")
st.metric("Prob. fallo mecánico", f"{mech_risk*100:.1f}%")
st.metric("Prob. riesgo paciente", f"{patient_risk*100:.1f}%")


# Mapa GPS con icono blanco
st.subheader(" Seguimiento GPS")

m = folium.Map(location=[twin.state["lat"], twin.state["lon"]],
               zoom_start=15, tiles="cartodb dark_matter")


# Icono blanco de ambulancia
icon = folium.CustomIcon(
    icon_image="https://cdn-icons-png.flaticon.com/512/2841/2841973.png",
    icon_size=(35, 35)
)

tooltip_text = f"Ambulancia – Código: {twin.state['emergency_code']}"
folium.Marker([twin.state["lat"], twin.state["lon"]],
              tooltip=tooltip_text,
              icon=icon).add_to(m)


# Traza de trayectoria
if len(st.session_state.history) > 1:
    points = [(h["lat"], h["lon"]) for h in st.session_state.history]
    folium.PolyLine(points, color="cyan", weight=3).add_to(m)

st_folium(m, width=900, height=500)


# Gráficas de evolución
if len(st.session_state.history) > 1:
    st.subheader(" Evolución de riesgo y estado del paciente")
    df = pd.DataFrame(st.session_state.history)
    st.line_chart(df[["patient_status"]])
    st.line_chart(df[["fuel","engine_temp"]])


# Panel de códigos de emergencia
st.subheader("ℹ Significado del código de emergencia")
st.markdown("""
- **0 – Normal**: Transporte rutinario sin urgencia.
- **1 – Urgencia leve**: Caso urgente pero estable.
- **2 – Urgencia grave**: Caso crítico, requiere atención inmediata.
- **3 – Código crítico**: Vida en riesgo, máxima prioridad.
""")


# Anomalías
st.subheader(" Anomalías")
if anomalies:
    for a in anomalies:
        st.error(f"{a['severity']} – {a['problem']}")
        st.info(f"Solución: {a['solution']}")
else:
    st.success("Sin anomalías")


# Simulación futura
st.subheader(" Simulación futura")
minutes = st.slider("Minutos a simular",5,60,20)
if st.button("Simular escenario"):
    future = simulate_future(twin.state, minutes)
    st.json(future)


# Recomendaciones
st.subheader(" Recomendaciones estratégicas")
for act in actions:
    st.write("•", act)
