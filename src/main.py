import machine
import time

# Configuração do hardware
# O pino 2 é o padrão para o LED na placa ESP32 do Wokwi
led = machine.Pin(2, machine.Pin.OUT)

print("--- Sistema Iniciado com Sucesso ---")

def executar_teste():
    for contagem in range(1, 6):
        led.value(1)
        print(f"LED ACESO | Ciclo: {contagem}")
        time.sleep(0.5)
        
        led.value(0)
        print(f"LED APAGADO | Ciclo: {contagem}")
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        executar_teste()
        print("--- Monitoramento Concluído com Sucesso ---")
    except Exception as e:
        print("Erro no sistema:", e)