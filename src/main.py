print("Teste")
import time
from machine import Pin

led = Pin(2, Pin.OUT)
print("Iniciando hardware...")

for i in range(3):
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)

print("Fim do teste.")