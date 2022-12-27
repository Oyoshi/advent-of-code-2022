class Node:
    def __init__(self, cur_dir):
        self.dir = cur_dir
        self.files_size = 0
        self.acc_size = 0
        self.children = None
        self.parent = None

    def add_subdir(self, dir_name):
        subdir = Node(dir_name)
        subdir.parent = self
        self.children = self.children + [subdir] if self.children else [subdir]
