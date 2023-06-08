# Importa as bibliotecas necessárias.
import cv2
import numpy as np

# Carrega os dois vídeos.
cap_webcam = cv2.VideoCapture('data/webcam.mp4')
cap_praia = cv2.VideoCapture('data/praia.mp4')

# Obtém as informações dos vídeos de entrada.
frame_width = int(cap_webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap_webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap_webcam.get(cv2.CAP_PROP_FPS)

# Define o codec e cria os objetos VideoWriter para salvar os vídeos.
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use o codec 'mp4v'
out_person = cv2.VideoWriter('output_person.mp4', fourcc, fps, (frame_width, frame_height))  # Salva o vídeo da pessoa isolada
out_final = cv2.VideoWriter('output_final.mp4', fourcc, fps, (frame_width, frame_height))  # Salva o vídeo da composição final

# Define as dimensões da janela menor
window_width = 1280
window_height = 720

# Loop principal.
while True:
    # Lê um quadro de cada vídeo.
    ret_webcam, frame_webcam = cap_webcam.read()
    ret_praia, frame_praia = cap_praia.read()

    # Verifica se os vídeos terminaram.
    # Se sim, termina o loop.
    if not ret_webcam or not ret_praia:
        break

    # Define os limites da cor verde em RGB.
    # Esses limites serão usados para criar a máscara.
    lower_green = np.array([0, 100, 0], dtype=np.uint8)
    upper_green = np.array([100, 255, 100], dtype=np.uint8)

    # Cria uma máscara com os pixels que estão dentro da faixa de cor verde.
    mask = cv2.inRange(frame_webcam, lower_green, upper_green)

    # Usa a máscara para extrair os pixels da praia que correspondem ao fundo verde da webcam.
    praia_background = cv2.bitwise_and(frame_praia, frame_praia, mask=mask)

    # Inverte a máscara para obter os pixels que não estão na faixa de cor verde.
    mask_inv = np.invert(mask)

    # Usa a máscara invertida para extrair os pixels da webcam que não são verdes.
    webcam_foreground = cv2.bitwise_and(frame_webcam, frame_webcam, mask=mask_inv)

    result = cv2.addWeighted(praia_background, 1, webcam_foreground, 1, 0)

     # Escreve os quadros nos arquivos de vídeo correspondentes.
    out_person.write(webcam_foreground)
    out_final.write(result)

    # Redimensiona o resultado para as dimensões desejadas
    result_resized = cv2.resize(result, (window_width, window_height))

    cv2.imshow("Resultado", result_resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_webcam.release()
cap_praia.release()
out_person.release()
out_final.release()
cv2.destroyAllWindows()