import argparse
from itertools import chain, tee


def recursive_calculate_fuel_needed(mass_list):
    m1, m2 = tee(mass_list)
    if all(m <= 0 for m in m1):
        return 0

    total = 0
    additional_masses = []
    for fuel in calculate_fuel_needed(m2):
        total += fuel
        additional_masses.append(fuel)
    return total + recursive_calculate_fuel_needed(additional_masses)


def calculate_fuel_needed(module_mass_list):
    for mass in module_mass_list:
        fuel_needed = (mass // 3) - 2
        fuel_needed = max(fuel_needed, 0)
        yield fuel_needed


def read_file(filename):
    with open(filename) as f:
        for line in f:
            yield int(line)


def main():
    parser = argparse.ArgumentParser(description="Day 1 solution for advent of code 2019")
    parser.add_argument("--input-file", "-f", dest="input_file", metavar="f", default="input", help="The input file for the day 1 problem")
    parser.add_argument("--part", "-p", dest="part", metavar="p", default="one", choices=["one", "two"], help="Which part of the day1 problem do you want to solve?")

    args = parser.parse_args()
    
    if args.part == "one":
        total_fuel_needed = sum(calculate_fuel_needed(read_file(args.input_file)))
    elif args.part == "two":
        input_masses = read_file(args.input_file)
        total_fuel_needed = recursive_calculate_fuel_needed(input_masses)

    print("Total fuel needed for this launch: ", total_fuel_needed)


main()
