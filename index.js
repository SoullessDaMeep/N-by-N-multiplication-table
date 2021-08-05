function multiTableNxN(n) {
    let new_row = ""
    for(let col = 1; col < n+1; col++) {
        for(let row = 1; row < n+1; row++) {
            if(row * col < 10) {
                new_row += row * col + "   "
            }
            else if(row * col >= 10 && row * col < 99) {
                new_row += row * col + "  "
            }
            else { 
                new_row += row * col + " "
            }
        }
        console.log(new_row)
        new_row = []
    }
}
multiTableNxN(12)
