## Solutions for :christmas_tree: [Advent of Code 2022](https://adventofcode.com/2022)

My second attempt to AoC. As previously in [Aoc2021](https://github.com/Oyoshi/advent-of-code-2021) all solutions are written in [Python](https://www.python.org/) :snake:. 
During this time I spent some time on learning Python concepts and was trying to write code with the spirit of [Tacit Programming](https://en.wikipedia.org/wiki/Tacit_programming) :trollface:.
### Map

TODO

### Framework

I've created complete framework for running and benchmarking AoC 2022 solutions. All options are listed below:

```
options:
  -h, --help               show this help message and exit
  -d [1-25], --day [1-25]  day of AoC
  -p [1-2], --part [1-2]   part of the AoC day
  -b int, --benchmark int  compute benchmarks
```
Time stats for the benchmark will be measured for all solutions with given number of trials.

There are also Unit Tests which cover basic scenarios described in the example part of each task. Each commit triggers GA pipeline and run all UTs.

### Benchmark

|        | Part 1  &mu; [ms] | Part 1  &sigma; [ms] | Part 2  &mu; [ms] | Part 2  &sigma; [ms] |
| ------ | ------  | ------ |  ------ |  ------ |
| Day 01 | 0.00 | 0.00 |  0.10 | 0.32 |
| Day 02 | 0.32 | 0.32 |  0.70 | 0.48 |
| Day 03 | 0.52 | 0.52 |  0.20 | 0.42 |
| Day 04 | 0.42 | 0.42 |  0.30 | 0.48 |
| Day 05 | 0.01 | 0.01 |  3.20 | 0.42 |
| Day 06 | 0.48 | 0.48 |  1.70 | 0.48 |
| Day 07 | 0.42 | 0.42 |  0.70 | 0.49 |
| Day 08 | 0.31 | 0.31 |  8.00 | 0.01 |
| Day 09 | 0.92 | 0.92 |  22.00 | 1.49 |
| Day 10 | 0.00 | 0.00 |  0.10 | 0.32 |
| Day 11 | 0.52 | 0.52 |  316.22 | 16.49 |
| Day 12 | 1.13 | 1.13 |  1278.42 | 15.01 |
| Day 13 | 0.52 | 0.52 |  10.30 | 0.48 |
| Day 14 | 0.82 | 0.82 |  1886.14 | 82.18 |
| Day 15 | 325.31 | 325.31 |  19694.50 | 346.43 |
