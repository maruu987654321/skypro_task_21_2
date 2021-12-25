from Unit import *
from terrain import *


class Cell:
    def __init__(self, obj):
        self.obj = obj

    def get_object(self):
        return self.obj

    def set_object(self, obj):
        self.obj = obj

    def get_name(self):
        if isinstance(self.obj, Terrain):
            return self.obj.get_terrain()
        elif isinstance(self.obj, Unit):
            return self.obj.name


class Field:
    def __init__(self, field, unit, cols, rows):
        self.field = field
        self.unit = unit
        self.cols = cols
        self.rows = rows
        self.cell_under_unit = Cell(Grass())

    def get_cell(self, x, y):
        return self.field[y][x]

    def set_cell(self, cell, x, y):
        self.field[y][x] = cell

    def get_cell_under_unit(self):
        return self.cell_under_unit

    def set_cell_under_unit(self, cell):
        if cell.get_object().get_terrain() == "Key":
            self.cell_under_unit = Cell(Grass())
        else:
            self.cell_under_unit = cell

    def move_unit_up(self):
        x, y = self.unit.get_coordinates()
        if y > 0 and self.get_cell(x, y - 1).get_object().is_walkable():
            self.unit.set_coordinates(x, y - 1)
            self.set_cell(self.get_cell_under_unit(), x, y)
            new_cell = self.get_cell(x, y - 1)
            new_cell.obj.step_on(self.unit)
            self.set_cell_under_unit(self.get_cell(x, y - 1))
            self.set_cell(Cell(self.unit), x, y - 1)
        else:
            print("Не можешь идти таким путем")

    def move_unit_down(self):
        x, y = self.unit.get_coordinates()
        if y < self.get_rows() - 1 and self.get_cell(x, y + 1).get_object().is_walkable():
            self.unit.set_coordinates(x, y + 1)
            self.set_cell(self.get_cell_under_unit(), x, y)
            new_cell = self.get_cell(x, y + 1)
            new_cell.obj.step_on(self.unit)
            self.set_cell_under_unit(new_cell)
            self.set_cell(Cell(self.unit), x, y + 1)
        else:
            print("Не можешь идти таким путем")

    def move_unit_right(self):
        x, y = self.unit.get_coordinates()
        if x < self.get_cols() - 1 and self.get_cell(x + 1, y).get_object().is_walkable():
            self.unit.set_coordinates(x + 1, y)
            self.set_cell(self.get_cell_under_unit(), x, y)
            new_cell = self.get_cell(x + 1, y)
            new_cell.obj.step_on(self.unit)
            self.set_cell_under_unit(self.get_cell(x + 1, y))
            self.set_cell(Cell(self.unit), x + 1, y)
        else:
            print("Не можешь идти таким путем")

    def move_unit_left(self):
        x, y = self.unit.get_coordinates()
        if x > 0 and self.get_cell(x - 1, y).get_object().is_walkable():
            self.unit.set_coordinates(x - 1, y)
            self.set_cell(self.get_cell_under_unit(), x, y)
            new_cell = self.get_cell(x - 1, y)
            new_cell.obj.step_on(self.unit)
            self.set_cell_under_unit(new_cell)
            self.set_cell(Cell(self.unit), x - 1, y)
        else:
            print("Не можешь идти таким путем")


    def get_field(self):
        return self.field

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows
