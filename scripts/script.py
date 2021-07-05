"""Just an empty script to simulate the training process."""

import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--params", type=str)
args = parser.parse_args()

with open(args.params):
    print("Read parameters file", args.params)

print("Training loop")
try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    print("Terminated")
