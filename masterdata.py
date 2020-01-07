from app import appbuilder, db
from app.models import VendorGroup, ProductGroup, ProductSubGroup, ProductSubSubGroup, Interests, Interests, SecurityLevel
from datetime import datetime
import logging
import random
from app.models import InterestsProductsubsubgroup

# role_admin = appbuilder.sm.find_role(appbuilder.sm.auth_role_admin)

# user1 = appbuilder.sm.add_user(
#     "vern", "Vern", "Fetter", "vernf10@live.com", role_admin, "princeton20"
# )

# db.session.merge(user1)
# db.session.commit()

# Security Level
try:
    db.session.add(SecurityLevel(name="Administrator")) # ID: 1
    db.session.add(SecurityLevel(name="Sub-Administrator")) # ID: 2
    db.session.add(SecurityLevel(name="Vendor User")) # ID: 3
    db.session.add(SecurityLevel(name="Vendor Site User")) # ID: 4
    db.session.add(SecurityLevel(name="Frontend User")) # ID: 5
    db.session.commit()
except:
    db.session.rollback()

# Vendor Groups
try:
    db.session.add(VendorGroup(name="CDs, DVDs and Games")) # ID: 1
    db.session.add(VendorGroup(name="Electronics")) # ID: 2
    db.session.add(VendorGroup(name="Hypermarket")) # ID: 3
    db.session.add(VendorGroup(name="Supermarket")) # ID: 4
    db.session.commit()
except:
    db.session.rollback()

# Interests
try:
    db.session.add(Interests(interest="Business and Industry")) # ID: 1
    db.session.add(Interests(interest="Entertainment")) # ID: 2
    db.session.add(Interests(interest="Family and Relationships")) # ID: 3
    db.session.add(Interests(interest="Fitness and Wellness")) # ID: 4
    db.session.add(Interests(interest="Food and Drink")) # ID: 5
    db.session.add(Interests(interest="Hobbies and Activities")) # ID: 6
    db.session.add(Interests(interest="Fashion")) # ID: 7
    db.session.add(Interests(interest="Sports and Outdoors")) # ID: 8
    db.session.add(Interests(interest="Technology")) # ID: 9
    db.session.commit()
except:
    db.session.rollback()

# Product Groups
try:
    db.session.add(ProductGroup(name="Drinks")) # ID: 1
    db.session.add(ProductGroup(name="Food")) # ID: 2
    db.session.add(ProductGroup(name="Household")) # ID: 3
    db.session.add(ProductGroup(name="Health and Beauty")) # ID: 4
    db.session.add(ProductGroup(name="Baby")) # ID: 5
    db.session.add(ProductGroup(name="Sport")) # ID: 6
    db.session.add(ProductGroup(name="Outdoor")) # ID: 7
    db.session.add(ProductGroup(name="Pets")) # ID: 8
    db.session.add(ProductGroup(name="Toys")) # ID: 9
    db.session.add(ProductGroup(name="Clothing and Footwear")) # ID: 10
    db.session.add(ProductGroup(name="Electronics")) # ID: 11
    db.session.add(ProductGroup(name="Gifts")) # ID: 12
    db.session.commit()
except:
    db.session.rollback()

# Product Sub-Groups (Drinks - ID: 1)
try:
    db.session.add(ProductSubGroup(productsubgroup_name="Soft Drinks", product_group_id=1)) # ID: 1
    db.session.add(ProductSubGroup(productsubgroup_name="Juices and Smoothies", product_group_id=1)) # ID: 2
    db.session.add(ProductSubGroup(productsubgroup_name="Bottled Water", product_group_id=1)) # ID: 3
    db.session.add(ProductSubGroup(productsubgroup_name="Squash, Concentrates and Cordials", product_group_id=1)) # ID: 4
    db.session.add(ProductSubGroup(productsubgroup_name="Kids and Lunchbox Drinks", product_group_id=1)) # ID: 5
    db.session.add(ProductSubGroup(productsubgroup_name="Sports and Energy Drinks", product_group_id=1)) # ID: 6
    db.session.add(ProductSubGroup(productsubgroup_name="Tea", product_group_id=1)) # ID: 7
    db.session.add(ProductSubGroup(productsubgroup_name="Dairy Drinks", product_group_id=1)) # ID: 8
    db.session.add(ProductSubGroup(productsubgroup_name="Coffee", product_group_id=1)) # ID: 9
    db.session.add(ProductSubGroup(productsubgroup_name="Hot Drinks", product_group_id=1)) # ID: 10
    db.session.add(ProductSubGroup(productsubgroup_name="Beer and Cider", product_group_id=1)) # ID: 11
    db.session.add(ProductSubGroup(productsubgroup_name="Wine", product_group_id=1)) # ID: 12
    db.session.add(ProductSubGroup(productsubgroup_name="Spirits and Liquers", product_group_id=1)) # ID: 13
    db.session.add(ProductSubGroup(productsubgroup_name="Spirit Coolers", product_group_id=1)) # ID: 14
    db.session.add(ProductSubGroup(productsubgroup_name="Soda and Tonic Water", product_group_id=1)) # ID: 15
    db.session.add(ProductSubGroup(productsubgroup_name="Non-Alcoholic Beverages", product_group_id=1)) # ID: 16
    db.session.commit()
