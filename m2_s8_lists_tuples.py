# List of voltage readings

voltage_readings = [

228.4, 229.1, 231.0

]

# Add new reading

voltage_readings.append(233.2)

print(voltage_readings[-1])

# Output: 233.2



# List of immutable tuples

students = [

(101, 'Anu'),

(102, 'Rahul')

]

# Attempting modification fails

# students[0][1] = 'Anushka' # Error!

# Replace entire record

students[0] = (101, 'Anushka')

# Raw material inventory

inventory = [

'wheat_flour', 'rice',

'soy', 'sugar'

]

# Check first two items

batch_A = inventory[:2]

print(batch_A)

# ['wheat_flour', 'rice'] - New List with first two items
