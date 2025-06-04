import cv2
import numpy as np
import requests

def detectar_apagao(frame, threshold=40):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    media_luminosidade = np.mean(gray)
    return media_luminosidade < threshold, media_luminosidade

cap = cv2.VideoCapture('apagao_simulado.mp4')  # ou 0 para webcam
apagao_detectado = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    apagou, nivel = detectar_apagao(frame)

    print(f"Luminosidade: {nivel:.2f}")

    if apagou and not apagao_detectado:
        print("⚠️ Queda de energia detectada!")
        # Envia alerta para Node-RED
        try:
            requests.post("http://localhost:1880/alerta", json={"evento": "apagao"})
        except:
            print("Erro ao enviar alerta para Node-RED.")
        apagao_detectado = True

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
