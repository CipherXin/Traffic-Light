import random
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d} : {:02d}'.format(mins, secs)
        print(timer, end="\r", flush=True)
        time.sleep(1)
        t -= 1

lights = ['RED', 'YELLOW', 'GREEN']

current_light = random.choice(lights)
print(current_light)

if current_light == lights[0]:
    countdown(10)
    print(lights[1])
    countdown(5)
    print(lights[2])

elif current_light == lights[1]:
    countdown(5)
    print(lights[2])

elif current_light == lights[2]:
    countdown(10)
    print(lights[1])
    countdown(5)
    print(lights[0])




