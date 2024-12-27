# you are building an inventory management system
# for a small store
inventory = {
'A001':{
    'Name': "Laptop",
    'Description': "The laptop is core i9, 2024",
    'Price': 256,
    'Stock': 50
},
'A002':{
    'Name': "smartphone",
    'Description': "The smartphone is in Iphone",
    'Price': 500,
    'Stock': 199
},
'A003':{
    'Name': "Book",
    'Description': "the book is a cooler",
    'Price': 399,
    'Stock': 299
},

}

item_code = 'A002'
print(F'Price : {inventory[item_code]['Price']}')

inventory[item_code]['Price'] -= 2 #
print(f'{inventory[item_code]['Price']}')