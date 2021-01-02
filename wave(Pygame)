import pygame
from collections import deque

WIDE = 12
HIGHT = 12
SIZE_CELL = 50

INF = 100000

pygame.init()
size = (1024, 640)
screen = pygame.display.set_mode(size)
color = (255, 255, 255)
font = pygame.font.SysFont("Arial", 50)

if HIGHT * SIZE_CELL > size[1] or WIDE * SIZE_CELL > 600:
    print("Некоректные размеры")
    quit()

x_start = -INF
y_start = -INF
x_finish = -INF
y_finish = -INF

field = [[0 for i in range(HIGHT)] for j in range(WIDE)]
for i in range(WIDE):
    for j in range(HIGHT):
        if i == 0 or j == 0 or j == HIGHT - 1 or i == WIDE - 1:
            field[i][j] = -1

screen.fill((255, 255, 255))
status_button = 0
status_way = False


def draw_button(text, x, y, size_of_button, size_text, color_of_button):
    global font, event
    font = pygame.font.SysFont("Arial", size_text)
    pygame.draw.rect(screen, color_of_button, (x, y, size_of_button[0], size_of_button[1]), 0)
    text = font.render(text, True, (0, 0, 0))
    screen.blit(text, (x, y))


def is_button_down(x, y, size_of_button):
    global event
    if event.type == pygame.MOUSEBUTTONDOWN:
        x1, y1 = event.pos
        if x < x1 < x + size_of_button[0] and y < y1 < y + size_of_button[1]:
            return False
    return True


def write_text_all(text, status_fill, x, y, color_of_text, size_text):
    global font, size
    font = pygame.font.SysFont("Arial", size_text)
    if status_fill:
        screen.fill((255, 255, 255))
    text = font.render(text, True, color_of_text)
    screen.blit(text, (x, y))


def draw_map():
    global WIDE, HIGHT, y_start, x_start, y_finish, x_finish, SIZE_CELL, INF
    for i in range(WIDE):
        for j in range(HIGHT):
            if field[j][i] == -1:
                pygame.draw.rect(screen, (0, 0, 0), (i * SIZE_CELL, j * SIZE_CELL, SIZE_CELL, SIZE_CELL), 0)
            elif i == x_start and j == y_start:
                pygame.draw.rect(screen, (0, 255, 0), (i * SIZE_CELL, j * SIZE_CELL, SIZE_CELL, SIZE_CELL), 0)
            elif i == x_finish and j == y_finish:
                pygame.draw.rect(screen, (255, 0, 0), (i * SIZE_CELL, j * SIZE_CELL, SIZE_CELL, SIZE_CELL), 0)
            elif field[j][i] == INF:
                pygame.draw.rect(screen, (115, 0, 255), (i * SIZE_CELL, j * SIZE_CELL, SIZE_CELL, SIZE_CELL), 0)
            else:
                pygame.draw.rect(screen, (255, 255, 255), (i * SIZE_CELL, j * SIZE_CELL, SIZE_CELL, SIZE_CELL), 0)


def make_field(type_firt):  # wall, start_or_finish
    global event, x_start, y_start, x_finish, y_finish
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        x //= SIZE_CELL
        y //= SIZE_CELL
        if x == 0 or y == 0 or y >= HIGHT - 1 or x >= WIDE - 1:
            return
        if type_firt == "wall":
            if event.button == 3:
                field[y][x] = 0
            elif event.button == 1:
                field[y][x] = -1
        if type_firt == "start_or_finish":
            if event.button == 1:
                x_start = x
                y_start = y
            elif event.button == 3:
                x_finish = x
                y_finish = y


def make_wave():
    global field, HIGHT, WIDE, x_start, y_start, y_finish, x_finish
    queue_of_cell = deque()
    field[y_start][x_start] = 1
    delta_x = [0, 0, 1, -1]
    delta_y = [1, -1, 0, 0]
    for i in range(4):
        y_temporary = y_start + delta_y[i]
        x_temporary = x_start + delta_x[i]
        if field[y_temporary][x_temporary] == 0:
            queue_of_cell.append([y_temporary, x_temporary])
            field[y_temporary][x_temporary] = 2
    while len(queue_of_cell) != 0:
        y, x = queue_of_cell.popleft()
        for i in range(4):
            y_temporary = y + delta_y[i]
            x_temporary = x + delta_x[i]
            if field[y_temporary][x_temporary] == 0:
                queue_of_cell.append([y_temporary, x_temporary])
                field[y_temporary][x_temporary] = field[y][x] + 1


def find_way():
    global field, x_start, y_start, x_finish, y_finish, INF, status_way
    status_way = True
    y_temporary = y_finish
    x_temporary = x_finish
    delta_x = [0, 0, 1, -1]
    delta_y = [1, -1, 0, 0]
    if field[y_finish][x_finish] == 0:
        return False
    lenth = field[y_finish][x_finish]
    while lenth > 0:
        lenth -= 1
        for i in range(4):
            x_temporary_in_for = x_temporary + delta_x[i]
            y_temporary_in_for = y_temporary + delta_y[i]
            if field[y_temporary_in_for][x_temporary_in_for] == lenth:
                x_temporary = x_temporary_in_for
                y_temporary = y_temporary_in_for
                field[y_temporary][x_temporary] = INF
    return True


