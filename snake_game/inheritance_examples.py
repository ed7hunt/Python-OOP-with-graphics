class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("(under water)")

    def swim(self):
        print("I am swimming.")


nemo = Fish()
nemo.swim()
nemo.breathe()
