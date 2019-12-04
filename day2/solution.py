import argparse
from itertools import chain, tee
import operator

class Computer(object):
    def __init__(self, filename):
        self.memory = [code for code in self.read_file(filename)]

    def read_file(self, filename):
        with open(filename) as f:
            for line in f:
                for code in line.split(','):
                    yield int(code)

    def run_program(self, initial_params):
        if initial_params:
            self.memory[1], self.memory[2] = initial_params
        for i in range(0, len(self.memory)-1, 4):
            opcode = self.memory[i]
            if opcode == 99:
                return
            elif opcode == 1:
                op = operator.add
            elif opcode == 2:
                op = operator.mul
            else:
                raise ValueError("Invalid program")

            arg1_index, arg2_index, dest = self.memory[i+1:i+4]
            arg1 = self.memory[arg1_index]
            arg2 = self.memory[arg2_index]
            # print(arg1, arg2, dest)
            self.memory[dest] = op(arg1, arg2)

    @property
    def program_output(self):
        return self.memory[0]

    def print_program_output(self):
        print(self.memory[0])

    def print_full_program(self):
        print(self.memory)


def main():
    parser = argparse.ArgumentParser(description="Day 2 solution for advent of code 2019")
    parser.add_argument("--input-file", "-f", dest="input_file", metavar="f", default="input", help="The input file for the problem")
    parser.add_argument("--part", "-p", dest="part", metavar="p", default="one", choices=["one", "two"], help="Which part of the problem do you want to solve?")

    args = parser.parse_args()
    
    if args.part == "one":
        computer = Computer(args.input_file)
        computer.run_program([12, 2])
        computer.print_program_output()
    elif args.part == "two":
        desired_output = 19690720
        for noun in range(0, 99):
            for verb in range(0, 99):
                computer = Computer(args.input_file)
                computer.run_program([noun, verb])
                if computer.program_output == desired_output:
                    print("{noun}{verb}".format(noun=noun, verb=verb))

main()
