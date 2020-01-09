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

# start turtle position
turtle_x = SCREEN_WIDTH/2
turtle_y = 170

# variables to control duck movement
left_pressed = False
right_pressed = False

# start duck speed
duck_speed = 5

# empty lists
duck_x = []
duck_y = []

for _ in range(10):
    duck_x = [0, -200, -400, -600, -800]
    y = 230
    duck_y.append(y)

def draw_background_scenery():
    # draw the land
    arcade.draw_rectangle_filled(200, 100, 400, 200, arcade.color.GREEN)
    arcade.draw_rectangle_filled(1200, 100, 400, 200, arcade.color.GREEN)

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

def draw_turtle(x, y):
    texture_2 = arcade.load_texture("Images/turtle.png")
    arcade.draw_texture_rectangle(x, y, texture_2.width*0.3, texture_2.height*0.3, texture_2, 0)

def on_update(delta_time):
    global turtle_x, turtle_y, left_pressed, right_pressed, duck_x, duck_y, duck_speed
    if left_pressed:
        turtle_x -= 15
    if right_pressed:
        turtle_x += 15

    if turtle_x == 490:
        left_pressed = False
    if turtle_x == 910:
        right_pressed = False
    
    for index in range(len(duck_x)):
        duck_x[index] += duck_speed
        if duck_x[index] >= 400 and duck_x[index] <= 500:
            duck_y[index] += duck_speed*3
            duck_x[index] += duck_speed
        if duck_x[index] >= 500 and duck_x[index] <= 700:
            duck_y[index] -= duck_speed*3
            duck_x[index] += duck_speed

def on_draw():
    global turtle_x, turtle_y, duck_x, duck_speed, duck_y, x, y
    arcade.start_render()
    
    draw_background_scenery()
    for x, y in zip(duck_x, duck_y):
        arcade.draw_circle_filled(x, y, 30, arcade.color.YELLOW)
    draw_turtle(turtle_x, turtle_y)

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
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "My Arcade Game-Turtles Bouncing Ducks")
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