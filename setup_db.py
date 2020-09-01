from app import app, db
from app.models import AllRecipes

db.create_all()

recipes = [
    ['Cheesy omelettes', 'Deliciously cheesy eggs', '2 eggs</br>a handful of cheese</br>50 mL of milk</br></br>whisk the eggs and milk together until mixed. </br> cover the bottom of pan on stove with cheese, then pour egg mixture over it.</br>Flip when egg mixture becomes mostly solid.</br>Consume when still hot.', False],
    ['Instant noodles', 'Instant noodles with cheese', '1 packet of instant noodles</br>250 mL of water</br>1 slice of cheese</br></br>boil water in pot, then add noodles and seasoning.</br>Let simmer for 1 minute.</br>Place cheese on top and serve immediately', False],
    ['Fried Egg', "It's a fried egg", '1 egg</br></br>Crack egg into a hot, oiled pan</br>When white has cooked serve.', True],
    ['Cereal', 'Cereal', '250 mL milk</br>cereal of choice</br></br>Put cereal into a bowl</br>Add milk then eat', False],
    ['Watermelon', 'It tastes like water', 'watermelon</br></br>Cut a watermelon', True],
    ['Pumpkin Soup', 'Creamy pumpkin soup', '1 Pumpkin</br>100 mL Sour cream</br>200 mL chicken stock</br></br>Slice pumpkin, then roast in oven for 30 minutes or until soft.</br>Blend pumpkin, sour cream and chicken soup stock in a blender until smooth</br>Boil on stove for 10 minutes', True],
    ['Tempura', 'Crispy, golden tempura', 'Bread crumbs</br>prawns or vegetables</br>1 cup self-raising flour</br>1 cup rice flour</br>250 mL carbonated water</br></br> mix the self-raising and rice flour together with the carbonated water to form a batter.</br>Heat oil on stove.</br>Dip prawns/vegetables in the batter then in the bread crumbs before frying.', False],
    ['Hot Chocolate', 'Really good hot chocolate', "15 chips of milk chocolate</br>250 mL of full cream milk</br></br>Heat milk over stove. Make sure it doesn't boil</br>Put chocolate in the milk and heat until melted", False],
    ['Hard-boiled egg', 'Perfect timing for hard boiled eggs', 'Eggs</br></br>Add eggs to boiling water. Ensure all eggs are completely covered.</br>Boil for 10 minutes.</br>Serve with black pepper and sweet soy sauce.', True],
    ['Spicy Carbonara', 'Really, really good carbonara', '1 bottle of carbonara</br>2 tblspns of Samyang spicy chili sauce</br>600 gm pasta of choice</br></br>Boil pasta until soft, then drain well.</br>Pour carbonara and spicy sauce into hot pasta and stir.</br>Add cheese to taste or if too spicy.', True],
    ['Healthy matcha', 'Tastes like matcha but with health benefits', '2 tspn wheatgrass powder</br>2 tbsp of honey</br>50 mL of milk</br>200 mL Hot water</br></br>Stir all ingredients in a cup until well mixed.', False],
    ['Mochi', 'Chewy glutinous rice balls', '1 cup glutinous rice flour</br>1 cup hot water</br>100 gm sugar</br>200 gm tofu</br></br></br>Mix all ingredients together in a bowl until combined in a dough.</br>Roll into small balls and boil in water</br>Remove after it floats for a few minutes.</br>Eat when cooled.', False],
    ['Curry puffs', 'Easy to make curry puffs', '1 potato</br>1 onion</br>1 cup of peas</br>1 carrot</br>2 tbsp curry powder</br>1 egg</br>4 sheets of puff pastry</br></br>Boil the egg until hard boiled.</br>Fry onions until fragrant, then add diced potatoes and carrots</br>When the potatos and carrots begin to soften, add the peas, curry powder and a bit of water - enough to moisten</br>Stir over heat until thoroughly mixed.</br>Cut puff pastry into smaller squares (3x3) then use it to wrap the curry. Place a small piece of egg in each puff.</br>Bake in oven at 160C for 30 minutes or until golden brown</br>Serve while hot.', True]
    ]


for recipe in recipes:
    new_recipe = AllRecipes(name=recipe[0], description=recipe[1], recipe=recipe[2], fav=recipe[3])
    db.session.add(new_recipe)
db.session.commit()