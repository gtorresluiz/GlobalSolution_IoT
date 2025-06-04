# 💡 Sistema de Alerta para Falta de Energia com Python, MediaPipe e Node-RED

## 🧠 Descrição do problema

Apagões podem causar grandes transtornos em locais como hospitais, centros de comando e residências. A falta de iluminação pode dificultar a locomoção, gerar riscos de segurança e impedir operações críticas.

Diante disso, propomos uma solução de **alerta automatizado de queda de energia**, utilizando apenas uma **webcam** e bibliotecas como **Python + OpenCV**, simulando o sensor LDR via vídeo, e **Node-RED** para notificações.

---

## 🚀 Visão geral da solução

Nosso sistema:
1. Usa a câmera do computador para monitorar a luminosidade ambiente.
2. Detecta quedas bruscas de luz simulando um **apagão**.
3. Ao detectar a queda de luz, dispara um **alerta** para o **Node-RED**, que pode ser adaptado para acionar e-mails, sons ou luzes de emergência.

---

## 🛠 Tecnologias utilizadas

- Python 3.10+
- OpenCV
- NumPy
- Node-RED
- (Opcional) MediaPipe para futuras evoluções

---

## 🧪 Simulação com vídeo/câmera

- O código Python simula o sensor LDR analisando o brilho da imagem captada pela webcam.
- Se a **luminosidade média** da imagem cair abaixo de um limite (`threshold`), é considerado um **apagão**.

---

## 🎯 Como funciona

### 1. 📷 Código Python de detecção

```bash
pip install opencv-python numpy requests
