# Credit Card Validator
You need to verify if the given credit card number is valid. For that you need to use the Luhn test.

Here is the Luhn formula:
1. Reverse the number.
2. Multiple every second digit by 2. 
3. Subtract 9 from all numbers higher than 9.
4. Add all the digits together.
5. Modulo 10 of that sum should be equal to 0. 

## Task: 
Given a credit card number, validate that it is valid using the Luhn test. Also, all valid cards must have exactly 16 digits.

## Input Format:
A string containing the credit card number you need to verify.

## Output Format:
A string: 'valid' in case the input is a valid credit card number (passes the Luhn test and is 16 digits long), or 'not valid', if it's not.

## Sample Input:
```4091131560563988```

## Sample Output:
```valid```

**Explanation:** Let's run the Luhn test for our input:  
Reverse: **8893650651311904**  
Multiplying the even positions by 2: **8 16 9 6 6 10 0 12 5 2 3 2 1 18 0 8**  
Subtract 9 from >9: **8 7 9 6 6 1 0 3 5 2 3 2 1 9 0 8**  
The sum: **70**  
70 Modulo 10 is **0**.  
The input passed the Luhn test and contains 16 digits, making it a valid credit card number.


```python
n = input()
def Luhn(n):
    '''Returns True, False, when Luhn test is fullfilled, not fulfilled, respectively'''
    n_list_rev = [int(digit) for digit in n[::-1]]
    for i in range(0,len(n_list_rev)):
        if i % 2 == 1: # note that due to 0-indexing "even" positions are "odd" positions and vice versa
            n_list_rev[i] *= 2
        if n_list_rev[i] > 9:
            n_list_rev[i] -= 9
    if sum(n_list_rev) % 10 == 0:
        return True
    else:
        return False

if len(n) == 16 and Luhn(n):
    print('valid')
else:
    print('not valid')
```
