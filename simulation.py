def simulate_future(state, minutes=10):
    future = state.copy()
    future["fuel"] = max(future["fuel"] - minutes*1.2, 0)
    future["engine_temp"] += minutes*0.8
    future["patient_status"] = max(future["patient_status"]-minutes*1.5,0)
    future["eta"] = max(future["eta"] - minutes*0.8,0)
    if future["fuel"]<10 or future["engine_temp"]>120:
        future["vehicle_status"] = "NO OPERATIVO"
    else:
        future["vehicle_status"] = "OPERATIVO"
    return future