except:
    db.session.rollback()

# Product Sub-Sub-Groups (Drinks - ID: 1)
try:
    # Soft Drinks
    db.session.add(ProductSubSubGroup(name="Cola", product_group_id=1, product_sub_group_id=1)) # ID: 1
    db.session.add(ProductSubSubGroup(name="Diet and Sugar Free Soft Drinks", product_group_id=1, product_sub_group_id=1)) # ID: 2
    db.session.add(ProductSubSubGroup(name="Flavoured Soft Drinks", product_group_id=1, product_sub_group_id=1)) # ID: 3
    db.session.add(ProductSubSubGroup(name="Lemonade and Ginger Ale", product_group_id=1, product_sub_group_id=1)) # ID: 4
    # Juices and Smoothies
    db.session.add(ProductSubSubGroup(name="Boxed Fruit Juice", product_group_id=1, product_sub_group_id=2)) # ID: 5
    db.session.add(ProductSubSubGroup(name="Coconut Water and Aloe Juice", product_group_id=1, product_sub_group_id=2)) # ID: 6
    db.session.add(ProductSubSubGroup(name="Fresh Fruit Juice", product_group_id=1, product_sub_group_id=2)) # ID: 7
    db.session.add(ProductSubSubGroup(name="Fresh Smoothies", product_group_id=1, product_sub_group_id=2)) # ID: 8
    db.session.add(ProductSubSubGroup(name="Kids Juice and Smoothies", product_group_id=1, product_sub_group_id=2)) # ID: 9
    db.session.add(ProductSubSubGroup(name="Tomato and Vegetable Juice", product_group_id=1, product_sub_group_id=2)) # ID: 10
    # Bottled Water
    db.session.add(ProductSubSubGroup(name="Sparkling Water", product_group_id=1, product_sub_group_id=3)) # ID: 11
    db.session.add(ProductSubSubGroup(name="Flavoured Water", product_group_id=1, product_sub_group_id=3)) # ID: 12
    db.session.add(ProductSubSubGroup(name="Still Water", product_group_id=1, product_sub_group_id=3)) # ID: 13
    # Squash, Concentrates and Cordials
    db.session.add(ProductSubSubGroup(name="Cordials", product_group_id=1, product_sub_group_id=4)) # ID: 14
    db.session.add(ProductSubSubGroup(name="Flavoured Syrups", product_group_id=1, product_sub_group_id=4)) # ID: 15
    db.session.add(ProductSubSubGroup(name="Fruit Concentrates", product_group_id=1, product_sub_group_id=4)) # ID: 16
    db.session.add(ProductSubSubGroup(name="Fruit Squash", product_group_id=1, product_sub_group_id=4)) # ID: 17
    db.session.add(ProductSubSubGroup(name="Soda Syrups", product_group_id=1, product_sub_group_id=4)) # ID: 18
    # Kids and Lunchbox Drinks
    db.session.add(ProductSubSubGroup(name="Kids and Lunchbox Juice Cartons", product_group_id=1, product_sub_group_id=5)) # ID: 19
    db.session.add(ProductSubSubGroup(name="Kids and Lunchbox Drink Pouches", product_group_id=1, product_sub_group_id=5)) # ID: 20
    db.session.add(ProductSubSubGroup(name="Kids and Lunchbox Drink Bottles", product_group_id=1, product_sub_group_id=5)) # ID: 21
    db.session.add(ProductSubSubGroup(name="Kids Water", product_group_id=1, product_sub_group_id=5)) # ID: 22
    # Sports and Energy Drinks
    db.session.add(ProductSubSubGroup(name="Sports Drinks", product_group_id=1, product_sub_group_id=6)) # ID: 23
    db.session.add(ProductSubSubGroup(name="Energy Drinks", product_group_id=1, product_sub_group_id=6)) # ID: 24
    db.session.add(ProductSubSubGroup(name="Wellbeing Drinks", product_group_id=1, product_sub_group_id=6)) # ID: 25
    # Tea
    db.session.add(ProductSubSubGroup(name="Ceylon Tea", product_group_id=1, product_sub_group_id=7)) # ID: 26
    db.session.add(ProductSubSubGroup(name="Decaf Tea", product_group_id=1, product_sub_group_id=7)) # ID: 27
    db.session.add(ProductSubSubGroup(name="Earl Gray Tea", product_group_id=1, product_sub_group_id=7)) # ID: 28
    db.session.add(ProductSubSubGroup(name="Fruit and Herbal Tea", product_group_id=1, product_sub_group_id=7)) # ID: 29
    db.session.add(ProductSubSubGroup(name="Green Tea", product_group_id=1, product_sub_group_id=7)) # ID: 30
    db.session.add(ProductSubSubGroup(name="Iced Tea", product_group_id=1, product_sub_group_id=7)) # ID: 31
    db.session.add(ProductSubSubGroup(name="Loose Leaf Tea", product_group_id=1, product_sub_group_id=7)) # ID: 32
    db.session.add(ProductSubSubGroup(name="Rooibos Tea", product_group_id=1, product_sub_group_id=7)) # ID: 33
    db.session.add(ProductSubSubGroup(name="Sleep, Detox and Added Benefits Tea", product_group_id=1, product_sub_group_id=7)) # ID: 34
    db.session.add(ProductSubSubGroup(name="Tea Creamer", product_group_id=1, product_sub_group_id=7)) # ID: 35
    db.session.add(ProductSubSubGroup(name="Tea Pods", product_group_id=1, product_sub_group_id=7)) # ID: 36
    db.session.add(ProductSubSubGroup(name="White Tea", product_group_id=1, product_sub_group_id=7)) # ID: 37
    # Dairy Drinks
    db.session.add(ProductSubSubGroup(name="Dairy Fruit Drinks", product_group_id=1, product_sub_group_id=8)) # ID: 38
    db.session.add(ProductSubSubGroup(name="Drinking Yoghurt", product_group_id=1, product_sub_group_id=8)) # ID: 39
    db.session.add(ProductSubSubGroup(name="Milkshakes", product_group_id=1, product_sub_group_id=8)) # ID: 40
    db.session.add(ProductSubSubGroup(name="Protein Shakes", product_group_id=1, product_sub_group_id=8)) # ID: 41
    # Coffee
    db.session.add(ProductSubSubGroup(name="Coffee Beans", product_group_id=1, product_sub_group_id=9)) # ID: 42
    db.session.add(ProductSubSubGroup(name="Coffee Creamer", product_group_id=1, product_sub_group_id=9)) # ID: 43
    db.session.add(ProductSubSubGroup(name="Coffee Filters", product_group_id=1, product_sub_group_id=9)) # ID: 44
    db.session.add(ProductSubSubGroup(name="Coffee Pods", product_group_id=1, product_sub_group_id=9)) # ID: 45
    db.session.add(ProductSubSubGroup(name="Decaf Coffee", product_group_id=1, product_sub_group_id=9)) # ID: 46
    db.session.add(ProductSubSubGroup(name="Ground Coffee", product_group_id=1, product_sub_group_id=9)) # ID: 47
    db.session.add(ProductSubSubGroup(name="Iced Coffee", product_group_id=1, product_sub_group_id=9)) # ID: 48
    db.session.add(ProductSubSubGroup(name="Instant Cappuccino, Latte and Mocha", product_group_id=1, product_sub_group_id=9)) # ID: 49
    db.session.add(ProductSubSubGroup(name="Instant Coffee", product_group_id=1, product_sub_group_id=9))  # ID: 50
    # Hot Drinks
    db.session.add(ProductSubSubGroup(name="Flavoured Hot Drinks", product_group_id=1, product_sub_group_id=10)) # ID: 51
    db.session.add(ProductSubSubGroup(name="Hot Chocolate", product_group_id=1, product_sub_group_id=10)) # ID: 52
    db.session.add(ProductSubSubGroup(name="Malted Hot Drinks", product_group_id=1, product_sub_group_id=10)) # ID: 53
    db.session.add(ProductSubSubGroup(name="Sugar Free Hot Drinks", product_group_id=1, product_sub_group_id=10)) # ID: 54
    db.session.add(ProductSubSubGroup(name="White Hot Chocolate", product_group_id=1, product_sub_group_id=10)) # ID: 55
    # Beer and Cider
    db.session.add(ProductSubSubGroup(name="Beer", product_group_id=1, product_sub_group_id=11)) # ID: 56
    db.session.add(ProductSubSubGroup(name="Cider", product_group_id=1, product_sub_group_id=11)) # ID: 57
    db.session.add(ProductSubSubGroup(name="Craft Beer", product_group_id=1, product_sub_group_id=11)) # ID: 58
    db.session.add(ProductSubSubGroup(name="Gluten Free Beer", product_group_id=1, product_sub_group_id=11)) # ID: 59
    db.session.add(ProductSubSubGroup(name="Stout", product_group_id=1, product_sub_group_id=11)) # ID: 60
    # Wine
    db.session.add(ProductSubSubGroup(name="Champagne and Sparkling Wine", product_group_id=1, product_sub_group_id=12)) # ID: 61
    db.session.add(ProductSubSubGroup(name="Red Wine", product_group_id=1, product_sub_group_id=12)) # ID: 62
    db.session.add(ProductSubSubGroup(name="Rose Wine", product_group_id=1, product_sub_group_id=12)) # ID: 63
    db.session.add(ProductSubSubGroup(name="White Wine", product_group_id=1, product_sub_group_id=12)) # ID: 64
    db.session.add(ProductSubSubGroup(name="Boxed Wine", product_group_id=1, product_sub_group_id=12)) # ID: 65
    db.session.add(ProductSubSubGroup(name="Sherry and Port", product_group_id=1, product_sub_group_id=12)) # ID: 66
    db.session.add(ProductSubSubGroup(name="Wine Gift Sets", product_group_id=1, product_sub_group_id=12)) # ID: 67
    # Spirits and Liquers
    db.session.add(ProductSubSubGroup(name="Brandy and Cognac", product_group_id=1, product_sub_group_id=13)) # ID: 68
    db.session.add(ProductSubSubGroup(name="Fortified Wine and Vermouth", product_group_id=1, product_sub_group_id=13)) # ID: 69
    db.session.add(ProductSubSubGroup(name="Gin", product_group_id=1, product_sub_group_id=13)) # ID: 70
    db.session.add(ProductSubSubGroup(name="Liqeurs and Speciality Spirits", product_group_id=1, product_sub_group_id=13)) # ID: 71
    db.session.add(ProductSubSubGroup(name="Premix Cocktails and Cocktail Ingredients", product_group_id=1, product_sub_group_id=13)) # ID: 72
    db.session.add(ProductSubSubGroup(name="Premix Shooters", product_group_id=1, product_sub_group_id=13)) # ID: 73
    db.session.add(ProductSubSubGroup(name="Rum", product_group_id=1, product_sub_group_id=13)) # ID: 74
    db.session.add(ProductSubSubGroup(name="Sambucca", product_group_id=1, product_sub_group_id=13)) # ID: 75
    db.session.add(ProductSubSubGroup(name="Spirits and Liqeurs Gifts", product_group_id=1, product_sub_group_id=13)) # ID: 76
    db.session.add(ProductSubSubGroup(name="Vodka", product_group_id=1, product_sub_group_id=13)) # ID: 77
    db.session.add(ProductSubSubGroup(name="Tequila", product_group_id=1, product_sub_group_id=13)) # ID: 78
    db.session.add(ProductSubSubGroup(name="Whisky", product_group_id=1, product_sub_group_id=13)) # ID: 79
    # Spirit Coolers
    # Soda and Tonic Water
    db.session.add(ProductSubSubGroup(name="Ginger Ale", product_group_id=1, product_sub_group_id=15)) # ID: 80
    db.session.add(ProductSubSubGroup(name="Soda Water", product_group_id=1, product_sub_group_id=15)) # ID: 81
    db.session.add(ProductSubSubGroup(name="Tonic Water", product_group_id=1, product_sub_group_id=15)) # ID: 82
    db.session.add(ProductSubSubGroup(name="Traditional Mixers", product_group_id=1, product_sub_group_id=15)) # ID: 83
    # Non-Alcoholic Beverages
    db.session.add(ProductSubSubGroup(name="Non-Alcoholic Beer", product_group_id=1, product_sub_group_id=16))  # ID: 84
    db.session.add(ProductSubSubGroup(name="Non-Alcoholic Spirit Coolers", product_group_id=1, product_sub_group_id=16))  # ID: 85
    db.session.add(ProductSubSubGroup(name="Non-Alcoholic Sparkling Wine", product_group_id=1, product_sub_group_id=16))  # ID: 86
    db.session.add(ProductSubSubGroup(name="Non-Alcoholic Wine", product_group_id=1, product_sub_group_id=16))  # ID: 87
    db.session.commit()
