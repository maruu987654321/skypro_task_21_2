from field import *
from Unit import Ghost
from terrain import *


class GameController:
    def __init__(self):
        self.mapping = {
            'Wall': '🔲',
            'Grass': '⬜',
            'Ghost': '👻',
            'Key': '🗝',
            'Door': '🚪',
            'Trap': '💀',
        }
        self.game_on = True
        self.hero = Ghost(hp=15, coord=(0, 0))
        self.field = None
        self.cell_under_hero = Cell(Grass())

    def make_field(self, levelstr_):
        str_lines = levelstr_.split("\n")
        rows = len(str_lines)
        cols = len(str_lines[0])

        field = []
        for i in range(len(str_lines)):
            field_line = []
            for j in range(len(str_lines[i])):
                obj = str_lines[i][j]
                if obj == "W":
                    cell = Cell(Wall())
                elif obj == "D":
                    cell = Cell(Door())
                elif obj == "T":
                    cell = Cell(Trap(5))
                elif obj == "G":
                    self.hero.set_coordinates(j, i)
                    cell = Cell(self.hero)
                elif obj == "K":
                    cell = Cell(Key())
                elif obj == "g":
                    cell = Cell(Grass())

                field_line.append(cell)

            field.append(field_line)

        self.field = Field(field, self.hero, cols, rows)

    def play(self):
        
        while self.game_on and not self.hero.has_escaped():
            self._draw_field()

            command = input('Куда вы хотите пойти?  ')

            if command == "a":
                self.field.move_unit_left()
            elif command == "d":
                self.field.move_unit_right()
            elif command == "w":
                self.field.move_unit_up()
            elif command == "s":
                self.field.move_unit_down()
            elif command == "exit":
                break

        if self.hero.has_escaped():
            print("Ты победитель!!!")

        

    def _draw_field(self):
        print("\n".join([f"{''.join([self.mapping[x.get_name()] for x in filed_row])}"
                          for filed_row in self.field.get_field()]))
