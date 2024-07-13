import os
import typing
import requests
import json

class Repo:

    def __init__(self):
        self.zpots = []
        self.baseCells = []
        self.enemyCells = []
        self.zombies = []
        self.gold = 0

        self.base = "https://games-test.datsteam.dev"
        api_key = ""
        if (os.path.isfile("API_KEY.txt")):
            with open("API_KEY.txt", "r") as fl:
                api_key = fl.read().replace('\n', '')
        else:
            api_key = os.environ.get("API_KEY", "invalid_key")
        
        print(api_key)
        self.headers = {"X-Auth-Token": api_key}

    def signin(self) -> int:
        p = requests.put(self.base + "/play/zombidef/participate", headers=self.headers)
        try:
            print("round starts in", p.json()['startsInSec'])
        except:
            print(json.dumps(p.json(), indent=4))
            return 0
        return p.json()['startsInSec']

    def init_map(self):
        r = requests.get(self.base + "/play/zombidef/world", headers=self.headers)
        self.zpots = r.json()['zpots']
        self.update()

    def update(self):
        r = requests.get(self.base + "/play/zombidef/units", headers=self.headers)
        self.baseCells = r.json()['base']
        self.enemyCells = r.json()['enemyBlocks']
        self.zombies = r.json()['zombies']
        self.gold = r.json()['player']['gold']
        return r.json()['turnEndsInMs']

    def next_move(self, attack_queue, build_queue, new_base):
        requests.post(self.base + "/play/zombidef/command", headers=self.headers,
                      json={'attack': attack_queue,
                            'build': build_queue,
                            'moveBase': new_base})
