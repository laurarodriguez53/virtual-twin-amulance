import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class RiskPredictor:
    """Predicción de fallo operativo y riesgo paciente"""

    def __init__(self):
        self.model_mech = RandomForestClassifier()
        self.model_patient = RandomForestClassifier()
        self._train_models()

    def _generate_data(self, n=4000):
        X = []
        y_mech = []
        y_patient = []

        for _ in range(n):
            fuel = np.random.uniform(0, 100)
            engine_temp = np.random.uniform(70, 130)
            vibration = np.random.uniform(0, 10)
            oil_pressure = np.random.uniform(20, 80)
            speed = np.random.uniform(0, 120)
            emergency_code = np.random.choice([0,1,2,3])
            patient_status = np.random.uniform(0,100)

            X.append([fuel, engine_temp, vibration, oil_pressure, speed, emergency_code, patient_status])

            # Mecánico
            mech_risk = 0
            if fuel<15: mech_risk+=1
            if engine_temp>115: mech_risk+=1
            if vibration>7: mech_risk+=1
            if oil_pressure<25: mech_risk+=1
            y_mech.append(1 if mech_risk>=2 else 0)

            # Paciente
            pat_risk = 0
            if patient_status<60: pat_risk+=1
            if speed>100: pat_risk+=1
            if emergency_code>=2: pat_risk+=1
            y_patient.append(1 if pat_risk>=2 else 0)

        return np.array(X), np.array(y_mech), np.array(y_patient)

    def _train_models(self):
        X, y_mech, y_patient = self._generate_data()
        X_train, X_test, y_mech_train, y_mech_test = train_test_split(X, y_mech, test_size=0.2)
        _, _, y_patient_train, y_patient_test = train_test_split(X, y_patient, test_size=0.2)
        self.model_mech.fit(X_train, y_mech_train)
        self.model_patient.fit(X_train, y_patient_train)

    def predict(self, state):
        data = np.array([[state["fuel"], state["engine_temp"], state["vibration"],
                          state["oil_pressure"], state["speed"], state["emergency_code"], state["patient_status"]]])
        mech_prob = self.model_mech.predict_proba(data)[0][1]
        patient_prob = self.model_patient.predict_proba(data)[0][1]
        return mech_prob, patient_prob
