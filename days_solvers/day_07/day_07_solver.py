from days_solvers import DaySolver
import re


class TreeNode:
    def __init__(self, cur_dir):
        self.dir = cur_dir
        self.files_size = 0
        self.acc_size = 0
        self.children = None
        self.parent = None

    def add_subdir(self, dir_name):
        subdir = TreeNode(dir_name)
        subdir.parent = self
        self.children = self.children + [subdir] if self.children else [subdir]


class Day07Solver(DaySolver):
    def __init__(self):
        self.day = "07"

    def load_input_impl(self, file):
        return [line.rstrip() for line in file]

    def solve_part_1(self):
        dir_tree = self.create_tree()
        self.traverse_tree_acc(dir_tree)
        return self.sum_tree_weights(dir_tree)

    def solve_part_2(self):
        dir_tree = self.create_tree()
        self.traverse_tree_acc(dir_tree)
        used_space_total = dir_tree.acc_size
        total_space = 70000000
        min_space = 30000000
        diff = total_space - used_space_total
        return self.find_min_dir(dir_tree, total_space, min_space - diff)

    def create_tree(self):
        dir_tree = TreeNode("/")
        pointer = dir_tree
        for cmd in self.input_data[1:]:
            if "dir" in cmd:
                pointer.add_subdir(cmd.split()[1])
            elif re.search(r"\d", cmd):
                pointer.files_size += int(cmd.split()[0])
                pointer.acc_size = pointer.files_size
            elif "cd" in cmd:
                if ".." in cmd:
                    pointer = pointer.parent
                else:
                    pointer = next(
                        c for c in pointer.children if c.dir == cmd.split()[2]
                    )
        return dir_tree

    def traverse_tree_acc(self, tree):
        if tree.children == None:
            return tree.acc_size
        for subdir in tree.children:
            tree.acc_size += self.traverse_tree_acc(subdir)
        return tree.acc_size

    def sum_tree_weights(self, tree):
        partial_sum = 0
        if tree.children != None:
            for subdir in tree.children:
                partial_sum += self.sum_tree_weights(subdir)
        return tree.acc_size + partial_sum if tree.acc_size <= 100000 else partial_sum

    def find_min_dir(self, tree, cur_min, target):
        if tree.acc_size < target:
            return cur_min
        if tree.children != None:
            for subdir in tree.children:
                cur_min = min(cur_min, self.find_min_dir(subdir, cur_min, target))
        return min(cur_min, tree.acc_size)
