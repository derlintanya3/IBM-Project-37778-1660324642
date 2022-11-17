import random
from time import sleep

while True:
    
    temp = random.randint(-100, 100)
    hum = random.randint(0, 101)

    if(temp > 40 or temp < 10 or hum < 10 or hum > 60):
        print("Abnormal Condtions Detected.")

    else:
        print("All Systems Normal")

    sleep(2)
