'''
-------------------------------------------------------------------------------
Name:		master.py
Purpose:	showcase the game that I have been working on>
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
collision_2 = False
collision_confirm = False
collision_confirm_2 = False

# game start screen
screen = "dead"

# score counter
score = 0

# input values for the ball locations
if screen == "dead":
    for _ in range(10):
        ball_x = [0, -200, -400, -600, -800, -1000, -1200, -1400, -1600, -1800, -2000, -2200, -2400, -2600, -2800, -3000, -3100, -3200, -3300, -3400, -3500 -3600, -3700, -3800, -3900, -4000]
        ball_y = [230]*26

# reset location of balls if dead
if screen == "actually_dead":
    for _ in range(5):
        ball_x = [0, -200, -400, -600, -800]
        ball_y = [230, 230, 230, 230, 230]
    
def draw_background_scenery():
    """[draw the background for the game]
    """
    # draw the land
    arcade.draw_rectangle_filled(200, 100, 400, 200, arcade.color.GREEN)
    arcade.draw_rectangle_filled(1200, 100, 400, 240, arcade.color.GREEN)

    # draw water
    arcade.draw_rectangle_filled(700, 70, 600, 200, arcade.color.BLUE)

    # draw sun
    arcade.draw_circle_filled(200, 700, 70, arcade.color.YELLOW)

    # draw clouds
    texture_1 = arcade.load_texture("Images/Cloud-for-game.png")
    arcade.draw_texture_rectangle(500, 700, texture_1.width*0.5, texture_1.height*0.5, texture_1, 0)
    arcade.draw_texture_rectangle(800, 600, texture_1.width*0.5, texture_1.height*0.5, texture_1, 0)
    arcade.draw_texture_rectangle(900, 800, texture_1.width*0.5, texture_1.height*0.5, texture_1, 0)
    arcade.draw_texture_rectangle(1200, 680, texture_1.width*0.5, texture_1.height*0.5, texture_1, 0)
    arcade.draw_texture_rectangle(100, 600, texture_1.width*0.5, texture_1.height*0.5, texture_1, 0)
    

def draw_wood(x, y):
    """[draw the player controlled character(wooden plank)]
    
    Arguments:
        x {[int]} -- [x value for wooden plank]
        y {[int]} -- [y value for wooden plank]
    """
    # draw the wooden plank
    texture_2 = arcade.load_texture("Images/wood.png")
    arcade.draw_texture_rectangle(x, y, texture_2.width*0.15, texture_2.height*0.15, texture_2, 0)


def draw_background():
    """[draw the start screen]
    """
    # load the texture for the homescreen
    texture_3 = arcade.load_texture("Images/game_start.png")
    arcade.draw_texture_rectangle(700, 400, texture_3.width*2, texture_3.height*2, texture_3, 0)


def on_update(delta_time):
    """[logic for game, and updates during game]
    
    Arguments:
        delta_time {[int]} -- [timer that moves the animation per frame]
    """
    global wood_x, wood_y, left_pressed, right_pressed, ball_x, ball_y, ball_speed, collision, screen, collision_confirm, collision_confirm_2, collision_2, score

    # on update for when you play game
    if screen == "alive":

        # moving character left and right
        ball_speed = 5
        if left_pressed:
            wood_x -= 15

        if right_pressed:
            wood_x += 15

        if wood_x == 490:
            left_pressed = False

        if wood_x == 910:
            right_pressed = False

        # for loop that moves the ball and handles collision test
        for index in range(len(ball_x)):
            collision = False
            collision_2 = False
            ball_x[index] += ball_speed
            
            if ball_x[index] >= 400 and ball_x[index] <= 470:
                ball_y[index] += ball_speed*3
                ball_x[index] += ball_speed

            if ball_x[index] >= 470 and ball_x[index] <= 571 and collision == False:
                ball_y[index] -= ball_speed*3
                ball_x[index] += ball_speed

            if ball_y[index] == 200 and wood_y == 170 and ball_x[index] == 570 and 400 < wood_x < 700:
                collision = True
                ball_x[index] += ball_speed
                ball_y[index] += ball_speed*3
                
            if ball_x[index] >= 571 and ball_x[index] <= 670 and collision == True:
                ball_x[index] += ball_speed
                ball_y[index] += ball_speed*3
                collision_confirm = True

            if ball_x[index] >= 571 and ball_x[index] <= 670 and collision_confirm == True:
                ball_x[index] += ball_speed
                ball_y[index] += ball_speed*3
            
            if ball_x[index] >= 670 and ball_x[index] <= 771 and collision == False:
                ball_y[index] -= ball_speed*6
                ball_x[index] += ball_speed*2
            
            if ball_y[index] == 200 and wood_y == 170 and ball_x[index] == 760 and 650 < wood_x < 1000:
                collision_2 = True
                ball_x[index] += ball_speed
                ball_y[index] += ball_speed*3
                
            if ball_x[index] >= 760 and ball_x[index] <= 860 and collision_2 == True:
                ball_x[index] += ball_speed
                ball_y[index] += ball_speed*3
                collision_confirm_2 = True

            if ball_x[index] >= 760 and ball_x[index] <= 860 and collision_confirm_2 == True:
                ball_x[index] += ball_speed
                ball_y[index] += ball_speed*3
                collision_confirm_2 = True

            if ball_x[index] >= 860 and ball_x[index] <= 1000 and collision_confirm_2 == True:
                ball_x[index] += ball_speed*4
                ball_y[index] -= ball_speed*7
            
            if ball_y[index] < 250 and ball_x[index] > 950:
                ball_y[index] = 250
            
            if ball_y[index] < 201:
                screen = "actually_dead"
            
            if ball_y[index] == 200 and wood_y == 170 and ball_x[index] == 760 and 650 > wood_x:
                screen = "actually_dead"

            if ball_x[index] == 1400:
                score += 1
                if score == 26:
                    screen = "done"

def on_draw():
    """[draw everything]
    """
    global wood_x, wood_y, ball_x, ball_y, x, y, ball_speed, collision, screen, score

    arcade.start_render()

    # draw start screen
    if screen == "dead":
        draw_background()

    # draw screen when dead
    if screen == "actually_dead":
        texture_4 = arcade.load_texture("Images/death_screen.png")
        arcade.draw_texture_rectangle(700, 400, texture_4.width*2, texture_4.height*2, texture_4, 0)

        # reset score
        score = 0

        # reset ball positions
        for _ in range(10):
            ball_x = [0, -200, -400, -600, -800, -1000, -1200, -1400, -1600, -1800, -2000, -2200, -2400, -2600, -2800, -3000, -3100, -3200, -3300, -3400, -3500, -3600, -3700, -3800, -3900, -4000]
            ball_y = [230]*26

    # draw items when playing game
    if screen == "alive":
        draw_background_scenery()
        draw_wood(wood_x, wood_y)
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

        # unload the x and y positions for balls
        for x, y in zip(ball_x, ball_y):
            arcade.draw_circle_filled(x, y, 30, arcade.color.YELLOW)

        # score counter
        arcade.draw_text("Score:" + str(score), 1250, 760, arcade.color.BLACK)
        
    # draw screen when done game
    if screen == "done":
        texture_5 = arcade.load_texture("Images/complete_screen.png")
        arcade.draw_texture_rectangle(700, 500, texture_5.width*1.6, texture_5.height*2, texture_5, 0)

        # reset score
        score = 0

        # reset ball positions
        for _ in range(10):
            ball_x = [0, -200, -400, -600, -800, -1000, -1200, -1400, -1600, -1800, -2000, -2200, -2400, -2600, -2800, -3000, -3100, -3200, -3300, -3400, -3500, -3600, -3700, -3800, -3900, -4000]
            ball_y = [230]*26

def on_key_press(key, modifiers):
    """[controls the key press when pressed]
    
    Arguments:
        key {[bool]} -- [which key is pressed]
        modifiers {[bool]} -- [keys that modify speed etc.]
    """
    global left_pressed, right_pressed, screen

    # confirm that a key was pressed to trigger movement
    if key == arcade.key.D:
        right_pressed = True

    if key == arcade.key.A:
        left_pressed = True
     
    if key == arcade.key.S and screen == "dead":
        screen = "alive"

    if key == arcade.key.S and screen == "actually_dead":
        screen = "alive"

def on_key_release(key, modifiers):
    """[controls the key press when released]
    
    Arguments:
        key {[bool]} -- [which key is released]
        modifiers {[bool]} -- [keys that modify speed etc. when released]
    """
    global left_pressed, right_pressed, screen
    
    # stop movement when key is released
    if key == arcade.key.D:
        right_pressed = False

    if key == arcade.key.A:
        left_pressed = False

    if key == arcade.key.S and screen == "dead":
        screen = "alive"
        
    if key == arcade.key.S and screen == "actually_dead":
        screen = "alive"


def setup():
    """[setup the game's methods and fps]
    """
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