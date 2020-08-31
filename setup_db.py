from app import app, db
from app.models import AllRecipes

db.create_all()

recipes = [
	['Cheesy omelettes', 'Deliciously cheesy eggs', '2 eggs</br>a handful of cheese</br>50 mL of milk</br></br>whisk the eggs and milk together until mixed. </br> cover the bottom of pan on stove with cheese, then pour egg mixture over it.</br>Flip when egg mixture becomes mostly solid.</br>Consume when still hot.'],
	['Instant noodles', 'Instant noodles with cheese', '1 packet of instant noodles</br>250 mL of water</br>1 slice of cheese</br></br>boil water in pot, then add noodles and seasoning.</br>Let simmer for 1 minute.</br>Place cheese on top and serve immediately'],
	['Fried Egg', "It's a fried egg", '1 egg</br></br>Crack egg into a hot, oiled pan</br>When white has cooked serve.'],
	['Cereal', 'Cereal', '250 mL milk</br>cereal of choice</br></br>Put cereal into a bowl</br>Add milk then eat'],
	['Watermelon', 'It tastes like water', 'watermelon</br></br>Cut a watermelon'],
	['Pumpkin Soup', 'Creamy pumpkin soup', '1 Pumpkin</br>100 mL Sour cream</br>200 mL chicken stock</br></br>Slice pumpkin, then roast in oven for 30 minutes or until soft.</br>Blend pumpkin, sour cream and chicken soup stock in a blender until smooth</br>Boil on stove for 10 minutes'],
	['Tempura', 'Crispy, golden tempura', 'Bread crumbs</br>prawns or vegetables</br>1 cup self-raising flour</br>1 cup rice flour</br>250 mL carbonated water</br></br> mix the self-raising and rice flour together with the carbonated water to form a batter.</br>Heat oil on stove.</br>Dip prawns/vegetables in the batter then in the bread crumbs before frying.'],
	['Hot Chocolate', 'Really good hot chocolate', "15 chips of milk chocolate</br>250 mL of full cream milk</br></br>Heat milk over stove. Make sure it doesn't boil</br>Put chocolate in the milk and heat until melted"],
	['Hard-boiled egg', 'Perfect timing for hard boiled eggs', 'Eggs</br></br>Add eggs to boiling water. Ensure all eggs are completely covered.</br>Boil for 10 minutes.</br>Serve with black pepper and sweet soy sauce.'],
	['Spicy Carbonara', 'Really, really good carbonara', '1 bottle of carbonara</br>2 tblspns of Samyang spicy chili sauce</br>600 gm pasta of choice</br></br>Boil pasta until soft, then drain well.</br>Pour carbonara and spicy sauce into hot pasta and stir.</br>Add cheese to taste or if too spicy.'],
	['Healthy matcha', 'Tastes like matcha but with health benefits', '2 tspn wheatgrass powder</br>2 tbsp of honey</br>50 mL of milk</br>200 mL Hot water</br></br>Stir all ingredients in a cup until well mixed.']
]


for recipe in recipes:
    new_recipe = AllRecipes(name=recipe[0], description=recipe[1], recipe=recipe[2])
    db.session.add(new_recipe)
db.session.commit()