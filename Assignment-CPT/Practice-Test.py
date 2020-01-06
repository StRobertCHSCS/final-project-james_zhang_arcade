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

# start duck position
turtle_x = SCREEN_WIDTH/2
turtle_y = 170

# variables to control duck movement
left_pressed = False
right_pressed = False

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


def draw_ducks(x, y):
    # draw head
    arcade.draw_circle_filled(x, y, 20, arcade.color.BANANA_YELLOW)
    # draw eyes
    arcade.draw_ellipse_filled(x + 13.5, y + 10, 8.5, 10.5, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 14, y + 10, 2.5, arcade.color.BLACK)
    # draw beak
    arcade.draw_triangle_filled(x + 17.5, y + 1.5, x + 17.5, y - 8.5, x + 27.5, y - 3.5, arcade.color.ORANGE_RED)
    # draw body
    arcade.draw_circle_filled(x, y - 30, 25, arcade.color.BANANA_YELLOW)
    # draw legs and feet
    arcade.draw_rectangle_filled(x, y - 60, 5, 10, arcade.color.ORANGE_RED)
    arcade.draw_ellipse_filled(x + 5, y - 67, 17, 7, arcade.color.ORANGE_RED)
    # draw tail
    arcade.draw_ellipse_filled(x - 20, y - 50, 17, 7, arcade.color.BANANA_YELLOW, 30)


def on_update(delta_time):
    pass


def on_draw():
    global turtle_x, turtle_y
    arcade.start_render()
    
    draw_background_scenery()
    draw_ducks(100, 270)
    draw_turtle(turtle_x, turtle_y)

def on_key_press(key, modifiers):
    pass
     
def on_key_release(key, modifiers):
    pass


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