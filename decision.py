def recommend(state, risk):
    actions=[]
    if risk>0.7:
        actions.append("Solicitar refuerzo mecánico inmediato")
    if state["traffic_delay"]>5:
        actions.append("Activar ruta alternativa")
    if state["fuel"]<20:
        actions.append("Planificar repostaje")
    if state["patient_status"]<70:
        actions.append("Atención médica urgente al paciente")
    if not actions:
        actions.append("Operación normal")
    return actions
