car_brands=[]
for i in range(5):
    car_brands1=input("BMW", "Mersedes", "Lamborgini", "Mitsubishi", "Pagani")
    car_brands.append(car_brands1)
print(car_brands)
car_brands.pop(4)
print(car_brands)
print(len(car_brands))
print(car_brands.index("lamborgini"))
