# 💡 Sistema de Alerta para Falta de Energia 

## Link do Vídeo Explicativo
### https://youtu.be/3rdsJmfeDDA

## Integrantes
### Eduardo Fedeli Souza RM:550132
### Otávio Vitoriano da Silva RM:552012
### Gabriel Torres Luiz RM: 98600

## 🧠 Descrição do problema

Apagões podem causar grandes transtornos em locais como hospitais, centros de comando e residências. A falta de iluminação pode dificultar a locomoção, gerar riscos de segurança e impedir operações críticas.

Diante disso, propomos uma solução de **alerta automatizado de queda de energia**, utilizando apenas uma **webcam** e bibliotecas como **Python + OpenCV**, simulando o sensor LDR via vídeo, e **Node-RED** para notificações.

---

## 🚀 Visão geral da solução

Nosso sistema:
1. Usa a câmera do celular para monitorar a luminosidade ambiente.
2. Detecta quedas bruscas de luz simulando um **apagão**.
3. Ao detectar a queda de luz, dispara um **alerta** para o **Node-RED**, que aciona o disparo de e-mails, gera um dashboard informativo e pode ser adaptado para implementar sons, luzes de emergência ou inicar o sistema de reajuste.

---

## 🛠 Tecnologias utilizadas

- Python 3.10+
- OpenCV
- NumPy
- Node-RED
- MediaPipe

---

## 🧪 Simulação com vídeo/câmera

- O código Python realiza o diagnóstico de um vídeo gravado pelo celular
- Se a **luminosidade média** da imagem cair abaixo de um limite (`threshold`), é considerado um **apagão**.

---

## 🎯 Como funciona

### 1. 📷 Código Python de detecção

```bash
pip install opencv-python numpy requests


