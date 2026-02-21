import math

# Lambda for RMS calculation

rms = lambda samples: math.sqrt(

sum(x*x for x in samples) /

len(samples)

)

# Usage

readings = [220, 225, 218, 230]

print(f"{rms(readings):.2f}V")