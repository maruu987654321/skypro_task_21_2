from controller import GameController

start_game = GameController()      # создаем объект 
start_game.make_field("""WTTTTTT         
gggKgggggW
ggTTTWWDgW
WKggggTggW
WKKKWWWWDG""")
start_game.play()                                # начинаем игру
