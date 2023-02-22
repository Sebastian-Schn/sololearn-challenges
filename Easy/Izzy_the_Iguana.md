# Izzy the Iguana

Your pet Iguana has run away, and you found it up in a tree! It will come down right away if you brought the right snacks, but if you don't have enough, you will have to wait. You need 10 total snack points to bring it down. Lettuce is worth 5, Carrot is worth 4, Mango is worth 9, and Cheeseburger is worth 0.

## Task: 
Evaluate whether or not you have enough snack points to convince your iguana to come down.

## Input Format: 
Your input is a string that represents the snacks that you have. Snacks are separated by spaces, you can have any number of snacks, and they can repeat.

## Output Format: 
A string that says 'Come on Down!' if you have enough points, or 'Time to wait' if you do not. 

## Sample Input: 
```Mango Cheeseburger Carrot```

Sample Output:
```Come on Down!```

***Explanation:***<br/> 
You have 13 snack points with a mango, cheeseburger, and carrot, which is enough to convince the iguana to come down.


```python
points = {'Lettuce': 5,
          'Carrot': 4,
          'Mango': 9,
          'Cheeseburger': 0}
          
snacks = input().split()
total_points = sum(points.get(snack) for snack in snacks)

print('Come on Down!' if total_points >= 10 else 'Time to wait')
```
