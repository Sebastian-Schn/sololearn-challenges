# Duct Tape

You want to completely cover a flat door on both sides with duct tape. You need to know how many rolls of duct tape to buy when you go to the store.

## Task: 
Given the height and width of the door, determine how many rolls of duct tape you will need (a roll of duct tape is 60 feet long and 2 inches wide and there are 12 inches in each foot). Don't forget both sides of the door!

## Input Format: 
Two integers that represent the height and width of the door.

## Output Format: 
An integer that represents the total rolls of duct tape that you need to buy.

## Sample Input: 
```7
4```

## Sample Output: 
```6```

***Explanation***<br/>
You will need 6 rolls of duct tape to cover both sides of a 7ft x 4ft door.


```python
import numpy as np

width, height = float(input()), float(input())
tape_needed   = width * height * 2 # cover door front- and backside
roll_area     = 60 * 2 / 12
rolls_needed  = int(np.ceil(tape_needed / roll_area))
print(rolls_needed)
```