def slide_1_introduction():
    write_text_all("Привет!", True, 400, 45, (0, 0, 0), 50)
    write_text_all("Эта программа находит путь", False, 150, 125, (0, 0, 0), 50)
    write_text_all("из одной точки в другую в лабиринте.", False, 75, 200, (0, 0, 0), 50)
    write_text_all("Нажмите Далее, чтобы продолжить.", False, 100, 275, (0, 0, 0), 50)
    write_text_all("Влад Бурмистров, 2020", False, 250, 550, (0, 0, 0), 50)
    draw_button("Далее", 450, 400, (150, 60), 50, (0, 227, 235))
    pygame.display.update()


def slide_2_make_walls():
    screen.fill((255, 255, 255))
    make_field("wall")
    draw_map()
    write_text_all("Постройте перегородки", False, 630, 50, (0, 0, 0), 35)
    write_text_all("Левая кнопка мыши – строит", False, 650, 150, (0, 0, 0), 24)
    write_text_all("Правая кнопка мыши – убирает", False, 650, 200, (0, 0, 0), 24)
    draw_button("Далее", 750, 300, (150, 60), 50, (0, 227, 235))
    draw_button("Назад", 750, 400, (150, 60), 50, (0, 100, 200))


def slide_3_make_start_and_finish():
    screen.fill((255, 255, 255))
    make_field("start_or_finish")
    draw_map()
    write_text_all("Отметьте:", False, 630, 50, (0, 0, 0), 35)
    write_text_all("Левая кнопка мыши – старт", False, 650, 150, (0, 0, 0), 24)
    write_text_all("Правая кнопка мыши – финиш", False, 650, 200, (0, 0, 0), 24)
    draw_button("Далее", 750, 300, (150, 60), 50, (0, 227, 235))
    draw_button("Назад", 750, 400, (150, 60), 50, (0, 100, 200))


def slide_4_way():
    global status_way
    if not status_way:
        screen.fill((255, 255, 255))
        if field[y_finish][x_finish] != 0:
            write_text_all("Путь найден!", False, 650, 150, (0, 0, 0), 30)
        else:
            write_text_all("Ошибка. Путь не найден.", False, 650, 150, (255, 0, 0), 30)
        make_wave()
        find_way()
        draw_map()


def hex(decimal):
    lenght = len(str(decimal))
    hex_number = ""
    hex_digits = "0123456789abcdef"
    for i in range(1, lenght + 1):
        d = decimal % 16
        hex_number = hex_digits[d] + hex_number
        decimal = decimal // 16
    if len(hex_number) == 3:
        return hex_number[1:]
    return hex_number


def make_colora_for_wave():
    colors = []
    for j in range(0, 256, 16):
        val2 = hex(j)
        while len(val2) != 2:
            val2 = "0" + val2
        val = "#" + "00" + val2 + "ff"
        colors.append(val)
    for j in range(255, -1, -16):
        val2 = hex(j)
        while len(val2) != 2:
            val2 = "0" + val2
        val = "#" + "00ff" + val2
        colors.append(val)
    for j in range(0, 256, 16):
        val2 = hex(j)
        while len(val2) != 2:
            val2 = "0" + val2
        val = "#" + val2 + "ff00"
        colors.append(val)
    for j in range(255, -1, -16):
        val2 = hex(j)
        while len(val2) != 2:
            val2 = "0" + val2
        val = "#" + "ff" + val2 + "00"
        colors.append(val)
    return colors


def draw_wave():
    global SIZE_CELL, colors
    screen.fill((255, 255, 255))
    make_wave()
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[j][i] == -1:
                pygame.draw.rect(screen, (0, 0, 0), (i * SIZE_CELL, j * SIZE_CELL, SIZE_CELL, SIZE_CELL), 0)
            else:
                pygame.draw.rect(screen, colors[field[j][i]],
                                 (i * SIZE_CELL, j * SIZE_CELL, SIZE_CELL, SIZE_CELL), 0)
    draw_button("Далее", 750, 300, (150, 60), 50, (0, 227, 235))


def main():
    global status_button
    if not is_button_down(750, 400, (150, 60)) and status_button <= 2:
        status_button -= 1
    else:
        if status_button == 0:
            slide_1_introduction()
            if not is_button_down(450, 400, (150, 60)):
                status_button = max(status_button, 1)
        elif status_button == 1:
            slide_2_make_walls()
            if not is_button_down(750, 300, (150, 60)):
                status_button = max(status_button, 2)
        elif status_button == 2:
            slide_3_make_start_and_finish()
            if not is_button_down(750, 300, (150, 60)):
                status_button = max(status_button, 3)
        elif status_button == 3:
            draw_wave()
            if not is_button_down(750, 300, (150, 60)):
                status_button = max(status_button, 4)
        else:
            slide_4_way()


colors = make_colora_for_wave()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        else:
            main()
    pygame.display.update()
