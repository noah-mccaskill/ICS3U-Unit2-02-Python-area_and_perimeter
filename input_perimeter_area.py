#!/usr/bin/env python3

# Created by Noah McCaskill
# Created in March 2022
# Program finding perimeter and area with user inputs


def main():
    # Calculating perimeter and area

    # Input
    print("Give me measurements of a rectangle!")
    length = int(input("Please enter the length (mm): "))
    width = int(input("Please enter the width (mm): "))

    # Process
    area = length * width
    perimeter = 2 * (length + width)

    # Output
    print("Area: {} mm²".format(area))
    print("Perimeter: {} mm".format(perimeter))


if __name__ == "__main__":
    main()
