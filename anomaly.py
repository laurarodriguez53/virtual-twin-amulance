# anomaly.py

from events import event_manager
def detect_anomalies(state):
    anomalies = []
    if state["engine_temp"]>115:
        anomaly = {"severity":"CRÍTICO","problem":"Motor sobrecalentado","solution":"Reducir velocidad y activar enfriamiento"}
        anomalies.append(anomaly)
        event_manager.publish("anomaly_detected", anomaly)
    if state["oxygen_level"]<65:
        anomaly = {"severity":"CRÍTICO","problem":"Oxígeno bajo","solution":"Revisar sistema oxígeno"}
        anomalies.append(anomaly)
        event_manager.publish("anomaly_detected", anomaly)
    if state["fuel"]<15:
        anomaly = {"severity":"ALTO","problem":"Combustible en reserva","solution":"Planificar repostaje"}
        anomalies.append(anomaly)
        event_manager.publish("anomaly_detected", anomaly)
    if state["vibration"]>7:
        anomaly = {"severity":"ALTO","problem":"Vibración peligrosa","solution":"Revisar suspensión/motor"}
        anomalies.append(anomaly)
        event_manager.publish("anomaly_detected", anomaly)
    if state["patient_status"]<70:
        anomaly = {"severity":"CRÍTICO","problem":"Paciente en riesgo","solution":"Atención inmediata"}
        anomalies.append(anomaly)
        event_manager.publish("anomaly_detected", anomaly)
    return anomalies
