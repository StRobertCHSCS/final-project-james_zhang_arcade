'''
-------------------------------------------------------------------------------
Name:		Practice-Test.py
Purpose:	testing out codes and designs for game>
Author:	    Zhang.J
Created:	23/12/2019
------------------------------------------------------------------------------
'''
import arcade

# set screen width and height
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

# start wood position
wood_x = SCREEN_WIDTH/2
wood_y = 170

# variables to control ball movement
left_pressed = False
right_pressed = False

# start ball speed
ball_speed = 0

# empty lists
ball_x = []
ball_y = []

# bool value for collision check
collision = False

# game start screen
screen = "dead"

for _ in range(5):
    ball_x = [0, -200, -400, -600, -800]
    ball_y = [230, 230, 230, 230, 230]
    
def draw_background_scenery():
    # draw the land
    arcade.draw_rectangle_filled(200, 100, 400, 200, arcade.color.GREEN)
    arcade.draw_rectangle_filled(1200, 100, 400, 170, arcade.color.GREEN)

    # draw water
    arcade.draw_rectangle_filled(700, 70, 600, 200, arcade.color.BLUE)

    # draw clouds and sun
    arcade.draw_circle_filled(200, 700, 70, arcade.color.YELLOW)

    # draw clouds
    texture_1 = arcade.load_texture("Images/Cloud-for-game.png")
    arcade.draw_texture_rectangle(500, 700, texture_1.width*0.5, texture_1.height*0.5, texture_1, 0)
    arcade.draw_texture_rectangle(800, 600, texture_1.width*0.5, texture_1.height*0.5, texture_1, 0)
    arcade.draw_texture_rectangle(900, 800, texture_1.width*0.5, texture_1.height*0.5, texture_1, 0)
    arcade.draw_texture_rectangle(1200, 680, texture_1.width*0.5, texture_1.height*0.5, texture_1, 0)
    arcade.draw_texture_rectangle(100, 600, texture_1.width*0.5, texture_1.height*0.5, texture_1, 0)


def draw_wood(x, y):
    texture_2 = arcade.load_texture("Images/wood.png")
    arcade.draw_texture_rectangle(x, y, texture_2.width*0.15, texture_2.height*0.15, texture_2, 0)


def draw_background():
    texture_3 = arcade.load_texture("Images/game_start.png")
    arcade.draw_texture_rectangle(700, 400, texture_3.width*(1400/1920), texture_3.height*(800/1080), texture_3, 0)


def on_update(delta_time):
    global wood_x, wood_y, left_pressed, right_pressed, ball_x, ball_y, ball_speed, collision, screen

    if screen == "alive":
        ball_speed = 5
    if left_pressed:
        wood_x -= 15

    if right_pressed:
        wood_x += 15

    if wood_x == 490:
        left_pressed = False

    if wood_x == 910:
        right_pressed = False

    for x2, y2 in zip(ball_x, ball_y):
        x2 += ball_speed
        
        if x2 >= 400 and x2 <= 470:
            y2 += ball_speed*3
            x2 += ball_speed

        if x2 >= 470 and x2 <= 571 and collision == False:
            y2 -= ball_speed*3
            x2 += ball_speed

        if y2 == 200 and wood_y == 170 and x2 == 570 and 400 < wood_x < 700:
            collision = True
            x2 += ball_speed
            y2 += ball_speed*3
            
        if collision:
            x2 += ball_speed
            y2 += ball_speed*3
           
def on_draw():
    global wood_x, wood_y, ball_x, ball_y, x, y, ball_speed, collision, screen

    arcade.start_render()

    if screen == "dead":
        draw_background()
        arcade.draw_text("Bouncing Balls Game!!", 230, 700, arcade.color.WHITE, 80)
        arcade.draw_text("Press S to start", 600, 400, arcade.color.WHITE, 30)

    if screen == "actually_dead":
        arcade.set_background_color(arcade.color.BLACK)
        arcade.draw_text("Press S to start", 600, 400, arcade.color.WHITE, 30)

    if screen == "alive":
        draw_background_scenery()
        draw_wood(wood_x, wood_y)
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

        for x, y in zip(ball_x, ball_y):
            arcade.draw_circle_filled(x, y, 30, arcade.color.YELLOW)
            

def on_key_press(key, modifiers):
    global left_pressed, right_pressed, screen
    if key == arcade.key.D:
        right_pressed = True

    if key == arcade.key.A:
        left_pressed = True
     
    if key == arcade.key.S:
        screen = "alive"


def on_key_release(key, modifiers):
    global left_pressed, right_pressed
    if key == arcade.key.D:
        right_pressed = False

    if key == arcade.key.A:
        left_pressed = False

    if key == arcade.key.S:
        screen = "alive"


def setup():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Ball Bouncing")
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()