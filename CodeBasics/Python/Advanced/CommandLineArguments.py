import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--physics")
parser.add_argument("--chemistry")
parser.add_argument("--maths")

args=parser.parse_args()

print((int(args.physics)+int(args.chemistry)+int(args.maths))/3)
