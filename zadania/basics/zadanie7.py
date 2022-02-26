my_height = 174
my_weight = 70
user_height = float(input("Podaj swój wzrost: "))
user_weight = float(input("Podaj swoją wagę: "))
bmi = user_weight / user_height ** 2
print(bmi)