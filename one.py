import argparse
# Create a object of the ArgumentParser class 
parser = argparse.ArgumentParser()

# Specift the argument that you want to add 
parser.add_argument("square",help="Display the square of the number",type=int)

# parse_args function will recieve the arguements from the cli and return a tuple 
args = parser.parse_args()

print(args.square ** 2)


