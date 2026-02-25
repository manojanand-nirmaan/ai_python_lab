# Single Sample: Food Quality Features

sample = {

    'batch_id': 'B-2026-X9',

    'temp_c': 7.2, # Feature 1

    'ph': 6.5, # Feature 2

    'moisture': 12.1, # Feature 3

    'label': 'good' # Target Class

}

 

# Accessing data by key

print(f"Batch: {sample['batch_id']}")

print(f"Quality Label: {sample['label']}")

 

# List of Dictionaries (Dataset structure)

dataset = [ sample, {'temp_c': 12.4, 'label':'bad'} ]

# Add a new key 'shelf_life_days' with value 14 to the sample dictionary.