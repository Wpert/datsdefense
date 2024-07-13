from math import sqrt

from datsdefense.repo import repo


class Attack:
    def __init__(self):
        self.used_blocks = []
        self.targets = []

    def get_base_block_id(self, target_x: int, target_y: int):
        for base_block in repo.baseCells:
            if base_block not in self.used_blocks:
                x = base_block.get('x')
                y = base_block.get('y')

                if base_block.range >= sqrt(abs(x - target_x)**2 + abs(y - target_y)**2):
                    self.used_blocks.append(base_block)
                    return base_block.id

    def create_attack_queue(self):
        for zombie in repo.zombies:
            zombie_x = zombie.get('x')
            zombie_y = zombie.get('y')

            base_block_id = self.get_base_block_id(zombie_x, zombie_y)
            self.targets.append({
                "blockId": base_block_id,
                "target": {
                    "x": zombie_x,
                    "y": zombie_y
                }
            })
