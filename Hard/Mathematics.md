# Mathematics
Find which math expression matches the answer that you are given, if you have an integer answer, and a list of math expressions.

## Task: 
Test each math expression to find the first one that matches the answer that you are given.

## Input Format: 
Two inputs: an integer and a space separated string of math expressions. The following operations need to be supported: addition +, subtraction -, multiplication *, division /. 
An expression can include multiple operations.

## Output Format: 
A string that tells the index of the first math expression that matches. If there are no matches, output 'none'.

## Sample Input: 
```
15
(2+100) (5*3) (14+1)
```

## Sample Output: 
```index 1```

**Explanation:**<br/> 
Index counting starts at 0, so '**(5*3)**' is at index 1 and matches your answer of **15**.


```python
n            = int(input())
expressions  = input()
lexpressions = expressions.split() # all expressions in one list
nexpressions = len(expressions.split()) # the number of expressions

i = 0
while True:
    if i+1 == nexpressions:
        print("none")
        break
    elif eval(lexpressions[i]) == n:
        print("index " + str(i))
        break
    i+=1
```
