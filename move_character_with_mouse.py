from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')
coord = [] * 20

def draw_all_hand():
    for i in range(len(coord)):
        hand.draw(coord[2 * (i // 2 - 1)], coord[2 * (i // 2 - 1) + 1])

def move_to_line():
    global mx, my, frame
    global coord, go

    if len(coord) <= 0:
        return
    frame = (frame + 1) % 8
    t = go / 100
    mx = (1 - t) * mx + t * coord[0]
    my = (1 - t) * my + t * coord[1]

    if (go == 100):
        del coord[1]
        del coord[0]
    go = (go + 10) % 110
    delay(0.05)

def draw_boy():
    if len(coord) <= 0:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, mx, my)
        return
    if (mx >= coord[0]):
        character.clip_draw(frame * 100, 100 * 0, 100, 100, mx, my)
    else:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, mx, my)
    update_canvas()

def handle_events():
    global running
    global x, y
    global coord
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            coord.append(x)
            coord.append(y)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    hand.draw(x, y)
    pass



running = True
mx, my = TUK_WIDTH // 2, TUK_HEIGHT // 2
x = random.randint(300,900)
y = random.randint(300,900)
frame = 0
go = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    handle_events()
    draw_all_hand()
    move_to_line()
    draw_boy()
    update_canvas()
close_canvas()

