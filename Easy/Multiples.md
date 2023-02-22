# Multiples

You need to calculate the sum of all the multiples of 3 or 5 below a given number.

## Task: 
Given an integer number, output the sum of all the multiples of 3 and 5 below that number. 
If a number is a multiple of both, 3 and 5, it should appear in the sum only once.

## Input Format: 
An integer.

## Output Format: 
An integer, representing the sum of all the multiples of 3 and 5 below the given input.

## Sample Input: 
```10```

## Sample Output:
```23```

***Explanation:***<br/> 
The numbers below 10 that are multiples of 3 or 5 are 3, 5, 6 and 9.
The sum of these numbers is 3+5+6+9=23


```python
import numpy as np

n = int(input())

# Calculate the highest multiple of 3 and 5 below n
highest_mult_of_3_below_n = n // 3 if n % 3 != 0 else (n // 3) - 1
highest_mult_of_5_below_n = n // 5 if n % 5 != 0 else (n // 5) - 1 


# Generate a list of multiples of 3 and 5 below n
multiples_of_3 = [i*3 for i in range(1, highest_mult_of_3_below_n+1)]
multiples_of_5 = [i*5 for i in range(1, highest_mult_of_5_below_n+1)]

# Since if a number is a multiple of both, 3 and 5, it should appear in the sum only once:
multiples_set = set(multiples_of_3).union(multiples_of_5)

print(np.sum(list(multiples_set)))
```
