# Scenario: Incoming stream of device IDs (with duplicates)

dev_ids = ['A1', 'A1', 'B7', 'C3', 'B7', 'D4']

# Create a set to remove duplicates instantly

unique_ids = set(dev_ids)

print(f"Raw count: {len(dev_ids)}")

print(f"Unique count: {len(unique_ids)}")

print(f"Unique Set: {unique_ids}")
 
# Fast membership test O(1) vs List O(n)

check_id = 'C3'

if check_id in unique_ids:

    print(f"Device {check_id} is active.")

