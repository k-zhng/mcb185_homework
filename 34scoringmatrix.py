def scoring_matrix(alphabet, matscore, misscore):
    matrix = " "
    for char in alphabet:
        matrix += "  " + str(char)
    for char in alphabet:
        matrix += "\n" + char
        for other_char in alphabet:
            matrix += " "
            if (char == other_char):
                matrix += str(matscore)
            else:
                matrix += str(misscore)
    return matrix

alphabet = 'ACGTN'
match = '+1'
mismatch = '-2'
print(scoring_matrix(alphabet, match, mismatch))