import time
from repo import Repo


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


if __name__ == '__main__':
    main()
