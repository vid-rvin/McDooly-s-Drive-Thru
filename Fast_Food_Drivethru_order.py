
def welcome():
    print("Welcome to McDooly's! Here's the Drive Thru Menu")
    print(
    '''
    1 - 🍔 Cheesburger
    2 - 🍟 Fries
    3 - 🥤 Soda
    4 - 🍦 Ice Cream
    5 - 🍪 Cookie
    '''
    )
def get_item(x):
    if x == 1:
        return "🍔 Cheesburger"
    elif x == 2:
        return "🍟 Fries"
    elif x == 3:
        return "🥤 Soda"
    elif x == 4:
        return "🍦 Ice Cream"
    elif x == 5:
        return "🍪 Cookie"
    else:
        return "Invalid input"  

welcome()
x = int(input("What do you want to order?:"))
print(get_item(x))
