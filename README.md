Python

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

JavaScript

The code before the beauty session:
```js
function multiTableNxN(n) {
    let new_row = ""
    for(let col = 1; col < n+1; col++) {
        for(let row = 1; row < n+1; row++) {
            new_row += row * col + " "
        }
        console.log(new_row)
        new_row = []
    }
}
multiTableNxN(12)
```
