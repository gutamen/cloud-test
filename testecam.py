import cv2

# URI do stream RTSP da câmera
uri_stream = 'rtsp://admin:Gustavo2606@24.152.102.197:55555/videoMain'

# Abrindo o stream de vídeo com OpenCV
cap = cv2.VideoCapture(uri_stream)

if not cap.isOpened():
    print("Erro ao abrir o stream de vídeo.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Falha ao obter frame do stream.")
        break

    # Exibindo o frame de vídeo
    cv2.imshow('Video Stream', frame)

    # Pressione 'q' para sair da exibição
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()