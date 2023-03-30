# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1: Greet Template

def greet(name, greeting='Hello, <name>!'):
    return greeting.replace ('<name>', name)

print(greet('Bob'))
print(greet('Bob', 'Bonjour, <name>!'))

# Part 2: Force

def force(mass, body='earth'):
    body_dict = {
        'sun': 274,
        'jupiter': 25,
        'neptune': 11.1,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon':	1.6,
        'pluto': 0.6
    }
    return mass * body_dict[body]

print(force(5))
print(force(5, 'jupiter'))

# Part 3: Gravity

def pull(m1, m2, d):
    G=6.674*(10**-11)
    return (G*float(m1)*float(m2))/(float(d)**2)

print(round(pull(800, 1500, 3),10))