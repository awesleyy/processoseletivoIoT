print("Teste")
import machine
import time

# Configuração do LED no pino 2
led = machine.Pin(2, machine.Pin.OUT)

print("--- SISTEMA INICIADO ---")

for i in range(1, 6):
    led.value(1) # Liga o LED
    print(f"CICLO: {i} | LED: LIGADO")
    time.sleep(0.5)
    
    led.value(0) # Desliga o LED
    print(f"CICLO: {i} | LED: DESLIGADO")
    time.sleep(0.5)

print("--- TESTE CONCLUIDO COM SUCESSO ---")