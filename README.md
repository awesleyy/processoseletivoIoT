# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## 🏁 Passo 0 – Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo — eles fazem parte do processo de aprendizagem esperado.

---

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

> 📌 O GitHub será utilizado para:
> - Envio do seu projeto  
> - Versionamento do código  
> - Correção e validação automática via GitHub Actions  

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows
Baixe e instale o **Git Bash**:  
https://git-scm.com/downloads

### Linux / macOS
Verifique se o Git já está instalado:

```bash
git --version
```
> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## ⚙ Passo 1 – Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1️⃣ Fork do Repositório
No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />


Uma cópia do repositório será criada no seu perfil do GitHub

> 🔎 O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2️⃣ Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### 🔹 Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### 🔹 Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> ➡️ Todas as dependências serão instaladas automaticamente.

## 🔐 Passo 2 – Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: https://wokwi.com/dashboard/ci
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

>⚠️ Importante
- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## 🔒 Passo 3 – Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> ✔️ As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## 🧠 Passo 4 – Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### 📁 Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### 🛠 Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### 1️⃣ src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### 2️⃣ diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### 3️⃣ wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### 4️⃣ Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```
### ⚙ Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### 📌 Caso algo falhe:

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## 📊 Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## 📎 Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions  
2. Confirme que todos os arquivos obrigatórios estão presentes  
3. Copie o link do **seu repositório no GitHub**

📤 Envie o link conforme as orientações do processo seletivo na plataforma **Moodle**.

---

## 📝 Relatório do Candidato

Com certeza, André. Aqui está o conteúdo formatado exatamente como deve ficar dentro do seu arquivo README.md.

Basta copiar o bloco de código abaixo e substituir todo o conteúdo do seu arquivo atual por este:

Markdown
# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

### 👤 Identificação do Candidato
- **Nome completo:** [Seu Nome Completo Aqui]
- **GitHub:** https://github.com/awesleyy

---

## 1️⃣ Visão Geral da Solução
O projeto consiste em um **Sistema de Monitoramento de Ciclos Operacionais** utilizando a placa ESP32. O objetivo é simular um processo de varredura ou verificação de sensores onde o sistema fornece um feedback visual através de um LED externo e envia logs detalhados de status via comunicação serial para monitoramento remoto em tempo real.

---

## 2️⃣ Arquitetura do Sistema Embarcado
A arquitetura do firmware foi desenvolvida em MicroPython, seguindo um modelo de **Loop de Controle Infinito** estruturado da seguinte forma:
- **Inicialização:** Configuração do pino GPIO 2 como saída digital e inicialização da interface serial.
- **Processamento:** O sistema executa ciclos incrementais, simulando a coleta de dados.
- **Feedback Visual:** A cada interação, o estado do LED é alternado. Utilizou-se tempos de espera de `0.5s` (aceso) e `1.5s` (apagado) para diferenciar visualmente a fase de processamento da fase de espera.
- **Comunicação:** Formatação e envio de telemetria via Serial, indicando o número do ciclo e a saúde do sistema.

---

## 3️⃣ Componentes Utilizados na Simulação
Conforme definido no arquivo `diagram.json`, os componentes são:
- **Placa:** ESP32 DevKit V4 (Microcontrolador principal).
- **LED Vermelho:** Atuador visual conectado à porta **D2**.
- **Serial Monitor:** Interface de saída para logs e depuração do sistema.

---

## 4️⃣ Decisões Técnicas Relevantes
- **Abstração de Hardware:** Uso de constantes para definição de pinos, facilitando a portabilidade do código para outros hardwares.
- **Encapsulamento:** A lógica principal foi isolada na função `executar_monitoramento()`, mantendo o ponto de entrada do script (`if __name__ == "__main__":`) organizado.
- **Resiliência:** Implementação de bloco `try/except` para capturar interrupções de teclado (KeyboardInterrupt), garantindo um desligamento limpo da simulação sem erros residuais nos logs.
- **Frequência de Operação:** Definição de delay total de 2 segundos por ciclo para garantir que o Serial Monitor seja legível e não sobrecarregue o processamento da simulação.

---

## 5️⃣ Resultados Obtidos
- **Funcionalidade:** O sistema executa o loop de monitoramento sem falhas, conforme validado pelas GitHub Actions.
- **Interatividade:** É possível observar o LED piscando no simulador Wokwi enquanto o terminal exibe o incremento dos ciclos.
- **Estabilidade:** O projeto atende a todos os requisitos obrigatórios de organização de pastas (`src/main.py`), configuração (`wokwi.toml`) e hardware (`diagram.json`).

---

## 6️⃣ Comentários Adicionais (Opcional)
- **Desafio:** A integração do Wokwi CLI com as Actions do GitHub foi um excelente aprendizado sobre como testar hardware virtualizado de forma automatizada.
- **Melhorias:** Em uma versão 2.0, eu adicionaria um botão físico no `diagram.json` para permitir que o usuário resetasse a contagem de ciclos manualmente via interrupção externa (IRQ).

---
*Relatório gerado para fins de avaliação técnica no processo seletivo Intensivo Maker.*

---

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
Mostre sua capacidade de pensar como um engenheiro de sistemas embarcados.
****
 
