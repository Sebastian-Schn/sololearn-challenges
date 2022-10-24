# Longest Common Substring
## Task:
Given multiple words, you need to find the longest string that is a substring of all words. 

## Input Format:
A string of words, separated by spaces. The string can also contain numbers.

## Output Format:
A string, representing the longest common substring. 
If there are multiple longest common substrings, output the smallest one in alphabetical order.

## Sample Input:
```SoloLearn Learning LearningIsFun Learnable```

## Sample Output:
```Learn```

**Explanation:**  
Learn is the longest common substring for the words SoloLearn Learning LearningIsFun Learnable.


```python
words = input().split(' ')
j=0
first_word = words[0]
rest_words = words[1:]
potential_list = []

while j < len(first_word):
    i = j + 1
    if all(first_word[j] in word for word in words): # letter firstword[j] in all words?
        while i < len(first_word) + 1 and all(first_word[j:i+1] in word for word in rest_words):
            i += 1
        #print(first_word[j:i])
        potential_list.append(first_word[j:i])
        if i < len(first_word) and all(first_word[j+1:i+1] in word for word in rest_words): 
            # Let i \in len(first_words) and 0 < j < i such that first_word[j:i] in each word in rest_words
            # but first_word[j:i+1] not in every word in rest word. It is possible that each word in rest_words
            # contains first_word[j+1:i+1], if that is the case, we need to include it.
            potential_list.append(first_word[j+1:i+1])
    j = i
print(max(potential_list, key=len))
```

*Note that this algorithm could be much improved wrt. number of necessary operations. For instance,
as soon as we find a substring $s$ in each word with $len(s) > 1$, we only have to consider matches of
$len(s)$ or more. For the current case the algorithm above provided suffices however, since the number of words
and length of each word is small.*
