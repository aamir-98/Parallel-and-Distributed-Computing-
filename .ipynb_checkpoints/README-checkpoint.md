# DSAI3202  
## Work Environment for the Parallel and Distributed Computing Course

---

## Question 1: Overview of the Automated Maze Explorer

The maze explorer in this project employs a fundamental navigation strategy known as the **right-hand rule**. This method simulates how a person might navigate a maze by keeping their right hand in contact with the wall at all times. At every junction, the explorer prioritizes available directions in the following order:

- **Turn Right**
- **Move Straight Ahead**
- **Turn Left**
- **Backtrack** (if no other option is available)

To prevent getting caught in repetitive loops, the explorer monitors its three most recent moves. If it detects a recurring pattern (for example, three consecutive right turns), it deduces that it is trapped and activates a backtracking routine. This routine leverages a record of previously visited cells to retrace its steps effectively.

At the end of each exploration, the explorer provides these key metrics:
- **Total Duration:** 0.0025 seconds  
- **Total Moves Made:** 1279 moves  
- **Backtracking Operations:** 0  
- **Average Speed:** 633055.80

For instance, one trial showed that the explorer navigated the maze in 1279 moves without any backtracking, completing the task in just 0.0025 seconds. Although the algorithm is straightforward, its robust performance makes it highly effective for maze navigation.

---

## Question 2: Executing Multiple Explorers Concurrently

To enhance the exploration process, a function was developed to allow a single maze explorer to operate on the static maze and return performance data (moves, time, and backtracks). Python’s `multiprocessing` module was then used to execute **four explorers** concurrently.

Each explorer followed the same logic, with all of them eventually completing the maze in 1279 moves without needing any backtracking. The minor differences in execution time (measured in milliseconds) can be attributed to the operating system’s task scheduling during parallel processing.

### Experimental Results

| Explorer | Moves | Backtracks | Time (s) |
|----------|-------|------------|----------|
| 1        | 494   | 0          | 0.0021   |
| 2        | 563   | 0          | 0.0023   |
| 3        | 92    | 0          | 0.0020   |
| 4        | 1279  | 0          | 0.0022   |

These results confirm that while the pathfinding algorithm remains robust, slight timing differences can occur due to the nature of multiprocessing.

---

## Question 3: Performance Evaluation of Explorers

In further testing, all four explorers were run concurrently on the same static maze while detailed performance data was collected concerning moves, execution time, and backtracking frequency.

**Key Observations:**
- **Uniformity in Moves:** Every explorer completed the maze in exactly 1279 moves, demonstrating the method's consistency.
- **Zero Backtracking:** The absence of any backtracking reinforces the efficiency of the right-hand rule.
- **Timing Variations:** Slight differences in execution time are likely due to the operating system's scheduling of processes.

Bar charts were generated to illustrate these performance metrics, clearly noting that no backtracking occurred.

### Summary Table

| Explorer | Moves | Backtracks | Time (s) |
|----------|-------|------------|----------|
| 1        | 1279  | 0          | 0.0023   |
| 2        | 1279  | 0          | 0.0029   |
| 3        | 1279  | 0          | 0.0042   |
| 4        | 1279  | 0          | 0.0021   |

While all explorers followed the same path without backtracking, the minor timing differences are attributed to the parallel processing overhead. Testing on more complex maze configurations is recommended for further performance evaluation.

---

## Question 4: Upgrading the Maze Explorer

The original maze explorer, based on the right-hand rule, can sometimes follow inefficient routes due to its lack of goal awareness. To address this, a new method, `bfs_solve()`, was added to the Explorer class. This method utilizes the **Breadth-First Search (BFS)** algorithm to systematically explore all possible routes and guarantee the shortest path in grid-like mazes.

**Advantages of the BFS Approach:**
- **Goal Awareness:** The explorer now identifies the exit’s exact location.
- **Minimized Turns:** Unnecessary directional changes and loops are reduced.
- **Shortest Path Guarantee:** BFS finds the optimal route without requiring backtracking.
- **Enhanced Efficiency:** The BFS approach operates more quickly than the right-hand rule.

Testing on the static maze demonstrated a significant improvement: the BFS-based explorer solved the maze in only 128 moves, compared to 1279 moves using the original method.

---

## Question 5: Comparing the Enhanced Explorer (BFS) to the Original

A direct comparison was made between the right-hand rule-based explorer and the newly enhanced BFS-based explorer on the same static maze. The results are summarized below:

| **Algorithm**      | **Moves** | **Backtracks** | **Time (s)** |
|--------------------|-----------|----------------|--------------|
| Right-Hand Rule    | 1279      | 0              | ~0.0025      |
| BFS                | 128       | 0              | 0.0013       |

The data clearly demonstrates that the BFS algorithm identifies a much shorter route (128 moves versus 1279 moves) while both approaches avoid backtracking. However, BFS is significantly more efficient due to its goal-aware design.

### Trade-Offs

- **Right-Hand Rule:**
  - *Pros:* Simple and effective in environments where the exit’s position is unknown.
  - *Cons:* Can lead to longer routes even when the exit is nearby.
- **BFS:**
  - *Pros:* Guarantees the shortest path by being goal-aware and operates more efficiently.
  - *Cons:* Requires complete knowledge of the maze layout before execution.

Given these considerations, the BFS approach is the superior solution when the full maze structure is available, providing a quicker and more direct path to the exit.

---