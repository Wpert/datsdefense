import sys
import time
from repo import Repo

def main():
    rep = Repo()

    rep.SignIn()

    while True:
        # think about move and move
        rep.InitMap()
        rep.Update()

if __name__ == '__main__':
    main()
