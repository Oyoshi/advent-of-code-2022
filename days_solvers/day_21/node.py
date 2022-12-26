class Node:
    def __init__(self, monkey, fix):
        self.monkey = monkey
        self.fix = fix


class BinaryOperatorNode(Node):
    def __init__(self, monkey, fix, lhs, op, rhs):
        super().__init__(monkey, fix)
        self.token = "binop"
        self.lhs = lhs
        self.op = op
        self.rhs = rhs


class IntegerNode(Node):
    def __init__(self, monkey, fix, val):
        super().__init__(monkey, fix)
        self.token = "int"
        self.value = val
