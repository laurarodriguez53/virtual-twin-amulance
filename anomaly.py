def detect_anomalies(state):
    anomalies = []
    if state["engine_temp"]>115:
        anomalies.append({"severity":"CRÍTICO","problem":"Motor sobrecalentado","solution":"Reducir velocidad y activar enfriamiento"})
    if state["oxygen_level"]<65:
        anomalies.append({"severity":"CRÍTICO","problem":"Oxígeno bajo","solution":"Revisar sistema oxígeno"})
    if state["fuel"]<15:
        anomalies.append({"severity":"ALTO","problem":"Combustible en reserva","solution":"Planificar repostaje"})
    if state["vibration"]>7:
        anomalies.append({"severity":"ALTO","problem":"Vibración peligrosa","solution":"Revisar suspensión/motor"})
    if state["patient_status"]<70:
        anomalies.append({"severity":"CRÍTICO","problem":"Paciente en riesgo","solution":"Atención inmediata"})
    return anomalies
