class Builder:
    def __init__(self, repo):
        self.repo = repo
        self.gold = repo.player.get("gold")
        self.build_queue = []

    def get_command_center_coords(self):
        for base_block in self.repo.baseCells:
            if base_block.get("attack") == 40:
                return base_block.get("x"), base_block.get("y")

    def start_build(self):
        command_center_x, command_center_y = self.get_command_center_coords()
        self.build_queue += [
            {command_center_x - 1, command_center_y - 1},
            {command_center_x - 1, command_center_y},
            {command_center_x - 1, command_center_y + 1},
            {command_center_x, command_center_y + 1},
            {command_center_x + 1, command_center_y + 1},
        ]
        self.gold -= 5

    def build(self):
        return self.build_queue
