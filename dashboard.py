import streamlit as st
from simulator import generate_telemetry
from twin import DigitalTwin
from anomaly import detect_anomalies
from simulation import simulate_future
from decision import recommend

twin = DigitalTwin()

st.title("Gemelo Digital – Ambulancia SVA")


if st.button("🚨 Simular incidente crítico"):
    future_crisis = simulate_future(twin.state, minutes=20)
    st.subheader("Escenario crítico simulado (20 min)")
    st.json(future_crisis)


telemetry = generate_telemetry()
twin.update(telemetry)

risk = twin.risk_level()
anomalies = detect_anomalies(twin.state)
future = simulate_future(twin.state)
actions = recommend(twin.state, risk)

st.markdown("### Estado operativo del Gemelo Digital")

st.metric(
    "Estado del vehículo",
    twin.state["vehicle_status"]
)

st.progress(risk)

st.subheader("Estado actual")
st.json(twin.state)

st.metric("Nivel de riesgo", f"{risk*100:.0f}%")
st.caption(f"Nivel de riesgo operativo: {int(risk * 100)} %")


st.subheader("Anomalías detectadas")
st.write(anomalies or "Ninguna")

st.subheader("Simulación a 10 minutos")
st.json(future)

st.subheader("Recomendaciones")
st.write(actions or "Operación normal")

