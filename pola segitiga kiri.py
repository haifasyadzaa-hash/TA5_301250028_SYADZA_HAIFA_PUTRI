#2. Pola segitiga kiri
tinggi = 5 
   
for i in range(tinggi): 
    for j in range(tinggi - i - 1):
        print("  ", end="")
    for k in range(2*i + 1):
       print("*", end="") 
    print()