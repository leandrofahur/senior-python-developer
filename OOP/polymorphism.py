class User:
    def __init__(self, email):
        self._email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self._name = name
        self._power = power

    def attack(self):
        print(f'attacking with power of {self._power}')


print('--- Polymorphism ---')
wizard1 = Wizard('Merlin', 50, 'merlin@mail.com')
print(wizard1._email)