except:
    db.session.rollback()

# Product Sub-Groups (Food - ID: 2)
try:
    db.session.add(ProductSubGroup(productsubgroup_name="Fresh Food", product_group_id=2))  # ID: 17
    db.session.add(ProductSubGroup(productsubgroup_name="Frozen Food", product_group_id=2))  # ID: 18
    db.session.add(ProductSubGroup(productsubgroup_name="Bakery", product_group_id=2))  # ID: 19
    db.session.add(ProductSubGroup(productsubgroup_name="Food Cupboard", product_group_id=2))  # ID: 20
    db.session.add(ProductSubGroup(productsubgroup_name="Platters and Food Baskets", product_group_id=2))  # ID: 21
except:
    db.session.rollback()

# Product Sub-Groups (Food - ID: 2)
try:
    # Fresh Food
    db.session.add(ProductSubSubGroup(name="Fresh Fruit", product_group_id=2, product_sub_group_id=17))  # ID: 88
    db.session.add(ProductSubSubGroup(name="Fresh Vegetables", product_group_id=2, product_sub_group_id=17))  # ID: 89
    db.session.add(ProductSubSubGroup(name="Fresh Salad, Herbs and Dip", product_group_id=2, product_sub_group_id=17))  # ID: 90
    db.session.add(ProductSubSubGroup(name="Cheese", product_group_id=2, product_sub_group_id=17))  # ID: 91
    db.session.add(ProductSubSubGroup(name="Yoghurt", product_group_id=2, product_sub_group_id=17))  # ID: 92
    db.session.add(ProductSubSubGroup(name="Milk, Butter and Eggs", product_group_id=2, product_sub_group_id=17))  # ID: 93
    db.session.add(ProductSubSubGroup(name="Fresh and Chilled Desserts", product_group_id=2, product_sub_group_id=17))  # ID: 94
    db.session.add(ProductSubSubGroup(name="Cooked Meats, Sandwich Fillers and Deli", product_group_id=2, product_sub_group_id=17))  # ID: 95
    db.session.add(ProductSubSubGroup(name="Ready Meals", product_group_id=2, product_sub_group_id=17))  # ID: 96
    db.session.add(ProductSubSubGroup(name="Fresh Meat and Poultry", product_group_id=2, product_sub_group_id=17))  # ID: 97
    db.session.add(ProductSubSubGroup(name="Fresh Fish and Seafood", product_group_id=2, product_sub_group_id=17))  # ID: 98
    # Frozen Food
    db.session.add(ProductSubSubGroup(name="Frozen Vegetables", product_group_id=2, product_sub_group_id=18))  # ID: 99
    db.session.add(ProductSubSubGroup(name="Frozen Chips, Potatoes and Rice", product_group_id=2, product_sub_group_id=18))  # ID: 100
    db.session.add(ProductSubSubGroup(name="Frozen Fish and Seafood", product_group_id=2, product_sub_group_id=18))  # ID: 101
    db.session.add(ProductSubSubGroup(name="Frozen Meat and Poultry", product_group_id=2, product_sub_group_id=18))  # ID: 102
    db.session.add(ProductSubSubGroup(name="Frozen Vegetables and Meat Pies", product_group_id=2, product_sub_group_id=18))  # ID: 103
    db.session.add(ProductSubSubGroup(name="Frozen Pies and Party Food", product_group_id=2, product_sub_group_id=18))  # ID: 104
    db.session.add(ProductSubSubGroup(name="Frozen Pizza and Garlic Bread", product_group_id=2, product_sub_group_id=18))  # ID: 105
    db.session.add(ProductSubSubGroup(name="Frozen Ready Meals", product_group_id=2, product_sub_group_id=18))  # ID: 106
    db.session.add(ProductSubSubGroup(name="Frozen Fruit and Pastry", product_group_id=2, product_sub_group_id=18))  # ID: 107
    db.session.add(ProductSubSubGroup(name="Frozen Deserts, Ice Cream and Ice", product_group_id=2, product_sub_group_id=18))  # ID: 108
    # Bakery
    db.session.add(ProductSubSubGroup(name="Bread and Rolls", product_group_id=2, product_sub_group_id=19))  # ID: 109
    db.session.add(ProductSubSubGroup(name="Wraps, Pitas and Naan", product_group_id=2, product_sub_group_id=19))  # ID: 110
    db.session.add(ProductSubSubGroup(name="Muffins, Pancakes and Waffles", product_group_id=2, product_sub_group_id=19))  # ID: 111
    db.session.add(ProductSubSubGroup(name="Croissants, Scones and Pastries", product_group_id=2, product_sub_group_id=19))  # ID: 112
    db.session.add(ProductSubSubGroup(name="Doughnuts, Fresh Cookies and Iced Buns", product_group_id=2, product_sub_group_id=19))  # ID: 113
    db.session.add(ProductSubSubGroup(name="Cakes, Cupcakes and Tarts", product_group_id=2, product_sub_group_id=19))  # ID: 114
    # Food Cupboard
    db.session.add(ProductSubSubGroup(name="Biltong, Dried Fruit, Nuts and Seeds", product_group_id=2, product_sub_group_id=20))  # ID: 115
    db.session.add(ProductSubSubGroup(name="Biscuits, Cookies and Cereal Bars", product_group_id=2, product_sub_group_id=20))  # ID: 116
    db.session.add(ProductSubSubGroup(name="Canned Food", product_group_id=2, product_sub_group_id=20))  # ID: 117
    db.session.add(ProductSubSubGroup(name="Crackers and Crispbreads", product_group_id=2, product_sub_group_id=20))  # ID: 118
    db.session.add(ProductSubSubGroup(name="Chips, Snacks and Popcorn", product_group_id=2, product_sub_group_id=20))  # ID: 119
    db.session.add(ProductSubSubGroup(name="Breakfast Cereals, Porridge and Pap", product_group_id=2, product_sub_group_id=20))  # ID: 120
    db.session.add(ProductSubSubGroup(name="Sugar and Sweeteners", product_group_id=2, product_sub_group_id=20))  # ID: 121
    db.session.add(ProductSubSubGroup(name="Baking", product_group_id=2, product_sub_group_id=20))  # ID: 122
    db.session.add(ProductSubSubGroup(name="Chocolates and Sweets", product_group_id=2, product_sub_group_id=20))  # ID: 123
    db.session.add(ProductSubSubGroup(name="Desserts, Jellies and Custards", product_group_id=2, product_sub_group_id=20))  # ID: 124
    db.session.add(ProductSubSubGroup(name="Long Life Milk and Dairy Alternatives", product_group_id=2, product_sub_group_id=20))  # ID: 125
    db.session.add(ProductSubSubGroup(name="Spreads, Honey and Preserves", product_group_id=2, product_sub_group_id=20))  # ID: 126
    db.session.add(ProductSubSubGroup(name="Rice, Pasta, Noodles and Cous Cous", product_group_id=2, product_sub_group_id=20))  # ID: 127
    db.session.add(ProductSubSubGroup(name="Table Condiments and Dressings", product_group_id=2, product_sub_group_id=20))  # ID: 128
    db.session.add(ProductSubSubGroup(name="Cooking Ingredients", product_group_id=2, product_sub_group_id=20))  # ID: 129
    db.session.add(ProductSubSubGroup(name="Olives, Gherkins and Pickles", product_group_id=2, product_sub_group_id=20))  # ID: 130
    # Platters and Fruit Baskets
    db.session.add(ProductSubSubGroup(name="Fruit and Vegetable Platters", product_group_id=2, product_sub_group_id=21))  # ID: 131
    db.session.add(ProductSubSubGroup(name="Chicken and Poultry Platters", product_group_id=2, product_sub_group_id=21))  # ID: 132
    db.session.add(ProductSubSubGroup(name="Meat Platters", product_group_id=2, product_sub_group_id=21))  # ID: 133
    db.session.add(ProductSubSubGroup(name="Sweet and Dessert Platters", product_group_id=2, product_sub_group_id=21))  # ID: 134
    db.session.add(ProductSubSubGroup(name="Cocktail and Cheese Platters", product_group_id=2, product_sub_group_id=21))  # ID: 135
    db.session.add(ProductSubSubGroup(name="Mixed Platters", product_group_id=2, product_sub_group_id=21))  # ID: 136
    db.session.add(ProductSubSubGroup(name="Vegetarian and Vegan Platters", product_group_id=2, product_sub_group_id=21))  # ID: 137
    db.session.add(ProductSubSubGroup(name="Fruit Baskets", product_group_id=2, product_sub_group_id=21))  # ID: 138
