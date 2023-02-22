## Task:
Count the number of ones in the binary representation of a given integer.

## Input Format:
An integer.

## Output Format: 
An integer representing the count of ones in the binary representation of the input.

## Sample Input:
```9```

## Sample Output:
```2```

***Explanation:***<br/> 
The binary representation of 9 is 1001, which includes 2 ones.


```python
n = int(input())
n_binary = bin(n)[2:]

print(n_binary.count('1'))
```
