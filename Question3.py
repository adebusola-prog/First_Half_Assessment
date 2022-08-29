shopping_cart = {"stationary":{"pencil" : 1, "notebooks": 5, "ruler": 19}, 
                  "foodstuffs":{"Bournvita": 3, "soymilk": 9, "cornflakes": 12},
                  "toileteries":{"diapers":4, "tissuepaper":15, "facetowel":1}}

def remove_shopping_items(data):
    shopping_cart["stationary"].pop("pencil")
    return(shopping_cart)

print(remove_shopping_items(shopping_cart))

def add_shopping_item():
    shopping_cart.setdefault("beauty")
    print(shopping_cart)
    shopping_cart["beauty"] = "cream, perfume"
    return(shopping_cart)

print(add_shopping_item())

def update_item():
    shopping_cart["toileteries"]["diapers"] = 5
    return(shopping_cart)

print(update_item())

