x = [0,0,0,0,0,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,1,1,0]
sum , y  = 0, 1;
for n in x:
    sum = sum + (n / (2** y))
    y = y + 1
print("Decimal -> ", sum)
print("resultado -> ", 1*( (sum+1) *(2**12) ) )