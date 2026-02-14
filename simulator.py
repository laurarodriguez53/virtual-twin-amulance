import random

def generate_telemetry(prev):
    # Movimiento GPS pequeño
    lat = prev["lat"] + random.uniform(-0.0005, 0.0005)
    lon = prev["lon"] + random.uniform(-0.0005, 0.0005)
    return {
        "speed": random.uniform(30, 120),
        "fuel": max(prev["fuel"]-random.uniform(0.1,1.0),0),
        "engine_temp": prev["engine_temp"] + random.uniform(-1,2),
        "oxygen_level": max(prev["oxygen_level"]-random.uniform(0,2),50),
        "traffic_delay": random.choice([0,2,5,8]),
        "lat": lat,
        "lon": lon,
        "emergency_code": random.choice([0,1,2,3]),
        "vibration": random.uniform(0,10),
        "oil_pressure": random.uniform(20,80),
        "battery": max(prev["battery"]-random.uniform(0,0.5),50),
        "distance_hospital": max(prev["distance_hospital"]-random.uniform(0.05,0.5),0),
        "eta": max(prev["eta"]-1,0),
        "stress_driver": min(prev["stress_driver"]+random.uniform(0,5),100),
        "patient_status": max(prev["patient_status"]-random.uniform(0,3),50)
    }
