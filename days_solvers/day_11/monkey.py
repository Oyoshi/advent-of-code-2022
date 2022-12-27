class Monkey:
    def __init__(self, items, mod, div, dest_if_true, dest_if_false):
        self.items = items
        self.mod = mod
        self.div = div
        self.throw_dest = {True: dest_if_true, False: dest_if_false}
