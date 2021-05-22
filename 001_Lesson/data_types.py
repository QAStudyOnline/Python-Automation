# Python do not have strong data type

"""
We have a next Data types in Python:
1) Numbers (числа)
2) Strings (строки)
3) Lists (списки) | (DATA STRUCTURE)
4) Dictionaries (словари) | (DATA STRUCTURE)
5) Tuples (кортежи) | (DATA STRUCTURE)
6) Sets (множества) | (DATA STRUCTURE)
7) Boolean (логический тип данных)
"""
# Numbers (числа) can be an integer or float\doable
# Integer example:
print("Integer example")
a = 10
b = 5
print(a + b)

# Float example
print("Float example")
a = 10.2
b = 20 / 4
print((a / b) * 10 - 2 + 4)

# String example
print("String example:")
a = "Let's Start "
b = 'Automation'
print(a + " " + b)

# String as Text example
print("String as Text example")
print()
c = """
Let's Start Automation Right Now And Immediately !!!
To do this, let's study Jenkins, Python, Selenium, Request, PyTest and Allure report !!
Friends Comrades Colleagues Brothers !!!
"""
print(c)

# Lists
print("Lists")
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
b = ['hot', 'dog', 'free', 'first', 'five']
print(b)
c = [1, 2, 4, "olla", 'Hände hoch']
print(c)
# Call specific element of the list can be done by index, index start from 0 in list
print(c[4])
# Re-set of value for specific element in list can be done by index
c[0] = "Automation forever !!!"
print(c)
# Got list from sting
d = list("Hände hoch")
print(d)
# Got a reverse list
d.reverse()
print(d)

# Also possible to create a List of lists
e = [
    ["Let's", "Start", "Automation", "Right", "Now", "And", "Immediately", "!!!"],
    ["To do this", "let's study", "Jenkins", "Python", "Selenium", "Request", "PyTest", "and", "Allure report", "!!"],
    ["Friends", "Comrades", "Colleagues", "Brothers", "!!!"]
]
print(e)
# And call specific sub list by index
print(e[0])

# We can find the length of list by len function
print(len(e))

# We can sort List by call sorted function
print(sorted(b))

# Dictionary kye:value storage'
ukraine = {'name': 'Ukraine', 'capital': 'Kyiv', 'area': '603,628'}
print(ukraine)

# Call specific value from dictionary
print(ukraine['name'])

# Re-set value for some key in dictionary
ukraine['capital'] = 'Kharkiv'
print(ukraine)

# Also possible to create a dictionary of dictionary
ukraine_city = {
    'kyiv':
        {
            'Area': '839',
            'Population': '2,950,819'
        },
    'rivne':
        {
            'Area': '63.00',
            'Population': '246,003'
        }
}

# Check our dictionary
print(ukraine_city)
# Call by key
print(ukraine_city['kyiv'])
# Call specific value
print(ukraine_city['kyiv']['Area'])

# Tuple immutable list

# How create empty Tuple
tuple1 = tuple()
print(tuple1)

# Single element tuple
tuple2 = ('password',)
print(tuple2)

# Create a tuple based on list
list_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
tuple_keys = tuple(list_keys)
print(tuple_keys)

# Find specific element by index
print(tuple_keys[2])

# Try to change immutable tuple
#tuple_keys[2]='cocacola'

# Set unique value not sorted list
some_values = [10, 20, 30, 40, 100, 10]
print(set(some_values))
unique_values = set(some_values)
unique_values.add(200)
print(unique_values)
unique_values.discard(20)
print(unique_values)
unique_values.clear()
print(unique_values)

# Boolean value True and False
items = [1, 2, 3]
empty_list = []
print(bool(empty_list))
print(bool(items))
print(bool(0))
print(bool(1))
# Comparing
print(1 > 0)
print(1 < 0)
print(1 == 0)
print(1 != 0)
print(1 >= 0)
print(1 <= 0)