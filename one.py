import argparse
# Create a object of the ArgumentParser class 
parser = argparse.ArgumentParser()

# Specift the argument that you want to add 
parser.add_argument("echo",help="echo the string you use here ")

# parse_args function will recieve the arguements from the cli and return a tuple 
args = parser.parse_args()

# args: Namespace(argument:value)
print(args.echo)


