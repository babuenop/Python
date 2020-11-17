# Los rangos se definen como:
#   range(comienzo, fin, pasos)

my_range  = range (1,5)
type(my_range)
for i in my_range:
    print(i)

print("Rango2")

my_range  = range (0,8,2)
type(my_range)
for i in my_range:
    print(i)

print(id(my_range))
