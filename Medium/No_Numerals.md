# No Numerals

You write a phrase and include a lot of number characters (0-9), but you decide that for numbers 10 and under you would rather write the word out instead. Can you go in and edit your phrase to write out the name of each number instead of using the numeral? 

## Task: 
Take a phrase and replace any instances of an integer from 0-10 and replace it with the English word that corresponds to that integer.

## Input Format: 
A string of the phrase in its original form (lowercase).

## Output Format: 
A string of the updated phrase that has changed the numerals to words.

## Sample Input: 
```i need 2 pumpkins and 3 apples```

## Sample Output: 
```i need two pumpkins and three apples```

***Explanation:***<br/>
You would update the phrase to change '2' to 'two' and '3' to 'three'.


```python
message = input()

numerals = list(range(0,10))
numerals.insert(0, 10) # otherwise, below 10 would be replaced by onezero, this is far from ideal.
words    = ['ten', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num_dict = dict(zip(numerals, words))

for i in numerals:
    message = message.replace(str(i), num_dict[i])
print(message)
```
