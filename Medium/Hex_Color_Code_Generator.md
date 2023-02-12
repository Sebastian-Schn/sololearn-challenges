# Hex Color Code Generator

You are starting a new company and unfortunately that means you can no longer rely on the free hex-color code software you used to rely on. It’s time to put your skills to the test and create one from the ground up!

## Task: 
Create a function that accepts three integers that represent the RGB (red, green, blue) values and outputs the hex-code representation.

## Input Format: 
Three integers that represent RGB values.

## Output Format: 
The hexadecimal color code string that corresponds with the entered RGB values.

## Sample Input: 
```100 
200 
233```

## Sample Output: 
```#64c8e9```

***Explanation:**<br/> 
Hex color codes work within 15 characters, 0-9 and a-f. RGB goes into hex color codes as such # (red) 00 (green) 00 (blue) 00. Hex color codes work by rolling over the value of 09 to 0a. Once 0f is hit (15) the following value (16) would be represented as 10 instead of (16). This means the RGB values (16, 32, 161) would evaluate to #1020a1 (10, 20, a1).



```python
R = int(input())
G = int(input())
B = int(input())

print('#' + f'{R:x}' + f'{G:x}' + f'{B:x}')
```

*using an inbuilt conversion function feels like cheating: hence:*


```python
import string

R = int(input())
G = int(input())
B = int(input())

def dec_to_hex(n):
    "input a decimal number, output the respective hexadecimal number"
    hex_dict = dict(zip(range(10, 16), string.ascii_lowercase[:6])) # dict "translating" a $10 \leq n \leq 16$ to it's hex. digit
    remainders = []
    while (n>0):
        temp = n % 16
        if temp >= 10:
            temp = hex_dict[temp]        
        remainders.append(str(temp))
        n//= 16
    n_hex = ''
    for remainder in remainders[::-1]:
        n_hex += remainder
    return(n_hex)

print('#' + dec_to_hex(R) + dec_to_hex(G) + dec_to_hex(B))
```
