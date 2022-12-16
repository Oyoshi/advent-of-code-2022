from days_solvers import DaySolver


class Day16Solver(DaySolver):
    def __init__(self):
        self.day = "16"

    def load_input_impl(self, file):
        return self.create_graph([line.rstrip().split() for line in file])

    def create_graph(self, inp):
        adj_list = {}
        rates = {data[1]: int(data[4].split("=")[1].rstrip(";")) for data in inp}
        for data in inp:
            cur_node = data[1]
            from_cur = (
                data[data.index("valves") + 1 :]
                if "valves" in data
                else data[data.index("valve") + 1 :]
            )
            from_cur = list(map(lambda n: n.rstrip(","), from_cur))
            adj_list[cur_node] = {
                "flow": rates[cur_node],
                "tunnels": from_cur,
            }
        return adj_list

    def solve_part_1(self):
        src = "AA"
        paths = self.scan_space_using_bfs(src)
        return self.find_max_flow(paths, set([src]), 0, src, 29, 0)

    def scan_space_using_bfs(self, src):
        paths = {}
        vertices = sorted(
            [
                x
                for x in list(self.input_data.keys())
                if x == src or self.input_data[x]["flow"] != 0
            ]
        )
        for v1 in vertices:
            paths[v1] = {}
            for v2 in vertices:
                if v1 != v2:
                    paths[v1][v2] = self.bfs(v1, v2)
        return paths

    def bfs(self, src, target):
        time_cost = 1
        stop = False
        neighbours = self.input_data[src]["tunnels"]
        while not stop:
            new_neighbours = set()
            for v in neighbours:
                if v == target:
                    stop = True
                    break
                new_neighbours |= set(self.input_data[v]["tunnels"])
            neighbours = new_neighbours
            time_cost += 1
        return time_cost - 1

    def find_max_flow(self, paths, opened, flow, v, time_left, current_max):
        current_max = max(flow, current_max)

        if time_left <= 0:
            return current_max

        if v not in opened:
            current_max = self.find_max_flow(
                paths,
                opened.union([v]),
                flow + self.input_data[v]["flow"] * time_left,
                v,
                time_left - 1,
                current_max,
            )
        else:
            current_max = max(
                current_max,
                max(
                    [
                        self.find_max_flow(
                            paths,
                            opened,
                            flow,
                            vv,
                            time_left - paths[v][vv],
                            current_max,
                        )
                        for vv in paths[v].keys()
                        if vv not in opened
                    ],
                    default=-1,
                ),
            )
        return current_max

    def solve_part_2(self):
        pass
