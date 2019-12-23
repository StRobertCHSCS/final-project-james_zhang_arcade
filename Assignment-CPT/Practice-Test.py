'''
-------------------------------------------------------------------------------
Name:		Practice-Test.py
Purpose:	testing out codes and designs for game>
Author:	    Zhang.J
Created:	23/12/2019
------------------------------------------------------------------------------
'''
import arcade


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

def draw_background_scenery():
    # draw the land
    arcade.draw_rectangle_filled(200, 100, 400, 200, arcade.color.GREEN)
    arcade.draw_rectangle_filled(1200, 100, 400, 200, arcade.color.GREEN)

    # draw water
    arcade.draw_rectangle_filled(700, 70, 600, 50, arcade.color.BLUE)

    # draw clouds and sun
    arcade.draw_circle_filled(300, 650, 40, arcade.color.YELLOW)
def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    
    draw_background_scenery()



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