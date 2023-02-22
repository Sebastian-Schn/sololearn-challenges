# Isogram Detector

An isogram is a word that has no repeating letters, whether they are consecutive or non-consecutive.  
Your job is to find a way to detect if a word is an isogram.

***Task:*** Write a program that takes in a string as input, detects if the string is an isogram and outputs true or false based on the result.
 
## Input Format: 
A string containing one word.

## Output Format: 
A string: true or false.

## Sample Input: 
```turbulence```

## Sample Output: 
```false```

***Explanation:***<br/> 
The word turbulence has multiple "u" and "e" in it, which would mean it is not an isogram.


```python
word = input()
letters_in_word = set()

def isogram(word):
    for letter in word:
        if letter in letters_in_word:
            return('false')
        else:
            letters_in_word.add(letter)
    return('true')

print(isogram(word))
```
