# AdventOfCode2024

This is my attempt at [Advent of Code 2024](https://adventofcode.com/2024/about).

Also included is a single sample run time for each solution (using the [codetiming](https://github.com/realpython/codetiming) library), the time complexity, and the space complexity.

For the space complexity the reading of the input file is not included, and instead only the complexity of the solution is considered.

## Advent Progress

| Advent Stage |                                      Solution Link                                       | Run Time (seconds) |   Time Complexity    | Space Complexity |
|:------------:|:----------------------------------------------------------------------------------------:|:------------------:|:--------------------:|:----------------:|
|    Day 1     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/A-day-1/part-1.py)  |      0.00226       |     $O(n\log n)$     |      $O(n)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/A-day-1/part-2.py)  |      0.00215       |        $O(n)$        |      $O(n)$      |
|    Day 2     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/B-day-2/part-1.py)  |      0.00305       |       $O(nm)$        |     $O(nm)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/B-day-2/part-2.py)  |      0.00995       |      $O(nm^2)$       |     $O(nm)$      |
|    Day 3     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/C-day-3/part-1.py)  |      0.00169       |        $O(n)$        |      $O(n)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/C-day-3/part-2.py)  |      0.00183       |        $O(n)$        |      $O(n)$      |
|    Day 4     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/D-day-4/part-1.py)  |      0.02613       |       $O(hw)$        |      $O(1)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/D-day-4/part-2.py)  |      0.01883       |       $O(hw)$        |      $O(1)$      |
|    Day 5     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/E-day-5/part-1.py)  |      0.00435       |      $O(np^2)$       |      $O(1)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/E-day-5/part-2.py)  |      0.00979       |      $O(np^2)$       |     $O(p^2)$     |
|    Day 6     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/F-day-6/part-1.py)  |      0.00441       |       $O(hw)$        |     $O(hw)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/F-day-6/part-2.py)  |      9.71691       |     $O(h^2w^2)$      |     $O(hw)$      |
|    Day 7     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/G-day-7/part-1.py)  |      0.08309       |       $O(nm)$        |      $O(m)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/G-day-7/part-2.py)  |      5.61981       |       $O(nm)$        |      $O(m)$      |
|    Day 8     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/H-day-8/part-1.py)  |      0.00108       |     $O(h^2w^2)$      |     $O(hw)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/H-day-8/part-2.py)  |      0.00189       | $O(h^2w^2\max(h,w))$ |     $O(hw)$      |
|    Day 9     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/I-day-9/part-1.py)  |      0.01419       |        $O(n)$        |      $O(1)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/I-day-9/part-2.py)  |      2.85318       |       $O(n^3)$       |      $O(1)$      |
|    Day 10    | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/J-day-10/part-1.py) |      0.00547       |     $O(h^2w^2)$      |     $O(hw)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/J-day-10/part-2.py) |      0.00491       |     $O(h^2w^2)$      |     $O(hw)$      |
|    Day 11    | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/K-day-11/part-1.py) |      0.00215       |      $O(2^kn)$       |      $O(k)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/K-day-11/part-2.py) |      0.08929       |      $O(2^kn)$       |      $O(k)$      |
|    Day 12    | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/L-day-12/part-1.py) |      0.02908       |       $O(hw)$        |     $O(hw)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/L-day-12/part-2.py) |      0.04146       |       $O(hw)$        |     $O(hw)$      |
|    Day 13    | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/M-day-13/part-1.py) |      0.00251       |        $O(n)$        |      $O(1)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/M-day-13/part-2.py) |      0.00292       |        $O(n)$        |      $O(1)$      |
|    Day 14    | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/N-day-14/part-1.py) |      0.00946       |        $O(n)$        |      $O(1)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/N-day-14/part-2.py) |      1.27681       |        $O(n)$        |      $O(1)$      |
|    Day 15    | [Part 1](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/O-day-15/part-1.py) |      0.00846       | $O(hw + m\max(h,w))$ |      $O(1)$      |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2024/blob/master/O-day-15/part-2.py) |      0.01871       |       $O(mhw)$       |     $O(hw)$      |
|    Day 16    |                                                                                          |                    |                      |                  |
|              |                                                                                          |                    |                      |                  |
|    Day 17    |                                                                                          |                    |                      |                  |
|              |                                                                                          |                    |                      |                  |
|    Day 18    |                                                                                          |                    |                      |                  |
|              |                                                                                          |                    |                      |                  |
|    Day 19    |                                                                                          |                    |                      |                  |
|              |                                                                                          |                    |                      |                  |
|    Day 16    |                                                                                          |                    |                      |                  |
|              |                                                                                          |                    |                      |                  |
|    Day 21    |                                                                                          |                    |                      |                  |
|              |                                                                                          |                    |                      |                  |
|    Day 22    |                                                                                          |                    |                      |                  |
|              |                                                                                          |                    |                      |                  |
|    Day 23    |                                                                                          |                    |                      |                  |
|              |                                                                                          |                    |                      |                  |
|    Day 24    |                                                                                          |                    |                      |                  |
|              |                                                                                          |                    |                      |                  |
|    Day 25    |                                                                                          |                    |                      |                  |
|              |                                                                                          |                    |                      |                  |
