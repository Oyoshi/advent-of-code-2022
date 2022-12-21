from days_solvers import DaySolver


class Node:
    pass


class BinaryOperatorNode(Node):
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs


class IntegerNode(Node):
    def __init__(self, val):
        self.value = val


class NodeVisitor:
    def visit(self, node):
        method_name = "visit_" + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception("No visit_{} method".format(type(node).__name__))


class TreeWalker(NodeVisitor):
    def evaluate(self, ast):
        return self.visit(ast)

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

    def build_tree(self, monkey):
        instr = self.input_data[monkey]
        if instr.isdigit():
            return IntegerNode(int(instr))
        lhs, op, rhs = instr.split(" ")
        lhs_node = self.build_tree(lhs)
        rhs_node = self.build_tree(rhs)
        return BinaryOperatorNode(lhs_node, op, rhs_node)

    def solve_part_2(self):
        pass
