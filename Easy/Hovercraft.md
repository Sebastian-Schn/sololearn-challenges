# Hovercraft
You run a hovercraft factory. Your factory makes ten hovercrafts in a month. Given the number of customers you got that month, did you make a profit? It costs you 2,000,000 to build a hovercraft, and you are selling them for 3,000,000. You also pay 1,000,000 each month for insurance.

## Task: 
Determine whether or not you made a profit based on how many of the ten hovercrafts you were able to sell that month.
 
## Input Format: 
An integer that represents the sales that you made that month.

## Output Format: 
A string that says 'Profit', 'Loss', or 'Broke Even'.

## Sample Input: 
```5```

## Sample Output: 
```Loss```

**Explanation**<br />
If you only sold 5 hovercrafts, you spent 21,000,000 to operate but only made 15,000,000.


```python
n_customers = int(input())
cost             = 2*10e6
price            = 3*10e5
running_expenses = 10e5

total = n_customers * price - (cost + running_expenses)

if total <0:
    print('Loss')
elif total > 0:
    print('Profit')
else:
    print('Broke Even')
```
