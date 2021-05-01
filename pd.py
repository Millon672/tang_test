import sys,tty,termios
import time
import board
import adafruit_dotstar as dotstar
from led3 import *
# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
dots = dotstar.DotStar(board.SCK, board.MOSI, 11, brightness=1)






class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch


def get():
        global i
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print("up")
                dots[i] = (255,69,0)
                i = i + 1
                if i == 11:
                       while True:
                              rainbow_cycle(0)
        elif k=='\x1b[B':
                print("down")
        elif k=='\x1b[C':
                i = 0
                print("right")
        elif k=='\x1b[D':
                print("left")
        else:
                print("not an arrow key!")

def main():
        for i in range(0,20):
                get()

if __name__=='__main__':
        main()
