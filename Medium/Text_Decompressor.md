# Text Decompressor

You need to decompress text. The compressed version has a number next to each symbol/letter, representing the amount of time that symbol should appear. 
For example, a2b3 is the compressed version of aabbb

## Task: 
Write a program that takes the compressed text as input and outputs the decompressed version.

## Input Format: 
A single string with letters/symbols, each followed by a number.

## Output Format: 
A string, representing the decompressed text.

## Sample Input: 
```k2&4b1```

## Sample Output: 
```kk&&&&b```

***Explanation:*** The letter k appears 2 times, the symbol & - 4 times and the letter b - 1 time.


```python
word = input()

decompressed_word = ''
for i in range(0, len(word), 2):
    decompressed_word += word[i] * int(word[i+1])
print(decompressed_word)
```
