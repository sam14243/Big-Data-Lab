#!/usr/bin/python3
import sys

def reducer():
    min_temp = float('inf')
    max_temp = float('-inf')

    for line in sys.stdin:
        line = line.strip()
        key, temperature = line.split('\t')
        temperature = float(temperature)

        if temperature < min_temp:
            min_temp = temperature
        if temperature > max_temp:
            max_temp = temperature

    print(f"Min Temperature: {min_temp}")
    print(f"Max Temperature: {max_temp}")

if __name__ == "__main__":
    reducer()