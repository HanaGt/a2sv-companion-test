# List-Comprehensions

**Problem:** [List-Comprehensions](https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true)

---

![HackerRank Logo](https://hrcdn.net/fcore/assets/brand/logo-new-white-green-a5cb16e0ae.svg)
 ?
Let's learn about list comprehensions! You are given three integers ? and ? representing the dimensions of a cuboid along with an integer ?. Print a list of all possible coordinates given by ? on a 3D grid where the sum of ? is not equal to ?. Here, ?. Please use list comprehensions rather than multiple loops, as a learning exercise.
**Example**
 ?
 ?
 ?
 ?
All permutations of ? are:
?.
Print an array of the elements that do not sum to ?.
?
**Input Format**
 ?
Four integers ? and ?, each on a separate line.
**Constraints**
 ?
Print the list in lexicographic increasing order.
**Sample Input 0**
 ?
```
1
1
1
2
```
**Sample Output 0**
 ?
```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```
**Explanation 0**
 ?
Each variable ? and ? will have values of ? or ?. All permutations of lists in the form ?.
Remove all arrays that sum to ? to leave only the valid permutations.
**Sample Input 1**
 ?
```
2
2
2
2
```
**Sample Output 1**
 ?
```
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
```
Change Theme
 Language
Pypy 3
 ?
?
?
 More ?
1
2
3
4
5
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
Line: 5 Col: 21
Submit Code
Run Code
Upload Code as File
 ?
Test against custom input
