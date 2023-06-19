#****************************************************************
#Name: Wing Lok LO
#Link: https://replit.com/join/fiaxtpavaq-lowinglokjason
#****************************************************************

# import random package for question 6
import random as random

#############
#Question #1
#############

# Create a dictionary to store six pieces of information about myself (First Name, Last Name, Gender, City, Occupation and Program)
info = {'First Name': 'LO', 'Last Name': 'WING LOK', 'Gender': 'M', 'City': 'HONG KONG', 'Occupation': 'student', 'Program': 'BAPG'}
# Print each piece of information stored in my dictionary
for key, value in info.items():
  print(f'{key}:{value}')

#############
#Question #2
#############

# Create a dictionary to store five classmates and their favourite foods
classmates = {'John': ['bread', 'rice', 'lemon'], 'Tim': ['oat', 'chicken', 'apple'], 'Peter': ['milk', 'beef', 'orange'], 'May': ['egg', 'pork', 'pear'], 'Clare': ['pancake', 'lamb', 'melon']}
# Use a for loop to print each person’s name and their favourite foods
for key, value in classmates.items():
  print(f"The favourute foods of {key} are {', '.join(value)}.")

#############
#Question #3
#############

# Create dictionaries where represents a different persons' foods and meals
Peter = {'Name': 'Peter', 'Food': ['egg', 'milk'], 'Meal': 'breakfast'}
Pony = {'Name': 'Pony', 'Food': ['chicken', 'soup'], 'Meal': 'lunch'}
Jack = {'Name': 'Jack', 'Food': ['seafood', 'wine'], 'Meal': 'dinner'}
# Store the dictionaries in a list
meals = [Peter, Pony, Jack]
# print each person, meal and food using a for loop
for meal in meals:
  print(f"{meal['Name']}'s {meal['Meal']} is {meal['Food'][0]} and {meal['Food'][1]}.")

#############
#Question #4
#############

# Create a dictionary which contains three cities and add infomation in the sub dictionary
cities = {'Hong Kong': {'Country': 'China', 'Population': '7 million', 'Facts': ['Cantonese and English are the official languages of Hong Kong.', 'Hong Kong consists of several islands and territories.', 'Hong Kong is one of the most densely populated cities in the world.']}, 
          'Sudbury': {'Country': 'Canada', 'Population': '0.16 million', 'Facts': ['Greater Sudbury is locally known as the City of Lakes and contains more lakes than any other municipality in Canada.', 'Dynamic Earth is home to the Big Nickel which is nine metres (30 ft.) high and recognized around the world.', 'With nine operating mines, two mills, two smelters, and a nickel refinery, Sudbury is arguably the hard rock mining capital of the world.']}, 
          'Toronto': {'Country': 'Canada', 'Population': '3 million', 'Facts': ['Toronto is the largest city in Canada, and the 4th largest city in North America.', 'Toronto is home to North America’s only castle.', 'The CN Tower is the largest free-standing structure in the Western Hemisphere.']}}
# Print the name of each city and all of the information
for city, detail in cities.items():
  print(f"{city} is in {detail['Country']} with {detail['Population']}. The facts of {city} are {' '.join(detail['Facts'])}")

#############
#Question #5
#############

# Create a dictionary with stock names which list 10 stock prices for each stock
stock_prices = {'TSLA': [189.5, 194.13, 195.06, 196.76, 207.13, 203.65, 190.85, 193.59, 208.72, 210.48], 
                'AAPL': [149.52, 152.06, 152.3, 154.11, 153.7, 150.06, 151.02, 151.66, 153.63, 153.85], 
                'NVDA': [210.42, 211.02, 210.84, 221.72, 222.09, 223.37, 212.61, 217.91, 229.6, 222.76]}
# Using a for loop, print out the stocks, minimum price, average price, and maximum price for each stock
for stock, price in stock_prices.items():
    print(f"The minimum price, average price and maximum price of the {stock} are {min(price)}, {sum(price)/len(price)} and {max(price)} respectively.")

#############
#Question #6
#############

# Set the popularity score at 0
score = 0
# Use a for loop to run the program five times that create an event adding a random amount of approval to the overall total
for i in range(5):
    event = f"Event {i+1}"
    gain = random.randint(1, 20)
    score += gain
    print(f"{event}: The public canvassing gained {gain}% popularity! Total popularity is now {score}%.")
# Print the final result to see whether I will win or lose the election
if score > 51:
    print("I won the election!")
else:
    print("I lost the election.")

#############
#Question #7
#############

# Create a dictionary with values of type int, float, string, list, dictionary, and tuple
koenigsegg = {'Model': 'agera rs', 'Production Amount': 25, '0-200-0 km/h in sec': 13.5, 'Features': ['twin turbo aluminum 5.0L V8 engine', 'Body made from pre-impregnated carbon fiber/kevlar', 'Two-door, two seater with removable hardtop'], 'Output': {'Power output': '960 hp at 7100 rpm', 'Max torque': '1100 Nm at 4000 rpm'}, 'Dimensions(length, width, height) in mm': (4293, 2050, 1120)}
# Check if the data types of values inside the dictionary
print(type(koenigsegg['Model']))
print(type(koenigsegg['Production Amount']))
print(type(koenigsegg['0-200-0 km/h in sec']))
print(type(koenigsegg['Features']))
print(type(koenigsegg['Output']))
print(type(koenigsegg['Dimensions(length, width, height) in mm']))