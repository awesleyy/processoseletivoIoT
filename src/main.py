import machine
import time

# Configuração do hardware
led = machine.Pin(2, machine.Pin.OUT)

print("--- Sistema Iniciado com Sucesso ---")

def loop():
    contagem = 0
    while True:
        contagem += 1
        led.value(1)
        print("LED ACESO | Ciclo:", contagem)
        time.sleep(1)
        
        led.value(0)
        print("LED APAGADO")
        time.sleep(1)

if __name__ == "__main__":
    try:
        loop()
    except Exception as e:
        print("Erro no sistema:", e)