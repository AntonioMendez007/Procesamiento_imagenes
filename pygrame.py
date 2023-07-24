import pygame
import cv2
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Configuración de Pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))

def update_cursor_position(x, y):
    # Actualizar la posición del cursor en la ventana de Pygame
    pygame.mouse.set_pos(x, y)

def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 24)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y)) 

def start():
    print("Paso 1")

def menu():
    """ El menú donde se generarán los dos botones y por ende hacer clic en ellos """
    b1 = button(screen, (400, 300), "Salir")
    b2 = button(screen, (500, 300), "Comenzar")

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    color_mouse_pointer = (255, 0, 200)

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5) as hands:

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        video_surface = pygame.surface.Surface((width, height)).convert()

        # Crea una nueva superficie sin canal alfa
        video_surface_no_alpha = pygame.surface.Surface(video_surface.get_size())
        while True:
            ret, frame = cap.read()
            if ret == False:
                break

            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(frame_rgb)

            video_surface = pygame.surfarray.make_surface(frame_rgb)  # Convierte el array en una superficie de Pygame
            screen.blit(video_surface, (0, 0))

            if results.multi_hand_landmarks is not None:
                for hand_landmarks in results.multi_hand_landmarks:
                    x = int(hand_landmarks.landmark[9].x * width)
                    y = int(hand_landmarks.landmark[9].y * height)
                    cv2.circle(frame, (x, y), 10, color_mouse_pointer, 3)
                    cv2.circle(frame, (x, y), 5, color_mouse_pointer, -1)
                    update_cursor_position(x, y)  # Actualizar posición del cursor

                    if b1.collidepoint(pygame.mouse.get_pos()) or b2.collidepoint(pygame.mouse.get_pos()):
                        if start_time == 0:
                            start_time = pygame.time.get_ticks()
                        elif pygame.time.get_ticks() - start_time >= 1000:
                            start()
                            start_time = 0                         
                    else:
                        start_time = 0

            #pygame.surfarray.blit_array(video_surface_no_alpha, frame_rgb)
            #screen.blit(video_surface_no_alpha, (0, 0))

            cv2.imshow('Cursor', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        start()

            pygame.display.update()

    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()

menu()
