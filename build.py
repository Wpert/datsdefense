class Builder:
    def __init__(self, repo):
        self.repo = repo
        self.gold = repo.player.get("gold")
        self.build_queue = []
        self.firstTurn = True

    # def MinimalSquareLen():
    #     command_center_x, command_center_y = self.get_command_center_coords()
    #     for i in range(-1, 2):
    #         for j in range(-1, 2):
                

    def get_command_center_coords(self):
        for base_block in self.repo.baseCells:
            if base_block.get("attack") == 40:
                return base_block.get("x"), base_block.get("y")

    def start_build(self):
        command_center_x, command_center_y = self.get_command_center_coords()
        self.build_queue += [
            {"x" : command_center_x - 1, "y" : command_center_y - 1},
            {"x" : command_center_x - 1, "y" : command_center_y},
            {"x" : command_center_x - 1, "y" : command_center_y + 1},
            {"x" : command_center_x, "y" : command_center_y + 1},
            {"x" : command_center_x + 1, "y" : command_center_y + 1},
        ]
        self.gold -= 5
    
    def build(self):
        self.start_build()

        return self.build_queue
