# Alerta Inteligente para Queda de Energia

## 💡 Problema
Durante quedas de energia, pessoas e serviços essenciais podem ficar vulneráveis sem aviso prévio.

## 🎯 Solução
Um sistema que analisa vídeos e detecta quedas abruptas de luminosidade, simulando um apagão, e envia alertas via Node-RED.

## 🛠️ Tecnologias
- Python + OpenCV
- Node-RED
- Vídeo simulado
- HTTP Request

## ▶️ Funcionamento
1. Python lê um vídeo e detecta queda de luminosidade.
2. Ao detectar apagão, envia um alerta para Node-RED via HTTP.
3. Node-RED mostra o alerta (pode ser expandido para e-mail, som, etc).

## 🎥 Demonstração
[Link para o vídeo aqui]

## 👨‍💻 Execução
```bash
pip install opencv-python numpy requests
python detecta_apagao.py
