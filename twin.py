class DigitalTwin:
    def __init__(self):
        self.state = {
            "speed": 0,
            "fuel": 100,
            "engine_temp": 80,
            "oxygen_level": 100,
            "traffic_delay": 0,
            "mission": "Traslado urgente",
            "vehicle_status": "OPERATIVO",
            "lat": 40.4168,
            "lon": -3.7038,
            "emergency_code": 1,
            "vibration": 1,
            "oil_pressure": 60,
            "battery": 100,
            "distance_hospital": 5.0,
            "eta": 10,
            "stress_driver": 20,
            "patient_status": 100
        }

    def update(self, telemetry: dict):
        self.state.update(telemetry)
        # Estado global
        if self.risk_level() > 0.7:
            self.state["vehicle_status"] = "EN RIESGO"
        else:
            self.state["vehicle_status"] = "OPERATIVO"

    def risk_level(self) -> float:
        risk = 0.0
        if self.state["fuel"] < 20: risk += 0.2
        if self.state["engine_temp"] > 110: risk += 0.3
        if self.state["vibration"] > 7: risk += 0.2
        if self.state["oil_pressure"] < 25: risk += 0.2
        if self.state["patient_status"] < 70: risk += 0.3
        return min(risk, 1.0)
