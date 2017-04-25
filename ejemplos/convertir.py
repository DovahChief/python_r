#el 12 lo encontre haciendo pruebas
print ("conversion de 4134.9018 -> ",
 4134.9018/(2**12) )

print("regresando  (1.009497509765625) * (2**12) = " ,
 (1.009497509765625) * (2**12)  )

print("binario de la potencia -> {0:b}".
format(127+12)  )

i = 0
x = 2 * ((4134.9018/(2**12)) % 1)

while i < 23:
    print("BIT -> ", i ," -> ", x)
    if x>1:
        x = x % 1
    x = x * 2
    i = i +1