# anomaly.py

def detect_anomalies(state):
    anomalies = []

    if state["engine_temp"] > 115:
        anomalies.append(" Temperatura de motor peligrosa")

    if state["oxygen_level"] < 65:
        anomalies.append(" Nivel de oxígeno crítico")

    if state["fuel"] < 15:
        anomalies.append(" Combustible en reserva")

    if state["traffic_delay"] > 6:
        anomalies.append(" Retraso severo por tráfico")

    return anomalies