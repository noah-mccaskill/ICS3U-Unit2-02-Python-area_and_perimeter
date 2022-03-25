#!/usr/bin/env python3

# Created by Noah McCaskill
# Created in March 2022
# Program finding perimeter and area with user inputs


def main():
    print("Give me measurements of a rectangle!")
    length = int(input("Please enter the length (mm): "))
    width = int(input("Please enter the width (mm): "))
    area = length * width
    perimeter = 2 * (length + width)
    superscript = str.maketrans("2", "²")

    print("Area: {} mm²".translate(superscript).format(area))
    print("Perimeter: {} mm".format(perimeter))


if __name__ == "__main__":
    main()
