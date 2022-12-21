from days_solvers import DaySolver


class Node:
    def __init__(self, monkey):
        self.monkey = monkey


class BinaryOperatorNode(Node):
    def __init__(self, monkey, lhs, op, rhs):
        super().__init__(monkey)
        self.token = "binop"
        self.lhs = lhs
        self.op = op
        self.rhs = rhs


class IntegerNode(Node):
    def __init__(self, monkey, val):
        super().__init__(monkey)
        self.token = "int"
        self.value = val


class TreeWalker:
    def evaluate(self, ast):
        return self.visit(ast)

    def visit(self, node):
        if node.token == "int":
            return self.visit_IntegerNode(node)
        elif node.token == "binop":
            return self.visit_BinaryOperatorNode(node)
        raise Exception(f"No visitor")

    def visit_BinaryOperatorNode(self, node):
        if node.op == "+":
            return self.visit(node.lhs) + self.visit(node.rhs)
        elif node.op == "-":
            return self.visit(node.lhs) - self.visit(node.rhs)
        elif node.op == "*":
            return self.visit(node.lhs) * self.visit(node.rhs)
        elif node.op == "/":
            return self.visit(node.lhs) // self.visit(node.rhs)

    def visit_IntegerNode(self, node):
        return node.value


class Day21Solver(DaySolver):
    def __init__(self):
        self.day = "21"

    def load_input_impl(self, file):
        return {
            instr[0]: instr[1] for instr in [line.rstrip().split(": ") for line in file]
        }

    def solve_part_1(self):
        ast = self.build_tree("root")
        tree_walker = TreeWalker()
        return tree_walker.evaluate(ast)

    def solve_part_2(self):
        pass

    def build_tree(self, monkey):
        instr = self.input_data[monkey]
        if instr.isdigit():
            return IntegerNode(monkey, int(instr))
        lhs, op, rhs = instr.split(" ")
        lhs_node = self.build_tree(lhs)
        rhs_node = self.build_tree(rhs)
        return BinaryOperatorNode(monkey, lhs_node, op, rhs_node)
