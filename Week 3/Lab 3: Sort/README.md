# Lab 3: Sort

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 3 - Lab 3: Sort](https://cs50.harvard.edu/x/2023/labs/3/). In the "Sorting Algorithms Analysis" lab, you are provided with three compiled C programs: `sort1`, `sort2`, and `sort3`. Your task is to analyze these programs and determine which sorting algorithm each program implements. The sorting algorithms in question are selection sort, bubble sort, and merge sort. You will use various input data files to assess the behavior and performance of each sorting algorithm.

## Getting Started

To get started with the lab, follow these steps:

1. **Download the Source Code**: Download the source code for the lab using the provided link and extract the contents of the ZIP file. You will find three compiled executable files named `sort1`, `sort2`, and `sort3`.

2. **Navigate to the Lab Directory**: Open a terminal and navigate to the directory where the executable files are located. You can do this by using the `cd` command.

   ```
   cd path/to/sort-directory
   ```

3. **Analyze Sorting Algorithms**: Run each of the sorting programs on different input data files to observe their behavior and performance. Use the provided input data files to assess how each sorting algorithm handles reversed, shuffled, and sorted lists.

   For example, to sort the reversed list of 10000 numbers using `sort1`, run:

   ```
   ./sort1 reversed10000.txt
   ```

   You can also time the execution of each sorting program using the `time` command:

   ```
   time ./sort1 reversed10000.txt
   ```

4. **Record Your Observations**: As you analyze each sorting program, record your observations and conclusions in the `answers.txt` file. Fill in the blanks marked as TODO with your explanations for each program.

## Sorting Algorithm Analysis

Here are the conclusions drawn from analyzing the provided sorting programs:

- `sort1` uses: Bubble Sort

  **How do you know?**: The sorting process took longer compared to other sorting algorithms, indicating that it might be bubble sort, which has higher time complexity.

- `sort2` uses: Merge Sort

  **How do you know?**: The sorting process is relatively faster than `sort1` and `sort3`, which is an indicator of merge sort's efficient performance.

- `sort3` uses: Selection Sort

  **How do you know?**: While `sort3` is not as fast as `sort2` (merge sort), it still sorts the numbers faster than `sort1` (bubble sort), suggesting that it might be selection sort.

## Hints

- The characteristics of different types of input data files (reversed, shuffled, sorted) can provide insights into the behavior of each sorting algorithm.

- Observe how each sorting algorithm performs on various input data scenarios, such as already sorted lists, reversed lists, and shuffled lists.