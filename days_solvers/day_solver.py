from abc import ABC, abstractmethod
import os


class DaySolver(ABC):
    def solve(self, part):
        self.load_input()
        solve_impl = getattr(self, f"solve_part_{part}")
        return solve_impl()

    def load_input(self):
        file_path = os.path.join("inputs", self.get_input_filename())
        with open(file_path) as f:
            input_data = [int(val) for val in f]
        self.input_data = input_data

    def get_input_filename(self):
        return f"day_{self.day}.txt"

    @abstractmethod
    def solve_part_1(self):
        pass

    @abstractmethod
    def solve_part_2(self):
        pass
