from abc import ABC, abstractmethod
import os
import time


class DaySolver(ABC):
    def solve(self, part, benchmark=False):
        self.input_data = self.load_input()
        solve_impl = getattr(self, f"solve_part_{part}")
        if benchmark:
            start = time.process_time()
        res = solve_impl()
        if benchmark:
            end = time.process_time()
            return {"time": end - start, "val": res}
        return {"time": None, "val": res}

    def load_input(self):
        file_path = os.path.join("inputs", self.get_input_filename())
        with open(file_path) as f:
            input_data = [int(val) for val in f]
        return input_data

    def get_input_filename(self):
        return f"day_{self.day}.txt"

    @abstractmethod
    def solve_part_1(self):
        pass

    @abstractmethod
    def solve_part_2(self):
        pass
