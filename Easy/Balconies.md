# Balconies

You are trying to determine which of two apartments has a larger balcony. Both balconies are rectangles, and you have the length and width, but you need the area.

## Task 
Evaluate the area of two different balconies and determine which one is bigger.

## Input Format 
Your inputs are two strings where the measurements for height and width are separated by a comma. The first one represents apartment A, the second represents apartment B.

## Output Format: 
A string that says whether apartment A or apartment B has a larger balcony.

Sample Input 
```
'5,5'
'2,10'
```

Sample Output 
```Apartment A```

***Explanation***<br/> 
Since the area of apartment A's balcony is 25 and the area of apartment B's balcony is 20, Apartment A is the correct answer.


```python
height_A, width_A = input().split(',')
height_B, width_B = input().split(',')

area_A = float(height_A) * float(width_A)
area_B = float(height_B) * float(width_B)

if area_A > area_B: 
    print('Apartment A')
elif area_A == area_B:
    pass # ? this case is not considered in the problem formulation
else:
    print('Apartment B')
```
