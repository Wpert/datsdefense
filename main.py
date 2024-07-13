import time
from repo import Repo

steps = 0

def main():
    rep = Repo()
    wait = rep.signin()
    time.sleep(wait)
    rep.init_map()
    while len(rep.baseCells) > 0:
        # think about move and move
        rep.next_move([], [], [])
        wait = rep.update()
        time.sleep(wait/1000)
        global steps
        print(f"I've did {steps} step")
        steps += 1

if __name__ == '__main__':
    main()
