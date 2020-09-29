#!/usr/bin/env python3
def dna_complement(sequence):
    Bases = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    complement = ""
    valid_seq = True
    if sequence:
        for base in sequence:
            if base.upper() in Bases:
                complement = complement + Bases.get(base.upper())
            else:
                valid_seq = False
                break
    else:
        valid_seq = False
    if valid_seq:
        return complement
    else:
        return None


# Demo of dna_complement(sequence)
valid_input = "aatTgGcC"
invalid_input = "aatTgGzZ"
print("Example input string: \"", valid_input, "\"", sep="")
print("Complement is: \"", dna_complement(valid_input), "\"", sep="")
print("Example input string: \"", invalid_input, "\"", sep="")
print("Complement is:", dna_complement(invalid_input))


# References
# https://www.w3schools.com/python/python_functions.asp
# https://stackoverflow.com/questions/20875150/how-to-fill-an-empty-string-which-has-already-been-created-in-python
# https://www.w3schools.com/python/python_booleans.asp
# https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3
# https://www.geeksforgeeks.org/python-string-upper/
# https://www.geeksforgeeks.org/get-method-dictionaries-python/#:~:text=In%20python%20dictionaries%2C%20following%20is,a%20value%20for%20a%20key.&text=The%20get()%20method%20is,used%20with%20only%20one%20argument).
# https://www.educative.io/edpresso/how-to-check-if-a-key-exists-in-a-python-dictionary
# https://www.tutorialspoint.com/python/python_functions.htm
# https://stackoverflow.com/questions/9050355/using-quotation-marks-inside-quotation-marks
# https://www.poftut.com/python-how-to-print-without-newline-or-space/#:~:text=Change%20separator,will%20join%20two%20string%20together.
