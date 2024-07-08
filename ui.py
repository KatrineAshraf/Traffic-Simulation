from grid import *

pygame.init()
CLOCK = pygame.time.Clock()
FPS = 5
WIDTH, HEIGHT = 1200, 650
BLACK = (0, 0, 0)

grid = Grid(rows=13, columns=24, obstacle=GREEN_OBSTACLE)
grid.fill(DOWN_ROAD, rows=(0, 3), columns=(4, 4))
grid.fill(DOWN_ROAD, rows=(0, 3), columns=(14, 14))
grid.fill(LEFT_ROAD, rows=(4, 4), columns=(0, 23))
grid.fill(RIGHT_ROAD, rows=(6, 6), columns=(0, 23))
grid.fill(LEFT_ROAD, rows=(8, 8), columns=(0, 23))
grid.fill(UP_ROAD, rows=(9, 12), columns=(8, 8))
grid.fill(UP_ROAD, rows=(9, 12), columns=(19, 19))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
ICON = pygame.image.load("assets/icon.png")
pygame.display.set_caption("Traffic Simulator")
pygame.display.set_icon(ICON)
SCALE = grid.get_scale(screen)
run = True
pause = True
mouse_action = None
instruction_content = [
    {"text": "Pause/Resume", "image": [pygame.image.load("assets/spacebar.png")]},
    {"text": "Random Car Generation", "image": [pygame.image.load("assets/r.png")]},
    {"text": "Clear all tiles", "image": [pygame.image.load("assets/tab.png")]},
    {"text": "Add/Remove Car", "image": [pygame.image.load("assets/r_mouse.png")]},
     {"text": "Clear all cars", "image": [pygame.image.load("assets/c.png")]},
    {"text": "Insert a Green Tile", "image": [pygame.image.load("assets/g.png"), pygame.image.load("assets/l_mouse.png")]},
    {"text": "Insert a Up Road", "image": [pygame.image.load("assets/up.png"), pygame.image.load("assets/l_mouse.png")]},
    {"text": "Insert a Down Road", "image": [pygame.image.load("assets/down.png"),pygame.image.load("assets/l_mouse.png")]},
    {"text": "Insert a Left Road", "image": [pygame.image.load("assets/left.png"),pygame.image.load("assets/l_mouse.png")]},
    {"text": "Insert a Right Road", "image": [pygame.image.load("assets/right.png"),pygame.image.load("assets/l_mouse.png")]},
    {"text": "Exit", "image": [pygame.image.load("assets/esc.png")]},
]

def display_instruction_manual():
    # Define the dimensions and position of the instruction box
        box_width = 300
        box_height = 200
        box_x = (WIDTH - box_width) // 2
        box_y = (HEIGHT - box_height) // 2
    
    # Draw a semi-transparent background rectangle
        pygame.draw.rect(screen, (200, 200, 200, 128), (box_x, box_y, box_width, box_height))
    
    # Display instruction text
        font = pygame.font.Font(None, 24)
        text_y = box_y + 20
        for item in instruction_content:
        # Display image
            print(item)
            for image in item["image"]:
                screen.blit(image, (box_x + 30, text_y))
        
        # Display text
            text_surface = font.render(item["text"], True, BLACK)
            text_rect = text_surface.get_rect(midleft=(box_x + 100, text_y + 25))
            screen.blit(text_surface, text_rect)
        
            text_y += 70  # Adjust vertical spacing as needed
    
    # Update the display
        pygame.display.update()

while run:
    CLOCK.tick(FPS)
    screen.fill(BLACK)
    display_instruction_manual()
    for event in pygame.event.get():
        mouse_press = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYUP:
            key = event.key
            if key == pygame.K_ESCAPE:
                run = False
            elif key == pygame.K_SPACE:
                pause = not pause
            elif pause:
                if key == pygame.K_n:
                    grid.next_state()
                elif key == pygame.K_c:
                    grid.clear_cars()
                elif key == pygame.K_r:
                    grid.fill_randomly_with_cars(p=0.25)
                elif key == pygame.K_TAB:
                    grid.cells.fill(GREEN_OBSTACLE)
                elif key == pygame.K_UP:
                    mouse_action = "V-1"
                elif key == pygame.K_DOWN:
                    mouse_action = "V1"
                elif key == pygame.K_RIGHT:
                    mouse_action = "H1"
                elif key == pygame.K_LEFT:
                    mouse_action = "H-1"
                elif key == pygame.K_g:
                    mouse_action = "G"
        elif mouse_press[0] or mouse_press[2]:
            x, y = pygame.mouse.get_pos()
            x //= SCALE
            y //= SCALE
            cell = grid.cells[y][x]
            if mouse_press[0]:
                if mouse_action == "V-1":
                    grid.cells[y][x] = UP_ROAD.__copy__()
                elif mouse_action == "V1":
                    grid.cells[y][x] = DOWN_ROAD.__copy__()
                elif mouse_action == "H-1":
                    grid.cells[y][x] = LEFT_ROAD.__copy__()
                elif mouse_action == "H1":
                    grid.cells[y][x] = RIGHT_ROAD.__copy__()
                elif mouse_action == "G":
                    grid.cells[y][x] = GREEN_OBSTACLE
            else:
                if cell.state == 0:
                    grid.insert_car(y, x)
                else:
                    grid.remove_car(y, x)
    if not pause:
        grid.next_state()
    grid.draw(screen)
    pygame.display.update()

pygame.quit()