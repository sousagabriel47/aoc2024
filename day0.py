from utils import get_data_full, DATA_FOLDER
import argparse
import os

parser = argparse.ArgumentParser(description='Solution aoc2024')
parser.add_argument('-d', "--day", help="Day of problem",
                    type=int, default=1)
parser.add_argument('-t', "--test", help="Test Data",action='store_true')
parser.add_argument('-f', "--full", help="Full Data",action='store_true')
arg = parser.parse_args()

def solve(type, day):
    with open(os.path.join(DATA_FOLDER,
                           type,
                           str(day)), 'r') as f:
        data = f.read().splitlines()
    # solution
    print(data)

if __name__ == '__main__':
    get_data_full(arg.day)
    if arg.full:
        solve('full', arg.day)
    else:
        solve('test', arg.day)