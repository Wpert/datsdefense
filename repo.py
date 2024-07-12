import json
import os
import requests


class Repo:

    def __init__(self):
        self.zpots = []
        self.baseCells = []
        self.enemyCells = []
        self.zombies = []

        self.base = "https://games-test.datsteam.dev"
        self.headers = {"X-Auth-Token": os.environ.get("API_KEY", "invalid_key")}

    def begin(self):
        requests.put(self.base + "/play/zombidef/participate", headers=self.headers)
        r = requests.get(self.base + "/play/zombidef/world", headers=self.headers)
        self.zpots = r.json()['zpots']
        self.update()

    def update(self):
        r = requests.get(self.base + "/play/zombidef/units", headers=self.headers)
        self.baseCells = r.json()['base']
        self.enemyCells = r.json()['enemyBlocks']
        self.zombies = r.json()['zombies']
