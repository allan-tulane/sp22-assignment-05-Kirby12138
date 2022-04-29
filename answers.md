# CMPS 2200 Assignment 5
## Answers

**Name:**_________Dachen Ni________________


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.**
The greedy algorithm would always pick the largest coin available that is smallar than remaining money.

For example, if you got 100 dollars, the greedy algorithm would first pick 64, which is the largest coin less than 100. Then, there are 36 remaining so it will pick 32 as it's the biggest coin less than 36. Finally, there are 4 remaining and the algorithm will pick four. And the result is 3 coins.



- **1b.**
The work and span would both be O(logn).


- **2a.**

The algorithm doesn't work optimally because the denomiators are arbitrary now.
An example that it fails will be you got 8 dollar and the available choices are 1, 4, and 5. Optimally you would pick two four dollars, which is 2 coins. However, the greedy algorithm will pick one five dollar and three one dollar, resulting in 4 coins.

- **2b.**

By using memorization to avoiding recomputation, the work would be the number of nodes of DAG, O(n * w). The span would be the longest path in DAG, which is O(n).


