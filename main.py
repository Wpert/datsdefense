import sys
import time
from repo import Repo

def main():
    rep = Repo()
    rep.SignIn()

    rep.init_map()
    while True:
        # think about move and move
        rep.next_move([], [], [])
        rep.update()

if __name__ == '__main__':
    main()
