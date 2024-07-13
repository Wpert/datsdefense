import os
import typing
import requests
import json
import time
import sys

from attack import Attack

class Repo:

    def __init__(self):
        self.zpots = []
        self.baseCells = []
        self.enemyCells = []
        self.zombies = []
        self.player = {}
        self.died_ = False

        self.base = "https://games-test.datsteam.dev"
        api_key = ""
        if (os.path.isfile("API_KEY.txt")):
            with open("API_KEY.txt", "r") as fl:
                api_key = fl.read().replace('\n', '')
        else:
            api_key = os.environ.get("API_KEY", "invalid_key")
        
        print(api_key)
        self.headers = {"X-Auth-Token": api_key}


    def SignIn(self) -> None:
        startsInSec = 999
        while True:
            try:
                p = requests.put(self.base + "/play/zombidef/participate", headers=self.headers)
                startsInSec = p.json()['startsInSec']
                print(f"round starts in: {startsInSec}")
            except:
                print(json.dumps(p.json(), indent=4))
                return
            DELAY = 5
            time.sleep(min(DELAY, startsInSec))


    def InitMap(self):
        r = requests.get(self.base + "/play/zombidef/world", headers=self.headers)
        self.zpots = r.json()['zpots']


    def Update(self) -> None:
        r = requests.get(self.base + "/play/zombidef/units", headers=self.headers)
        unitsInfo = r.json()
        waitNextTurnInMS = 2000
        try:
            self.turn = unitsInfo["turn"]
            waitNextTurnInMS = unitsInfo["turnEndsInMs"]
            print(f"Turn {self.turn} ends in {waitNextTurnInMS}")
        except Exception as err:
            print(err)

        try:
            self.baseCells = unitsInfo['base']
            self.enemyCells = unitsInfo['enemyBlocks']
            self.zombies = unitsInfo['zombies']
            self.player = unitsInfo['player']
            self.turn = unitsInfo["turn"]

            print(f"Current gold: {self.player["gold"]}")
            if self.baseCells == None and not self.died_:
                print("I'm dead")
                self.died_ = True
                return

        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            print(json.dumps(r.json(), indent=4))

        self.next_move([], [])
        time.sleep(waitNextTurnInMS / 1000)

    def next_move(self, build_queue, new_base):
        if self.died_:
            print("I'm died, cannot attack")
            return

        atck = Attack(self)
        attack_queue = atck.create_attack_queue()
        print(f"I've attacked {len(attack_queue)} times.")

        requests.post(self.base + "/play/zombidef/command", headers=self.headers,
                      json={'attack': attack_queue,
                            'build': build_queue,
                            'moveBase': new_base})
