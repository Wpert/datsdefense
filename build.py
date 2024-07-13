class Builder:
    def __init__(self, repo):
        self.repo = repo
        self.gold = repo.player.get("gold")
        self.build_queue = []


        self.square_size = 4
        self.perimeter = 12
        self.cur_x, self.cur_y = -10000, -10000
        self.index = 0

        #****  - i < square_size: x+=1
        #*..*  - i >= square_size: y+=1
        #*..*  - i > square_size*2 - 2:x-=1
        #****  - i > perimeter - square_size + 2 : y-=1


    def get_command_center_coords(self):
        for base_block in self.repo.baseCells:
            if base_block.get("attack") == 40:
                return base_block.get("x"), base_block.get("y")

    def calc_perimeter(self):
        self.perimeter = self.square_size * 2 + (self.square_size - 2) * 2

    def start_build(self):
        if self.cur_x == -10000:
            self.cur_x, self.cur_y = self.get_command_center_coords()
            self.cur_x -= 1
            self.cur_y += 1

        while self.gold is not None and self.gold > 0:
            if self.index == self.perimeter:
                self.index = 0
                self.square_size += 1
                self.calc_perimeter()
                self.cur_x -= 1
                self.cur_y += 2
            self.build_queue += {'x': self.cur_x, 'y': self.cur_y}
            if self.index < self.square_size:
                self.cur_x += 1
            elif self.index > self.perimeter - self.square_size + 2:
                self.cur_y -= 1
            elif self.index > self.square_size * 2:
                self.cur_x -= 1
            elif self.index >= self.square_size:
                self.cur_y += 1
            self.index += 1
            self.gold -= 1



    def build(self):
        self.gold = self.repo.player.get("gold")
        self.start_build()

        return self.build_queue
