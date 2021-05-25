#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 25, 2021
# This program displays the square of all the
# numbers from 0 up to the users number


# main function
def main():

    # vars
    user_num = input("What is you number (must be a whole positive number): ")

    # make sure the users num can be an integer
    try:
        user_num = int(user_num)

        # if the users number is less than 0
        if (user_num < 0):
            print("Number must be positive")
        else:
            # excecutes the code the number of times the user said to
            for counter in range(user_num + 1):
                # prints the output for the currect loop of the for function
                print("{}² = {}".format(counter, counter ** 2))

    # if there is an error
    except ValueError:
        print("Not valid input")


if __name__ == "__main__":
    main()
