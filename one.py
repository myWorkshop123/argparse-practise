import argparse
# Create a object of the ArgumentParser class 
parser = argparse.ArgumentParser(description="Practise of argparse module",formatter_class=argparse.RawDescriptionHelpFormatter)
# for formatter_class=https://docs.python.org/3/library/argparse.html#formatter-class

# Specift the argument that you want to add 
parser.add_argument("square",help="Display the square of the number",type=int)
parser.add_argument("--verbose",help="Increase output verbosity ")

# parse_args function will recieve the arguements from the cli and return a tuple 
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")

print(args.square ** 2)


