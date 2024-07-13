import os
import typing
import requests
import json
import time
import sys

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

    def init_map(self):
        r = requests.get(self.base + "/play/zombidef/world", headers=self.headers)
        self.zpots = r.json()['zpots']

    def update(self) -> None:
        r = requests.get(self.base + "/play/zombidef/units", headers=self.headers)
        unitsInfo = r.json()

        try:
            self.turn = unitsInfo["turn"]
            waitNextTurnInMS = unitsInfo["turnEndsInMs"]
            print(f"Turn {self.turn} ends in {waitNextTurnInMS}")
        except e:
            print(e)
            return
        
        if (self.died_):
            time.sleep(waitNextTurnInMS / 1000)
            return

        try:
            self.baseCells = unitsInfo['base']
            self.enemyCells = unitsInfo['enemyBlocks']
            self.zombies = unitsInfo['zombies']
            self.player = unitsInfo['player']
            self.turn = unitsInfo["turn"]

            if (self.player["gameEndedAt"] != None):
                raise Exception("died")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            if err.message == "died":
                self.died_ = True
            # print(json.dumps(r.json(), indent=4))
        
        time.sleep(waitNextTurnInMS / 1000)

    def next_move(self, attack_queue, build_queue, new_base):
        requests.post(self.base + "/play/zombidef/command", headers=self.headers,
                      json={'attack': attack_queue,
                            'build': build_queue,
                            'moveBase': new_base})
