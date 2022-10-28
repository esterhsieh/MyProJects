"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
Name: Ester
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    graphics.set_ball_velocity()
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    lives = NUM_LIVES
    collisions = 0
    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        while graphics.get_start():
            break_brick = graphics.check_collision()
            # 偵測碰撞到的物件是否為brick
            if break_brick is True:
                vy = -vy
                collisions += 1
            if break_brick is False:
                if vy > 0:
                    vy = -vy
                else:
                    vy = vy

            # 消除全部bricks，遊戲結束
            if collisions >= graphics.get_brick_qty():
                break

            # 碰到視窗邊界反彈，掉到底部少一條命
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                vx = -vx
            if graphics.ball.y <= 0:
                vy = -vy
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.reset_ball()
                lives -= 1
            graphics.ball.move(vx, vy)
            pause(FRAME_RATE)
        if lives <= 0:
            break


if __name__ == '__main__':
    main()
