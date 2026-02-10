# decision.py

def recommend(state, risk):
    actions = []

    if risk > 0.7:
        actions.append(" Solicitar unidad de refuerzo inmediata")
        actions.append(" Evaluar cambio de hospital")

    if state["traffic_delay"] > 5:
        actions.append(" Activar ruta alternativa")

    if state["fuel"] < 20:
        actions.append(" Planificar repostaje tras misión")

    if not actions:
        actions.append(" Operación dentro de parámetros normales")

    return actions
