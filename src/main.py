import machine
import time

# Configuração do hardware
# O pino 2 é o padrão para o LED que conectamos no diagram.json
LED_PIN = 2
led = machine.Pin(LED_PIN, machine.Pin.OUT)

def executar_monitoramento():
    print("--- Sistema de Monitoramento Embarcado ---")
    print("Iniciando leitura de dados simulados...")
    
    contagem = 0
    
    while True:
        contagem += 1
        
        # Lógica de piscar o LED (Feedback visual)
        led.value(1)
        print(f"Status: OK | Ciclo: {contagem} | LED: Aceso")
        time.sleep(0.5)
        
        led.value(0)
        print(f"Status: OK | Ciclo: {contagem} | LED: Apagado")
        time.sleep(1.5)

if __name__ == "__main__":
    try:
        executar_monitoramento()
    except KeyboardInterrupt:
        print("\nSistema encerrado pelo usuário.")