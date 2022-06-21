name = 'Nkem C. Omede'
age = 43 # This is for real
height = 178 #centimeters
weight = 75 #kg
eyes = 'brown'
teeth = 'white'
hair = 'black'

print(f"Let's talk about {name}.")
print(f"He's {height} cm tall.")
print(f"He's {weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#This line is tricky, try to get it exactly right
total = age + height + weight
print(f"if I add {age}, {height}, and {weight} I get {total}.")

#Convert inches to centimeters
a = "height in inches"
b = "height in cm"
b = a * 2.54
