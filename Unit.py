class Unit:
    def __init__(self, hp, coord, escaped=False, got_key=False):
        self.hp = hp
        self.coord = coord
        self.got_key = got_key
        self.escaped = escaped

    def has_key(self):
        return self.got_key

    def set_key(self):
        self.got_key = True

    def has_escaped(self):
        return self.escaped

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, damage):
        self.hp -= damage
        

    def set_coordinates(self, x, y):
        self.coord = (x, y)

    def get_coordinates(self):
        return self.coord

    def has_position(self, x, y):
        return self.coord == (x, y)


class Ghost(Unit):
    def __init__(self, hp, coord):
        super().__init__(hp=hp, coord=coord)
        self.name = "Ghost"
