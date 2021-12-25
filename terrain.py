class Terrain:
    def __init__(self, name, walkable):
        self.name = name
        self.walkable = walkable

    def is_walkable(self):
        return self.walkable

    def get_terrain(self):
        return self.name

    def step_on(self, unit):
        raise NotImplementedError()


class Door(Terrain):
    def __init__(self):
        super().__init__(name="Door", walkable=True)

    def step_on(self, unit):
        if unit.has_key():
            unit.escaped = True
        else:
            print("You need a key to escape")


class Key(Terrain):
    def __init__(self):
        super().__init__(name="Key", walkable=True)

    def step_on(self, unit):
        unit.set_key()
        print(f"You got the key")


class Trap(Terrain):
    def __init__(self, damage):
        super().__init__(name="Trap", walkable=True)
        self.damage = damage

    def step_on(self, unit):
        unit.get_damage(self.damage)
        print(f"You got damage {self.damage} hp")
        print(f"{unit.hp} hp left")


class Grass(Terrain):
    def __init__(self):
        super().__init__(name="Grass", walkable=True)

    def step_on(self, unit):
        pass


class Wall(Terrain):
    def __init__(self):
        super().__init__(name="Wall", walkable=False)

    def step_on(self, unit):
        pass
