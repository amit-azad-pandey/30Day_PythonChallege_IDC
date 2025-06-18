import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Convert temperature between Celsius and Fahrenheit")

# Add arguments
parser.add_argument("--temp", type=float, required=True, help="Temperature value to convert")
parser.add_argument("--unit", choices=["c", "f"], required=True, help="Unit to convert to: c (Celsius), f (Fahrenheit)")

# Parse the arguments
args = parser.parse_args()

# Convert based on unit
if args.unit == "c":
    result = (args.temp - 32) * 5 / 9
    print(f"{args.temp}°F is {result:.2f}°C")
else:
    result = (args.temp * 9 / 5) + 32
    print(f"{args.temp}°C is {result:.2f}°F")
