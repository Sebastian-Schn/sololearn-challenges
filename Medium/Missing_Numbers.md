# Missing Numbers
You are given a list of whole numbers in ascending order. You need to find which numbers are missing in the sequence.

## Task: 
Create a program that takes in a list of numbers and outputs the missing numbers in the sequence separated by spaces.

## Input Format: 
The first input denotes the length of the list (N). The next N lines contain the list elements as integers. 

## Output Format: 
A string containing a space-separated list of the missing numbers.

## Sample Input: 
```5
2
4
5
7
8```

## Sample Output: 
```3 6```

***Explanation:***<br/> 
The input list is missing the numbers 3 and 6.


```python
#
```


```python
N = int(input())
S = {int(input())}
for i in range(1, N):
    S.add(int(input() ) )
T = set(range(min(S), max(S) + 1)) # Let T be the set \{min(S), ..., max(S)\}

D = list(T.difference(S)) # D := T \setminus S
D.sort()
print(' '.join(str(x) for x in D))
```
