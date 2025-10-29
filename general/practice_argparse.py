import argparse
import math

parser = argparse.ArgumentParser(description='Calculate the volume of a Cylinder')
parser.add_argument('--radius', type=int, help='Radius of the Cylinder')
parser.add_argument('--height', type=int, help='Height of the Cylinder')
args = parser.parse_args()

