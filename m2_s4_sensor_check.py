# Sensor Configuration (EEE/IoT Example)

sensor_id = 42 # int

voltage = 255.0 # float

is_active = True # bool

 

# Logic with conditional operator

status = "OK" if voltage < 250 else "HIGH_VOLTAGE"

 

# Output results

print(f"Sensor {sensor_id}: {voltage}V -> Status: {status}")

 

# List example

readings = [228.4, 229.1, 231.0]


