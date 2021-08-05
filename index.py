def multiTableNxN(n):
    new_row = []
    for col in range(1, n+1, 1):
        for row in range(1, n+1, 1):
            #spacing numbers for better look

            #single digit spacing
            if row * col < 10:
            #appending row number * column number, 1 * 1, 1 * 2 ..., 1 * 12, 2 * 1 ..., ...,
                new_row.append(str(row * col) + "   ")
            #double digit spacing
            elif row * col >= 10 and row * col < 100:
                new_row.append(str(row * col) + "  ")
            #triple digit spacing
            else:
                new_row.append(str(row * col) + " ")
        print(new_row)
        #setting the new row to nothing to add new numbers
        new_row = []

multiTableNxN(12)
