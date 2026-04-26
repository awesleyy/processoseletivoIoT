import machine
import time

# Configuração do LED no pino 2
led = machine.Pin(2, machine.Pin.OUT)

print("--- Sistema de Monitoramento Iniciado ---")

# Rodamos exatamente 5 vezes para que o teste termine com sucesso
for i in range(1, 6):
    led.value(1)
    print(f"LED ACESO | Ciclo: {i}")
    time.sleep(0.5)
    
    led.value(0)
    print(f"LED APAGADO | Ciclo: {i}")
    time.sleep(0.5)

print("--- Projeto validado com sucesso! ---")