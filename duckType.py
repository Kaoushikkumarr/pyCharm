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

print()

class Editor:

    def excute(self):
        print("Checking another Duck Type Concept.")
        print("Use for coding.")


class IDE:

    def code(self, args):
        args.excute()
        # selfi.excute()

e = Editor()
ide = IDE()
ide.code(e)
