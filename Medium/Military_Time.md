# Military Time

You want to convert the time from a 12 hour clock to a 24 hour clock. If you are given the time on a 12 hour clock, you should output the time as it would appear on a 24 hour clock.  

## Task:  
Determine if the time you are given is AM or PM, then convert that value to the way that it would appear on a 24 hour clock.

## Input Format: 
A string that includes the time, then a space and the indicator for AM or PM.

## Output Format: 
A string that includes the time in a 24 hour format (XX:XX)

## Sample Input: 
```1:15 PM```

## Sample Output: 
```13:15```

***Explanation:***<br/>
1:00 PM on a 12 hour clock is equivalent to 13:00 on a 24 hour clock.


```python
time, ampm = input().split()
hour, minute = time.split(":")
hour = int(hour)
if ampm == "PM":
    hour = 12 if hour == 12 else hour + 12
else:
    hour = 0 if hour == 12 else hour
print("{:02d}:{:02d}".format(hour, int(minute)))
```
