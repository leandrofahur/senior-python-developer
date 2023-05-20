class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):

        print(f'my name is {self.name} and {self.age} years old')

    @classmethod
    def adding_things(cls, num_1, num_2):
        return cls('Tommy', num_1 + num_2)

    @staticmethod
    def adding_things2(num_1, num_2):
        return num_1 + num_2


player1 = PlayerCharacter('Cindy', 44)
player1.speak()

player2 = PlayerCharacter.adding_things(2, 3)
print(player2)
print(PlayerCharacter.adding_things2(2, 3))
