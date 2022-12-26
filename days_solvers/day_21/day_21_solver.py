from days_solvers import DaySolver
from .node import BinaryOperatorNode, IntegerNode
from .tree_walker import TreeWalker, ReverseTreeWalker


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
        ast = self.build_tree("root")
        is_left_subtree = self.find_node_to_fix(ast.lhs)
        tree_walker = TreeWalker()
        r_tree_walker = ReverseTreeWalker()
        if is_left_subtree:
            target = tree_walker.evaluate(ast.rhs)
            return r_tree_walker.evaluate(ast.lhs, target)
        else:
            target = tree_walker.evaluate(ast.lhs)
            return r_tree_walker.evaluate(ast.rhs, target)

    def build_tree(self, monkey):
        instr = self.input_data[monkey]
        if instr.isdigit():
            return IntegerNode(monkey, False, int(instr))
        lhs, op, rhs = instr.split(" ")
        lhs_node = self.build_tree(lhs)
        rhs_node = self.build_tree(rhs)
        return BinaryOperatorNode(monkey, False, lhs_node, op, rhs_node)

    def find_node_to_fix(self, node):
        if node.token == "int":
            node.fix = node.monkey == "humn"
            return node.monkey == "humn"
        node.fix = self.find_node_to_fix(node.lhs) or self.find_node_to_fix(node.rhs)
        return node.fix
