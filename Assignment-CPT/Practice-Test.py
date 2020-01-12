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
ball_speed = 5

# empty lists
ball_x = []
ball_y = []

# bool value for collision check
collision = False

# game start screen

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

def on_update(delta_time):
    global wood_x, wood_y, left_pressed, right_pressed, ball_x, ball_y, ball_speed, collision
    if left_pressed:
        wood_x -= 15

    if right_pressed:
        wood_x += 15

    if wood_x == 490:
        left_pressed = False

    if wood_x == 910:
        right_pressed = False


    for index in range(len(ball_x)):
        ball_x[index] += ball_speed
        """
        if collision:
            ball_x[index] += ball_speed
            ball_y[index] += ball_speed*3
            """
        if ball_x[index] >= 400 and ball_x[index] <= 470:
            ball_y[index] += ball_speed*3
            ball_x[index] += ball_speed

        if ball_x[index] >= 470 and ball_x[index] <= 571: #and collision == False
            ball_y[index] -= ball_speed*3
            ball_x[index] += ball_speed

        if ball_y[index] == 200 and wood_y == 170 and ball_x[index] == 570 and 400 < wood_x < 800:
            #collision = True 
            ball_x[index] += ball_speed
            ball_y[index] += ball_speed*3
           

def on_draw():
    global wood_x, wood_y, ball_x, ball_y, x, y, ball_speed, collision
    arcade.start_render()
    
    draw_background_scenery()
    for x, y in zip(ball_x, ball_y):
        arcade.draw_circle_filled(x, y, 30, arcade.color.YELLOW)
    draw_wood(wood_x, wood_y)
            
def on_key_press(key, modifiers):
    global left_pressed, right_pressed
    if key == arcade.key.D:
        right_pressed = True

    if key == arcade.key.A:
        left_pressed = True
     
def on_key_release(key, modifiers):
    global left_pressed, right_pressed
    if key == arcade.key.D:
        right_pressed = False

    if key == arcade.key.A:
        left_pressed = False

def on_mouse_press(x, y, button, modifiers):
    pass

def setup():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Ball Bouncing")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()