except:
    db.session.rollback()

# Product Sub-Groups (Household - ID: 3)
try:
    db.session.add(ProductSubGroup(productsubgroup_name="Appliances", product_group_id=3))  # ID: 22
    db.session.add(ProductSubGroup(productsubgroup_name="Bathroom", product_group_id=3))  # ID: 23
    db.session.add(ProductSubGroup(productsubgroup_name="Bedroom", product_group_id=3))  # ID: 24
    db.session.add(ProductSubGroup(productsubgroup_name="Car", product_group_id=3))  # ID: 25
    db.session.add(ProductSubGroup(productsubgroup_name="Cleaning", product_group_id=3))  # ID: 26
    db.session.add(ProductSubGroup(productsubgroup_name="Decor", product_group_id=3))  # ID: 27
    db.session.add(ProductSubGroup(productsubgroup_name="DIY", product_group_id=3))  # ID: 28
    db.session.add(ProductSubGroup(productsubgroup_name="Electrical", product_group_id=3))  # ID: 29
    db.session.add(ProductSubGroup(productsubgroup_name="Kitchen", product_group_id=3))  # ID: 30
    db.session.add(ProductSubGroup(productsubgroup_name="Laundry", product_group_id=3))  # ID: 31
    db.session.add(ProductSubGroup(productsubgroup_name="Luggage and Travel", product_group_id=3))  # ID: 32
    db.session.add(ProductSubGroup(productsubgroup_name="Wool, Sewing and Needlework", product_group_id=3))  # ID: 33
    db.session.add(ProductSubGroup(productsubgroup_name="Stationary and Newsagent", product_group_id=3))  # ID: 34
