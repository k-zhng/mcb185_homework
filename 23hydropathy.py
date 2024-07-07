import math
hydrophob_vals = [["a", 1.80], ["b", 2.50], ["c", -3.50], ["d", -3.50], ["e", -3.50], ["f", 2.80], ["g", -0.40], ["h", -3.20], ["i", 4.50], ["k", -3.90], ["l", 3.80], ["m", 1.90], ["n", -3.50], ["p", -1.60], ["q", -3.50], ["r", -4.50], ["s", -0.80], ["t", -0.70], ["v", 4.20], ["w", -0.90], ["y", -1.30]]

def get_val (letter):
    for i in range(0, len(hydrophob_vals)):
        if (letter.lower() == hydrophob_vals[i][0]):
            return hydrophob_vals[i][1]
    return math.nan
    
print(get_val("a"))
print(get_val("z"))