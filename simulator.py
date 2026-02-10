import random
import time

def generate_telemetry():
    return{
        "speed": random.randint(30,120),
        "fuel": random.uniform(10,100),
        "engine_temp": random.uniform(70, 120),
        "oxygen_level": random.uniform(60,100),
        "traffic_delay": random.choice([0,2,5,8])
        
    }
    
if __name__ == "__main__":
    while True:
        print(generate_telemetry())
        time.sleep(1)
                

    
