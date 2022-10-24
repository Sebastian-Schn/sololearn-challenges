# Camel to Snake
The company you are working for is refactoring its entire codebase. It's changing all naming conventions from camel to snake case (camelCasing to snake_casing). 
Every capital letter is replaced with its lowercase prefixed by an underscore _, except for the first letter, which is lowercased without the underscore, so that SomeName becomes some_name.

## Task: 
Write a program that takes in a string that has camel casing, and outputs the same string but with snake casing.

## Input Format: 
A string with camelCasing.

## Output Format: 
The same string but with snake_casing.

## Sample Input: 
```camelCasing```

## Sample Output:
```camel_casing```

**Explanation:**  
The capital C was lowercased and prefixed by an underscore.


```python
import re

wordCamel = input()
wordCamelStart = wordCamel[0].lower() # first letter lowercase w/o the underscore
wordCamelEnd = wordCamel[1:]

capitals = set(re.findall(r"[A-Z]", wordCamelEnd))
for letter in capitals:
    wordCamelEnd = re.sub(letter, r"_" + letter.lower(),  wordCamelEnd)
print(wordCamelStart + wordCamelEnd)
```

### Alternatively:


```python
wordCamel = [*input()]
wordCamel[0] = wordCamel[0].lower() # first letter lowercase w/o the underscore
for i in range(1, len(wordCamel)):
    if wordCamel[i].isupper():
        wordCamel[i] = r'_' + wordCamel[i].lower()
print(''.join(wordCamel))
```
