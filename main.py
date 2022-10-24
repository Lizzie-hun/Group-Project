from game.level import Level

def Main():
    first_level = Level(1)
    first_level.create_gates()
    print(first_level.get_gates())

if __name__ == Main():
    Main()