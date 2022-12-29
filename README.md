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

Benchmark for `N=10` trials are shown below:

|        | Part 1  &mu; [ms] | Part 1  &sigma; [ms] | Part 2  &mu; [ms] | Part 2  &sigma; [ms] |
| ------ | ------  | ------ |  ------ |  ------ |
| Day 01 | 2.19 | 2.19 |  0.00 | 0.00 |
| Day 02 | 0.01 | 0.01 |  0.70 | 0.48 |
| Day 03 | 0.48 | 0.48 |  0.40 | 0.52 |
| Day 04 | 0.00 | 0.00 |  0.40 | 0.52 |
| Day 05 | 0.32 | 0.32 |  3.30 | 0.47 |
| Day 06 | 0.00 | 0.00 |  1.70 | 0.68 |
| Day 07 | 0.49 | 0.49 |  0.99 | 0.02 |
| Day 08 | 0.79 | 0.79 |  8.71 | 2.26 |
| Day 09 | 0.97 | 0.97 |  22.42 | 1.77 |
| Day 10 | 0.00 | 0.00 |  0.10 | 0.32 |
| Day 11 | 5.51 | 5.51 |  292.75 | 7.33 |
| Day 12 | 4.65 | 4.65 |  1243.59 | 8.52 |
| Day 13 | 0.52 | 0.52 |  10.30 | 0.48 |
| Day 14 | 0.93 | 0.93 |  1746.82 | 9.71 |
| Day 15 | 166.60 | 166.60 |  19660.58 | 249.94 |
| Day 16 | 14.01 | 14.01 |  210661.89 | 3507.71 |
| Day 17 | 4.52 | 4.52 |  200.32 | 11.03 |
| Day 18 | 4.54 | 4.54 |  363.99 | 1.76 |
| Day 19 | 7.50 | 7.50 |  601.02 | 2.80 |
| Day 20 | 1.97 | 1.97 |  1943.20 | 10.79 |
| Day 21 | 0.52 | 0.52 |  3.00 | 1.15 |
| Day 22 | 0.62 | 0.62 |  9.81 | 0.63 |
| Day 23 | 7.28 | 7.28 |  29561.37 | 483.43 |
| Day 24 | 19.43 | 19.43 |  4213.97 | 31.95 |
| Day 25 | 0.00 | 0.00 |  0.00 | 0.00 |
