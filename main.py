# python 10th homework!!!!!!!!!!!!!!
from functools import reduce

#დავალება1: გამოიყენეთlambda ფუნქცია sorted() ფუნქციაში, იმისათვის რომ დაასორტიროს მოცემული
# ლისტი: [(1, 3), (4, 2), (2, 5)] - მასში არსებული ელემენტების მეორე ელემენტის მიხედვით
lst = [(1, 3), (4, 2), (2, 5)]
new_lst = list(sorted(lst, key=lambda x : x[1]))
print(new_lst)





# დავალება2:  დაწერეთ ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს ორ რიცხვს და პირველ რიცხვს გაყოფს მეორე რიცხვზე და დააბრუნებს შედეგს,
# დაიჭირეთ ორი ერორი: ის რომ მომხმარებელმა ინტეჯერები შეიყვანოს და ნულზე რომ არ შეიძლება გაყოფა, თითოეული ერორისთვის გამოუტანეთ
# შესაბამისი შეტყობინება. (ორივე ერორი უნდა იყოს შესაბამისი ერორებით დაჭერილი, არ გამოიყენოთ ზოგადი იქსეფშენი)
def division(num1, num2):
    result = num1 / num2
    return result

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = division(num1, num2)

except ZeroDivisionError:
    print("can't divide by zero")

except ValueError:
    print("insert only Integers")

except Exception as e:
    print(e)

else:
    print(result)

finally:
    print("end of a program")


# დავალება3: მოცემულია პროდუქტების ლისტი:
# filter() ფუნქციის გამოყენებით გაფილტრეთ და გამოიტანეთ პროდუქტები, რომლის ფასი ნაკლებია 100-ზე;
# map() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის სახელი და ფასი
# sorted() ფუნქციის გამოყენებით დაასორტირეთ პროდუქტების სია ფასის მიხედვით
# reduce() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის ფასების ჯამი

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

# filter() ფუნქციის გამოყენებით გაფილტრეთ და გამოიტანეთ პროდუქტები, რომლის ფასი ნაკლებია 100-ზე;
expensive = list(filter(lambda x : x["price"] < 100, products))
print(expensive)

# map() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის სახელი და ფასი
name_and_price = list(map(lambda x : (x["name"], x["price"]), products))
print(name_and_price)

# sorted() ფუნქციის გამოყენებით დაასორტირეთ პროდუქტების სია ფასის მიხედვით
price = list(sorted(products, key=lambda x : x["price"]))
print(price)

# reduce() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის ფასების ჯამი
total_price = reduce(lambda x, y: x + y["price"], products, 0)
print(total_price)






#  # დავალება4: დაწერეთ რეკურსიული ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და დააბრუნებს 1-დან ამ რიცხვის ჩათვლით ყველა რიცხვის ჯამს
def my_func(n):
     if n == 0 or n == 1:
        return n
     else:
         return n + my_func(n - 1)
print(my_func(int(input("Enter a number: "))))









