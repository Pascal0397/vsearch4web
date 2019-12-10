word = "bottles"  # Assigns a string to a value "word"
for beer_num in range(99, 0, -1):  # Creates a for loop which has the name "beer_num", it counts from 99 to 0 in -1 step
    print(beer_num, word, "of beer on the wall.")  # Prints beer_num number and the word + a string
    print(beer_num, word, "of beer.")  # Same as above
    print("Take one down.")  # Prints a string
    print("Pass it around.")  # Prints a string
    if beer_num == 1:  # If beer_num is 1 print() this:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1  # Creates a variable with beer_num - 1 stored in it
        if new_num == 1:  # If new num is 1 change word
            word = "bottle"
        print(new_num, word, "of beer on the wall")  # Print new number + word + string
    print()