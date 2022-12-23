from days_solvers import DaySolver
from utils import sum_iterable


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.guard = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.guard == None:
            self.guard = Node(None)
            self.guard.next = node
            node.prev = self.guard
            self.guard.prev = node
            node.next = self.guard
        else:
            last_node = self.guard.prev
            last_node.next = node
            node.prev = last_node
            node.next = self.guard
            self.guard.prev = node
        self.size += 1

    def move_by_offset(self):
        iterator_source = self.guard.next
        current_idx = 0
        while iterator_source.data != None and iterator_source.data[1] == True:
            iterator_source = iterator_source.next
            current_idx += 1
        if iterator_source.data[0] == 0:
            iterator_source.data[1] = True
            return
        target_idx = self.compute_target_index(current_idx, iterator_source.data[0])
        iterator_target = self.guard.next
        idx = 0
        while iterator_target.data != None and idx < target_idx:
            iterator_target = iterator_target.next
            idx += 1
        iterator_source.prev.next = iterator_source.next
        iterator_source.next.prev = iterator_source.prev
        after_target = iterator_target.next
        iterator_target.next = iterator_source
        iterator_source.prev = iterator_target
        iterator_source.next = after_target
        after_target.prev = iterator_source
        iterator_source.data[1] = True

    def compute_target_index(self, idx, offset):
        target = idx + offset
        if target <= 0:
            return (self.size + target - 1) % (self.size - 1)
        return target % self.size

    def index_of(self, val):
        iterator = self.guard.next
        idx = 0
        while iterator.data[0] != val:
            iterator = iterator.next
            idx += 1
        return idx

    def values_at(self, targets):
        iterator = self.guard.next
        greatest_idx = sorted(targets)[len(targets) - 1]
        nums = []
        idx = 0
        while idx <= greatest_idx:
            if idx in targets:
                nums.append(iterator.data[0])
            iterator = iterator.next
            idx += 1
        return nums

    def to_string(self):
        iterator = self.guard.next
        while iterator.data != None:
            print(iterator.data, end=" ")
            iterator = iterator.next


class Day20Solver(DaySolver):
    def __init__(self):
        self.day = "20"

    def load_input_impl(self, file):
        return [int(line.rstrip()) for line in file]

    def solve_part_1(self):
        print(self.input_data)
        linked_list = LinkedList()
        for v in self.input_data:
            linked_list.append([v, False])
        already_moved = 0
        while already_moved < linked_list.size:
            linked_list.move_by_offset()
            already_moved += 1
        idx_of_zero = linked_list.index_of(0)
        indices = [
            linked_list.compute_target_index(idx_of_zero, (i + 1) * 1000)
            for i in range(3)
        ]
        return sum_iterable(linked_list.values_at(indices))

    def solve_part_2(self):
        pass
