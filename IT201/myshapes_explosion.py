"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import random
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
EXPLOSION_TEXTURE_COUNT = 60

class Ball:
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = 30
        self.maxsize = 40
        self.minsize = 20
        self.gettingbigger = True

def make_ball():
    x = random.randrange(30,SCREEN_WIDTH-30)
    y = random.randrange(30,SCREEN_HEIGHT-30)
    dx = random.randrange(-3,3)
    dy = random.randrange(-3,3)

    myball = Ball(x,y,dx,dy)
    return myball

class Explosion(arcade.Sprite):
    """ This class creates an explosion animation """

    # Static variable that holds all the explosion textures
    explosion_textures = []

    def __init__(self, texture_list):
        super().__init__("images/explosion/explosion0000.png")

        # Start at the first frame
        self.current_texture = 0
        self.textures = texture_list

    def update(self):

        # Update to the next frame of the animation. If we are at the end
        # of our frames, then delete this sprite.
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.kill()


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMBER)

        
        self.explosions_list = None
        self.ball_list = []
        
        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):

        """ Set up the game and initialize the variables. """
        
        self.explosions_list = arcade.SpriteList()

        self.explosion_texture_list = []

        for i in range(EXPLOSION_TEXTURE_COUNT):
            # Files from http://www.explosiongenerator.com are numbered sequentially.
            # This code loads all of the explosion0000.png to explosion0270.png files
            # that are part of this explosion.
            texture_name = f"images/explosion/explosion{i:04d}.png"

            self.explosion_texture_list.append(arcade.load_texture(texture_name))
            
        # create 10 balls
        for i in range(10):
            myball = make_ball()
            self.ball_list.append(myball)
        
    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        
        self.explosions_list.draw()

        # Call draw() on all your sprite lists below
        print(len(self.ball_list))
        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, arcade.color.BLACK)

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        
        self.explosions_list.update()

        print(len(self.ball_list))
        for ball in self.ball_list:
            ball.x = ball.x + ball.dx
            ball.y = ball.y + ball.dy
            
            if ball.gettingbigger:
                if ball.size >= ball.maxsize:
                    ball.gettingbigger = False
                else:
                    ball.size = ball.size + 1
            else:
                if ball.size<=ball.minsize:
                    ball.gettingbigger = True
                else:
                    ball.size = ball.size -1

            if (ball.x >= (SCREEN_WIDTH - ball.size) or ball.x <= ball.size):
                ball.dx = -ball.dx
            
            if (ball.y >= (SCREEN_HEIGHT - ball.size) or ball.y <= ball.size):
                ball.dy = -ball.dy
            


    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        # here you should test for whether the click hits a ball
        explosion = Explosion(self.explosion_texture_list)
        explosion.center_x = x
        explosion.center_y = y
        self.explosions_list.append(explosion)
        
def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
