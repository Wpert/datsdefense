import sys
import time
from repo import Repo

def main():
    rep = Repo()
    rep.SignIn()

    rep.InitMap()
    while True:
        # think about move and move
        rep.Update()

if __name__ == '__main__':
    main()
