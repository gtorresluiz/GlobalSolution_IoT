import cv2
import numpy as np
import requests

def detectar_apagao(frame, threshold=40):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    media_luz = np.mean(gray)
    return media_luz < threshold, media_luz

cap = cv2.VideoCapture(0)  # ou 'video.mp4' se tiver vídeo salvo
apagao_detectado = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    apagao, nivel = detectar_apagao(frame)

    print(f"Luminosidade: {nivel:.2f}")

    if apagao and not apagao_detectado:
        print("⚠️ Queda de energia detectada!")
        try:
            requests.post("http://127.0.0.1:1880/alerta", json={"evento": "apagao"})
            print("✅ Alerta enviado para Node-RED")
        except Exception as e:
            print(f"❌ Falha ao enviar alerta: {e}")
        apagao_detectado = True

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
