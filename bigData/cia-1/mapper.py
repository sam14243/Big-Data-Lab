#!/usr/bin/python3
import sys

def mapper():
    for line in sys.stdin:
        line = line.strip()
        fields = line.split(',')
        if len(fields) > 1:
            try:
                temperature = float(fields[2])
                print(f"temperature\t{temperature}")
                
            except ValueError:
                continue

if __name__ == "__main__":
    mapper()