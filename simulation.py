# simulation.py

def simulate_future(state, minutes=10):
    future = state.copy()

    # Consumo y desgaste
    future["fuel"] = max(future["fuel"] - minutes * 1.8, 0)
    future["engine_temp"] += minutes * 0.9

    # Riesgo médico
    if future["oxygen_level"] < 70:
        future["mission"] = "RIESGO VITAL"

    # Estado final
    if future["fuel"] < 10 or future["engine_temp"] > 120:
        future["vehicle_status"] = "NO OPERATIVO"
    else:
        future["vehicle_status"] = "EN RIESGO"

    return future
