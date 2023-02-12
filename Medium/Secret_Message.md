# Secret Message

You are trying to send a secret message, and you've decided to encode it by replacing every letter in your message with its corresponding letter in a backwards version of the alphabet. 
What do your messages look like?

## Task: 
Create a program that replaces each letter in a message with its corresponding letter in a backwards version of the English alphabet.

## Input Format: 
A string of your message in its normal form.

## Output Format: 
A string of your message once you have encoded it (all lower case).

## Sample Input: 
```Hello World```

## Sample Output: 
```svool dliow```

***Explanation:***<br/>
If you replace each letter in 'Hello World' with the corresponding letter in a backwards version of the alphabet, you get 'svool dliow'.


```python
import string

message = input().lower()
abc = string.ascii_lowercase
zyx = abc[::-1]
abc_dict = dict(zip(abc, zyx)) # dict "translating" a letter to its backwards version
abc_dict[' '] = ' '            # whitespace <-> whitespace

secret_message = ''
for ch in message:
    secret_message += abc_dict[ch]
print(secret_message)
```
