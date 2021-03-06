from cv2 import cv2
from random import randrange

# cargar data pre-entrenada
data_rostro_entrenada = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

######FOTO CAPTURA########
# Escoger una imagen para detectar rostros
img = cv2.imread('img01.jpg')

# Convertir imagen a escala de grises
bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detectar rostros
coordenadas_rostro = data_rostro_entrenada.detectMultiScale(bw_img)
print(coordenadas_rostro)

# Dibujar rectangulos alrededor de los rostros
for(x, y, w, h) in coordenadas_rostro:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
    # cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 3)

# Mostrar imagen
cv2.imshow('Strange Code Detector Rostros', img)
cv2.waitKey()



# #####VIDEO CAPTURA#######
# # Capturar un video en tiempo real
# webcam  = cv2.VideoCapture(0)

# # Interactuar por tiempo indefinido con la camara
# while True:
#     ## Leer los frames
#     lectura_frame_exitosa, frame = webcam.read()

#     ## Convertir a escala de grises
#     bw_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     ## Detectar los rostros
#     coordenadas_rostro = data_rostro_entrenada.detectMultiScale(bw_img)

#     ## Dibujar Rectangulos alrededor de los rostros
#     for(x,y,w,h) in coordenadas_rostro:
#         cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

#     cv2.imshow('strange code Detector Rostro', frame)
#     key = cv2.waitKey(1)
#     print(key)
#     ## pare si presionamos la tecla q
#     if key==81 or key==113:
#         break

# webcam.release()

print("código completado")