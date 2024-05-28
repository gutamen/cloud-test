import cv2

# URI do stream RTSP da câmera
uri_stream = 'rtsp://admin:Gustavo2606@24.152.102.197:25565/videoMain'
#uri_stream = 'rtsp://admin:Gustavo2606@192.168.1.101:25565/videoMain'

# Abrindo o stream de vídeo com OpenCV
cap = cv2.VideoCapture(uri_stream)

"""
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

"""
if not cap.isOpened():
    print("Erro ao abrir o stream de vídeo.")
    exit()

# Capturando um frame
ret, frame = cap.read()
if not ret:
    print("Falha ao obter frame do stream.")
else:
    cv2.imshow('Video Stream', frame)
    cv2.imwrite('captured_image.jpg', frame)
    # Pressione 'q' para sair da exibição
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()