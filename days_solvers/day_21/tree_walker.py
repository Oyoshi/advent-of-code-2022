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


class ReverseTreeWalker:
    def evaluate(self, ast, target):
        return self.visit(ast, target)

    def visit(self, node, target):
        if node.token == "int":
            return self.visit_IntegerNode(node, target)
        elif node.token == "binop":
            return self.visit_BinaryOperatorNode(node, target)
        raise Exception(f"No visitor")

    def visit_BinaryOperatorNode(self, node, target):
        if node.op == "+":
            if node.rhs.fix:
                ev = self.visit(node.lhs, target)
                new_target = target - ev
                return self.visit(node.rhs, new_target)
            elif node.lhs.fix:
                ev = self.visit(node.rhs, target)
                new_target = target - ev
                return self.visit(node.lhs, new_target)
            else:
                return self.visit(node.lhs, target) + self.visit(node.rhs, target)
        elif node.op == "-":
            if node.rhs.fix:
                ev = self.visit(node.lhs, target)
                new_target = ev - target
                return self.visit(node.rhs, new_target)
            elif node.lhs.fix:
                ev = self.visit(node.rhs, target)
                new_target = target + ev
                return self.visit(node.lhs, new_target)
            else:
                return self.visit(node.lhs, target) - self.visit(node.rhs, target)
        elif node.op == "*":
            if node.rhs.fix:
                ev = self.visit(node.lhs, target)
                new_target = target // ev
                return self.visit(node.rhs, new_target)
            elif node.lhs.fix:
                ev = self.visit(node.rhs, target)
                new_target = target // ev
                return self.visit(node.lhs, new_target)
            else:
                return self.visit(node.lhs, target) * self.visit(node.rhs, target)
        elif node.op == "/":
            if node.rhs.fix:
                ev = self.visit(node.lhs, target)
                new_target = ev // target
                return self.visit(node.rhs, new_target)
            elif node.lhs.fix:
                ev = self.visit(node.rhs, target)
                new_target = target * ev
                return self.visit(node.lhs, new_target)
            else:
                return self.visit(node.lhs, target) // self.visit(node.rhs, target)

    def visit_IntegerNode(self, node, target):
        return target if node.fix else node.value
