# Day of the Week
You receive a date and need to know what day of the week it is. 
 
## Task: 
Create a program that takes in a string containing a date, and outputs the day of the week.

## Input Format: 
A string containing a date in either "MM/DD/YYYY" format or "Month Day, Year" format.

## Output Format: 
A string containing the day of the week from the provided date.

## Sample Input: 
```11/19/2019```

## Sample Output: 
```Tuesday```

**Explanation:** <br/> 
19 November 2019 is a Tuesday.


```python
import datetime

date = input()
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
try:
    i = datetime.datetime.strptime(date, "%m/%d/%Y").weekday()
except ValueError:
    i = datetime.datetime.strptime(date, "%B %d, %Y").weekday()
print(weekdays[i])
```
