import cv2
import numpy as np
import mediapipe as mp
import pygame
import pygame_menu # libreria para hacer menus en la interfaz

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Configuración de Pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))

def update_cursor_position(x, y):
    # Actualizar la posición del cursor en la ventana de Pygame
    pygame.mouse.set_pos(x, y)

def start():
    # Inicializar video en tiempo real
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    color_mouse_pointer = (255, 0, 200)

    start_time = 0
    button_h = False # Se define como falsa al momento de verificar que si esa variable relacionada con el boton no tiene nada, se hagan las respectivas acciones

    # Configurar la ventana de pantalla ancho x alto
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Jijijia")

    # Definir el tema personalizado
    custom_theme = pygame_menu.themes.Theme(
        background_color=(189, 155, 19),  # Color de fondo personalizado
        title_font_size=30,
        title_font_color=(255, 255, 255),
        widget_font_size=20,
        widget_font_color=(10, 10, 10),
        widget_font=pygame_menu.font.FONT_OPEN_SANS_BOLD
    )

    # Crear el menú con el tema personalizado
    main_menu = pygame_menu.Menu("UX20II294", 800, 600, theme=custom_theme)

    def button3():
        # Es el que me va aregresar al menú principal
        show_menu()

    main_menu.add.button("Regresar", button3, button_id="salir_f")  # Agregar un ID al botón

    # Comienza la detección de la mano
    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.7) as hands:
        while True:
            ret, frame = cap.read()
            if ret == False:
                break

            height, width, _ = frame.shape
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks is not None:
                for hand_landmarks in results.multi_hand_landmarks:
                    x = int(hand_landmarks.landmark[9].x * width)
                    y = int(hand_landmarks.landmark[9].y * height)
                    cv2.circle(frame, (x, y), 10, color_mouse_pointer, 3)
                    cv2.circle(frame, (x, y), 5, color_mouse_pointer, -1)
                    update_cursor_position(x, y)  # Actualizar posición del cursor

                    mouse_pos = pygame.mouse.get_pos()
                    button3_widget = main_menu.get_widget("salir_f")  # Obtener el botón por su ID
                    button3_rect = button3_widget.get_rect() if button3_widget else None  # Obtener el rectángulo del botón
                    # Lo que se hace en estos if's, es que si el cursor esta encima del botón por 1 segundo, este se active y realice el evento asignado a él
                    if button3_rect and button3_rect.collidepoint(mouse_pos):
                        if not button_h:
                            start_time = pygame.time.get_ticks()
                            button_h = True
                        elif pygame.time.get_ticks() - start_time >= 1000:
                            button3()
                    else:
                        button_h = False

            # Girar el frame(180 grados)
            frame = cv2.rotate(frame, cv2.ROTATE_180)

            # Mostrar el frame en la ventana de Pygame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = np.flip(frame, 1)
            frame_surface = pygame.surfarray.make_surface(frame)
            screen.blit(frame_surface, (0, 0))

            # Actualizar y dibujar el menú
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()

            main_menu.update(events)
            main_menu.draw(screen)

            pygame.display.update()

    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()

def show_menu():
    """ El menú donde se generarán los dos botones y por ende hacer clic en ellos """
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    color_mouse_pointer = (255, 0, 200)

    start_time = 0
    button_hovered = False # Variables que me dirán si el cursor está encima de un botón
    button_h = False

    # Configurar la ventana de pantalla
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Universidad de Xalapa")

    # Definir el tema personalizado
    custom_theme = pygame_menu.themes.Theme(
        background_color=(50, 0, 0),  # Color de fondo personalizado
        title_font_size=30,
        title_font_color=(255, 255, 255),
        widget_font_size=20,
        widget_font_color=(255, 255, 255),
        widget_font=pygame_menu.font.FONT_OPEN_SANS_BOLD
    )

    # Crear el menú con el tema personalizado
    main_menu = pygame_menu.Menu("Procesamiento de imágenes", 800, 600, theme=custom_theme)

    def button1():
        pygame.quit()

    def button2():
        start()

    main_menu.add.button("Salir", button1, button_id="salir_btn")  # Agregar un ID al botón
    main_menu.add.button("Comenzar", button2, button_id="comenzar_btn")  # Agregar un ID al botón

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5) as hands:
        while True:
            ret, frame = cap.read()
            if ret == False:
                break

            height, width, _ = frame.shape
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks is not None:
                for hand_landmarks in results.multi_hand_landmarks:
                    x = int(hand_landmarks.landmark[9].x * width)
                    y = int(hand_landmarks.landmark[9].y * height)
                    cv2.circle(frame, (x, y), 10, color_mouse_pointer, 3)
                    cv2.circle(frame, (x, y), 5, color_mouse_pointer, -1)
                    update_cursor_position(x, y)  # Actualizar posición del cursor

                    mouse_pos = pygame.mouse.get_pos()
                    button1_widget = main_menu.get_widget("salir_btn")  # Obtener el botón por su ID
                    button2_widget = main_menu.get_widget("comenzar_btn")
                    button1_rect = button1_widget.get_rect() if button1_widget else None  # Obtener el rectángulo del botón
                    button2_rect = button2_widget.get_rect() if button2_widget else None
                    # Lo que hace este if es comparar o verificar si el cursor esta encima del botón
                    if button1_rect and button1_rect.collidepoint(mouse_pos):  # Verificar si se encontró el botón y si se colisiona con el cursor
                        if not button_hovered:
                            start_time = pygame.time.get_ticks()
                            button_hovered = True
                        elif pygame.time.get_ticks() - start_time >= 1000:
                            button1()
                    else:
                        button_hovered = False
                    
                    if button2_rect and button2_rect.collidepoint(mouse_pos):  # Verificar si se encontró el botón y si se colisiona con el cursor
                        if not button_h:
                            start_time = pygame.time.get_ticks()
                            button_h = True
                        elif pygame.time.get_ticks() - start_time >= 1000:
                            button2()
                    else:
                        button_h = False

            # Girar el frame(180 grados)
            frame = cv2.rotate(frame, cv2.ROTATE_180)

            # Mostrar el frame en la ventana de Pygame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = np.flip(frame, 1)
            frame_surface = pygame.surfarray.make_surface(frame)
            screen.blit(frame_surface, (0, 0))

            # Actualizar y dibujar el menú
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()

            main_menu.update(events)
            main_menu.draw(screen)

            pygame.display.update()

    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()

show_menu()


