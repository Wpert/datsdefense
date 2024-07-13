import os

import requests


class Repo:

    def __init__(self):
        self.zpots = []
        self.baseCells = []
        self.enemyCells = []
        self.zombies = []
        self.gold = 0

        self.base = "https://games-test.datsteam.dev"
        self.headers = {"X-Auth-Token": os.environ.get("API_KEY", "invalid_key")}

    def signin(self):
        p = requests.put(self.base + "/play/zombidef/participate", headers=self.headers)
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