except:
    db.session.rollback()

# Product Sub-Groups (Household - ID: 3)
try:
    # Appliances
    db.session.add(ProductSubSubGroup(name="Food Preperation Appliances", product_group_id=3, product_sub_group_id=22))  # ID: 139
    db.session.add(ProductSubSubGroup(name="Floorcare Appliances", product_group_id=3, product_sub_group_id=22))  # ID: 140
    db.session.add(ProductSubSubGroup(name="Health and Beauty Appliances", product_group_id=3, product_sub_group_id=22))  # ID: 141
    db.session.add(ProductSubSubGroup(name="Heating and Cooling Appliances", product_group_id=3, product_sub_group_id=22))  # ID: 142
    db.session.add(ProductSubSubGroup(name="Kitchen Appliances", product_group_id=3, product_sub_group_id=22))  # ID: 143
    db.session.add(ProductSubSubGroup(name="Ice Makers", product_group_id=3, product_sub_group_id=22))  # ID: 144
    db.session.add(ProductSubSubGroup(name="Party and Entertainments Appliances", product_group_id=3, product_sub_group_id=22))  # ID: 145
    # Bathroom
    db.session.add(ProductSubSubGroup(name="Bath and Toilet Mats", product_group_id=3, product_sub_group_id=23))  # ID: 146
    db.session.add(ProductSubSubGroup(name="Bathroom Accessories", product_group_id=3, product_sub_group_id=23))  # ID: 147
    db.session.add(ProductSubSubGroup(name="Bathroom Decor", product_group_id=3, product_sub_group_id=23))  # ID: 148
    db.session.add(ProductSubSubGroup(name="Bathroom Fittings", product_group_id=3, product_sub_group_id=23))  # ID: 149
    db.session.add(ProductSubSubGroup(name="Bathroom Furniture", product_group_id=3, product_sub_group_id=23))  # ID: 150
    db.session.add(ProductSubSubGroup(name="Shower Curtains", product_group_id=3, product_sub_group_id=23))  # ID: 151
    db.session.add(ProductSubSubGroup(name="Towels", product_group_id=3, product_sub_group_id=23))  # ID: 152
    # Bedroom
    db.session.add(ProductSubSubGroup(name="Bedding Sets", product_group_id=3, product_sub_group_id=24))  # ID: 153
    db.session.add(ProductSubSubGroup(name="Bedroom Curtains", product_group_id=3, product_sub_group_id=24))  # ID: 154
    db.session.add(ProductSubSubGroup(name="Bedroom Decor", product_group_id=3, product_sub_group_id=24))  # ID: 155
    db.session.add(ProductSubSubGroup(name="Bedroom Furniture", product_group_id=3, product_sub_group_id=24))  # ID: 156
    db.session.add(ProductSubSubGroup(name="Cushions and Pillows", product_group_id=3, product_sub_group_id=24))  # ID: 157
    db.session.add(ProductSubSubGroup(name="Duvet Inners, Throws and Blankets", product_group_id=3, product_sub_group_id=24))  # ID: 158
    db.session.add(ProductSubSubGroup(name="Duvet and Pillow Covers", product_group_id=3, product_sub_group_id=24))  # ID: 159
    db.session.add(ProductSubSubGroup(name="Sheets and Protectors", product_group_id=3, product_sub_group_id=24))  # ID: 160
    # Car
    db.session.add(ProductSubSubGroup(name="Auto Maintenance", product_group_id=3, product_sub_group_id=25))  # ID: 161
    db.session.add(ProductSubSubGroup(name="Battery Cables and Chargers", product_group_id=3, product_sub_group_id=25))  # ID: 162
    db.session.add(ProductSubSubGroup(name="Car Cleaning and Sun Care", product_group_id=3, product_sub_group_id=25))  # ID: 163
    db.session.add(ProductSubSubGroup(name="Car Covers and Mats", product_group_id=3, product_sub_group_id=25))  # ID: 164
    db.session.add(ProductSubSubGroup(name="Car Tools", product_group_id=3, product_sub_group_id=25))  # ID: 165
    db.session.add(ProductSubSubGroup(name="Motot Oil and Additives", product_group_id=3, product_sub_group_id=25))  # ID: 166
    # Cleaning
    db.session.add(ProductSubSubGroup(name="Bleach and Disinfectants", product_group_id=3, product_sub_group_id=26))  # ID: 167
    db.session.add(ProductSubSubGroup(name="Air Fresheners and Home Fragrance", product_group_id=3, product_sub_group_id=26))  # ID: 168
    db.session.add(ProductSubSubGroup(name="Buckets and Basins", product_group_id=3, product_sub_group_id=26))  # ID: 169
    db.session.add(ProductSubSubGroup(name="Brooms, Brushes and Mops", product_group_id=3, product_sub_group_id=26))  # ID: 170
    db.session.add(ProductSubSubGroup(name="Cleaning Protection and Wear", product_group_id=3, product_sub_group_id=26))  # ID: 171
    db.session.add(ProductSubSubGroup(name="Dishwashing", product_group_id=3, product_sub_group_id=26))  # ID: 172
    db.session.add(ProductSubSubGroup(name="Eco-Friendly Cleaning", product_group_id=3, product_sub_group_id=26))  # ID: 173
except:
    db.session.rollback()

# Product Sub-Sub-Group Interests
try:
    db.session.add(InterestsProductsubsubgroup(interests_id=1, productsubsubgroup_id=1)) # ID: 1
    db.session.add(InterestsProductsubsubgroup(interests_id=1, productsubsubgroup_id=1)) # ID: 1
    db.session.add(InterestsProductsubsubgroup(interests_id=1, productsubsubgroup_id=1)) # ID: 1
    db.session.add(InterestsProductsubsubgroup(interests_id=1, productsubsubgroup_id=1)) # ID: 1
    db.session.add(InterestsProductsubsubgroup(interests_id=1, productsubsubgroup_id=1)) # ID: 1
    db.session.add(InterestsProductsubsubgroup(interests_id=1, productsubsubgroup_id=1)) # ID: 1
    db.session.commit()
except:
    db.session.rollback()
