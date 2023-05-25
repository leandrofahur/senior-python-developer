class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def attack(self):
        print(f'attacking with power of {self._power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self._num_arrows}')


print('---')
wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()
print('---')

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
print(isinstance(archer1, Wizard))
print(isinstance(archer1, User))
print(isinstance(archer1, object))
print('---')
