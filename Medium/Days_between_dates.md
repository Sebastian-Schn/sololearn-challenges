# Days between dates

You need to calculate exactly how many days have passed between two dates.

## Task:  
Calculate how many days have passed between two input dates, and output the result. 

## Input Format: 
Two strings that represent the dates, first date should be the older date. 
Date format: Month DD, YYYY

## Output Format: 
A number representing the number of days between the two dates.

## Sample Input: 
```August 15, 1979
June 15, 2018 ```

## Sample Output: 
```14184```

***Explanation:***<br/> 
14184 days have passed between the two input days.


```python
from datetime import datetime

date_from = datetime.strptime(input(), "%B %d, %Y")
date_till = datetime.strptime(input(), "%B %d, %Y")
days_betw = date_till - date_from
print(days_betw.days)
```
