def calc_shelf_life(days, temp_c):
    # Encapculate any businees logic in pure function

    # Reduce 0.5 days per °C over 4°C

    loss = (temp_c - 4) * 0.5

    if loss < 0: loss = 0

    return max(0, days - loss)

# Usage

base_life = 10 # days

current_temp = 8.0 # °C

print(calc_shelf_life(base_life, current_temp))