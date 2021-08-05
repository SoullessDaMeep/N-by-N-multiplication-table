The code before the beauty session:
```py
def multiTableNxN(n):
    new_row = []
    for col in range(1, n+1, 1):
        for row in range(1, n+1, 1):
                new_row.append(row * col)
        print(new_row)
        new_row = []

multiTableNxN(12)
```
