import pybullet as p
import time

physicsClient = p.connect(p.GUI)

for x in range(0,1000):
    p.stepSimulation()
    time.sleep(0.01)

p.disconnect()