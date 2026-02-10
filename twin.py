# twin.py

class DigitalTwin:
    def __init__(self):
        self.state = {
            "speed": 0,
            "fuel": 100,
            "engine_temp": 80,
            "oxygen_level": 100,
            "traffic_delay": 0,
            "mission": "Traslado urgente",
            "vehicle_status": "OPERATIVO"
        }

    def update(self, telemetry: dict):
        self.state.update(telemetry)

        # Estado global del vehículo
        if self.risk_level() > 0.7:
            self.state["vehicle_status"] = "EN RIESGO"
        else:
            self.state["vehicle_status"] = "OPERATIVO"

    def risk_level(self) -> float:
        risk = 0.0
        if self.state["fuel"] < 20:
            risk += 0.3
        if self.state["engine_temp"] > 110:
            risk += 0.4
        if self.state["oxygen_level"] < 70:
            risk += 0.5
        return min(risk, 1.0)
