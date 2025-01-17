from math import sqrt


class Attacker:
    def __init__(self, repo):
        self.repo = repo
        self.used_blocks = []
        self.targets = []

    # def get_base_block_id(self, target_x: int, target_y: int):
    #     for base_block in self.repo.baseCells:
    #         if base_block not in self.used_blocks:
    #             x = base_block.get('x')
    #             y = base_block.get('y')
    #
    #             if base_block.get("range") >= sqrt(abs(x - target_x)**2 + abs(y - target_y)**2):
    #                 self.used_blocks.append(base_block)
    #                 return base_block.get("id")

    def create_attack_queue(self):
        if (self.repo.baseCells == None):
            print("I dont see any enemy.", end="")
            return []

        for base_block in self.repo.baseCells:
            if self.repo.enemyCells != None:
                for enemy_block in self.repo.enemyCells:
                    if enemy_block.get("attack") == 40:
                        enemy_command_center_x = enemy_block.get('x')
                        enemy_command_center_y = enemy_block.get('y')

                        base_block_id = base_block.get("id")
                        self.targets.append({
                            "blockId": base_block_id,
                            "target": {
                                "x": enemy_command_center_x,
                                "y": enemy_command_center_y
                            }
                        })
                        break
                continue

            if (self.repo.zombies != None):
                for zombie in self.repo.zombies:
                    zombie_x = zombie.get('x')
                    zombie_y = zombie.get('y')

                    base_block_id = base_block.get("id")
                    self.targets.append({
                        "blockId": base_block_id,
                        "target": {
                            "x": zombie_x,
                            "y": zombie_y
                        }
                    })
                    break
                continue

            if (self.repo.enemyCells != None):
                for enemy_block in self.repo.enemyCells:
                    if enemy_block.get("attack") != 40:
                        enemy_base_block_x = enemy_block.get('x')
                        enemy_base_block_y = enemy_block.get('y')

                        base_block_id = base_block.get("id")
                        self.targets.append({
                            "blockId": base_block_id,
                            "target": {
                                "x": enemy_base_block_x,
                                "y": enemy_base_block_y
                            }
                        })
                continue

        # if (self.repo.enemyCells != None):
        #     for enemy_block in self.repo.enemyCells:
        #         if enemy_block.get("attack") == 40:
        #             enemy_command_center_x = enemy_block.get('x')
        #             enemy_command_center_y = enemy_block.get('y')
        #
        #             health = enemy_block.get("health")
        #             while health > 0:
        #                 base_block_id = self.get_base_block_id(enemy_command_center_x, enemy_command_center_y)
        #                 self.targets.append({
        #                     "blockId": base_block_id,
        #                     "target": {
        #                         "x": enemy_command_center_x,
        #                         "y": enemy_command_center_y
        #                     }
        #                 })
        #                 health -= 10
        #
        #
        # if (self.repo.zombies != None):
        #     for zombie in self.repo.zombies:
        #         zombie_x = zombie.get('x')
        #         zombie_y = zombie.get('y')
        #
        #         base_block_id = self.get_base_block_id(zombie_x, zombie_y)
        #         self.targets.append({
        #             "blockId": base_block_id,
        #             "target": {
        #                 "x": zombie_x,
        #                 "y": zombie_y
        #             }
        #         })
        # if (self.repo.enemyCells != None):
        #     for enemy_block in self.repo.enemyCells:
        #         if enemy_block.get("attack") != 40:
        #             enemy_base_block_x = enemy_block.get('x')
        #             enemy_base_block_y = enemy_block.get('y')
        #
        #             base_block_id = self.get_base_block_id(enemy_base_block_x, enemy_base_block_y)
        #             self.targets.append({
        #                 "blockId": base_block_id,
        #                 "target": {
        #                     "x": enemy_base_block_x,
        #                     "y": enemy_base_block_y
        #                 }
        #             })

        return self.targets
