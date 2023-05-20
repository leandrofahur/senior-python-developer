class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Cindy')
print(player1.name)
player1.speak()
