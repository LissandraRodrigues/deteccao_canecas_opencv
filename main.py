# 12/04/2020
# Luiza Lissandra R. Rosa
# Contato: luizalissandrarosa@poli.ufrj.br
# Descrição: Programa que detecta o número de canecas existentes em um frame.

# Importação
import cv2

# Programa principal.
def main():

    video = cv2.VideoCapture(0)

    # Arquivo XML que contêm as características de canecas.
    # Para um melhor desempenho, seria necessário um cascade mais bem treinado.
    classifierMug = cv2.CascadeClassifier('cascade_mug.xml')

    colorText = (255, 255, 255)

    fontText = cv2.FONT_HERSHEY_COMPLEX_SMALL

    while True:

        connected, frame = video.read()

        frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # A partir do classificador, detecta se há canecas no frame.
        mugDetector = classifierMug.detectMultiScale(frameGray, scaleFactor=1.01, minNeighbors = 125)

        mugCounter = 0

        # Insere bounding box para cada caneca detectada.
        for (x, y, l, a) in mugDetector:

            cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 255, 0), 2)

            mugCounter += 1

        cv2.putText(frame, 'Canecas: ' + str(mugCounter), (10,30), fontText, 1, colorText, 2)

        cv2.imshow('Detector de canecas', frame)

        # O programa é fechado ao apertar a tecla 'x'.
        if cv2.waitKey(1) == ord('x'):

            break

    video.release()

    cv2.destroyAllWindows()

main()