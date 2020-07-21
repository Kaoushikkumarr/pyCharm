class Duck:
    def quack(self):
        print('Quack')
    def fly(self):
        print('Flap')


class Human:
    def quack(self):
        print('Trying to Quack like a duck')

    def fly(self):
        print('Spreading my arm to flap like a duck')

    # @staticmethod
def fly_quack(self):
    self.quack()
    self.fly()
    # pass
#
du = Duck()
fly_quack(du)
h = Human()
# h.quack()
# h.fly()
# h.fly_quack()
fly_quack(h)