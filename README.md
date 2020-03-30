# 15-Puzzle Solver using Branch and Bound
Making a solver for 15-puzzle using Branch and Bound algorithm with python


### Compile and Running
Can run in both Windows and Linux
1. Open main.py at src directory 
1. Change the file test on `line 172` into filename at test directory ex: `solve1.txt` 
1. Open Command Prompt and go to src directory
1. type `python main.py`


### File Structure
```
│   README.md
│
├───docs
│       Tucil3StrAlgo_Laporan_13518024
├───src
│       main.py
│
└───test
        solve1.txt
        solve2.txt
        solve3.txt
        unsolve1.txt
        unsolve2.txt
```

### Input
txt file that have 4x4 size of numbers from 0 - 15
```
1 2 3 4
5 6 7 8
9 10 11 0 
13 14 15 12
```

### Output
- Initial Matrix
- Empty space(0) at 
- Fungsi Kurang(i)
- Sum of fungsi Kurang(i) + X value
- Tell if the puzzle solvable or unsolvable 
- Time needed to run the algorithm
- How Many node that is pushed into queue

## Acknowledgement
This project is made to fulfill IF2211 Algorithm and Strategy assignment.
Created By : Jovan Karuna Cahyadi 