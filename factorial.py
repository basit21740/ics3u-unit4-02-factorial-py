#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Dec 2021
# this program is do while loop


def main():
    # this is function for creating do while loop

    # variables
    counter = 0
    product_num = 1

    # input
    number = input("Enter a positive integer: ")
    number = int(number)

    # process & output
    if number <= 0:
        if number == 0:
            print("0! = 1")
        else:
            print("You did not enter a positive integer")
    else:
        while True:
            counter += 1
            product_num *= counter
            if counter >= number:
                break
        print(f"{number}! = {product_num}.")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()