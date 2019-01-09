"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ball:
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.maxsize = 30
        self.minsize = 10
        self.size = 20
        self.isitgrowing = True

def make_ball():
    x = random.randrange(30,SCREEN_WIDTH-30)
    y = random.randrange(30,SCREEN_HEIGHT-30)
    dx = random.randrange(-3,3)
    dy = random.randrange(-3,3)

    myball = Ball(x,y,dx,dy)
    return myball

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

        self.ball_list = []

        # If you have sprite lists, you should create them here,
        # and set them to None

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, arcade.color.BLACK)

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        
        for ball in self.ball_list:
            ball.x = ball.x + ball.dx
            ball.y = ball.y + ball.dy
            
            if (ball.x >= (SCREEN_WIDTH - ball.size) or ball.x <= ball.size):
                ball.dx = -ball.dx
            
            if (ball.y >= (SCREEN_HEIGHT - ball.size) or ball.y <= ball.size):
                ball.dy = -ball.dy
                
            if ball.isitgrowing:
                if ball.size < ball.maxsize:
                    ball.size = ball.size +1
                else:
                    ball.isitgrowing = False
            else:
                if ball.size > ball.minsize:
                    ball.size = ball.size -1
                else:
                    ball.isitgrowing = True
            


    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        myball = make_ball()
        self.ball_list.append(myball)


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
