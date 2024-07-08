# Define the genomic coordinates from the example
file1 = [
    {'Chr': 'Chr1', 'Start': 100, 'End': 200, 'Label': 'D'},
    {'Chr': 'Chr1', 'Start': 300, 'End': 400, 'Label': 'E'},
    {'Chr': 'Chr2', 'Start': 100, 'End': 150, 'Label': 'F'}
]

file2 = [
    {'Chr': 'Chr1', 'Start': 110, 'End': 112, 'Label': 'A'},
    {'Chr': 'Chr1', 'Start': 50, 'End': 550, 'Label': 'B'},
    {'Chr': 'Chr2', 'Start': 200, 'End': 300, 'Label': 'C'}
]

# Function to find overlaps
def find_overlaps(list1, list2):
    overlaps = []
    for row1 in list1:
        for row2 in list2:
            if row1['Chr'] == row2['Chr']:
                overlap_start = max(row1['Start'], row2['Start'])
                overlap_end = min(row1['End'], row2['End'])
                if overlap_start <= overlap_end:
                    overlaps.append(f"{row2['Label']}-{row1['Label']}: {overlap_start}-{overlap_end}")
    return overlaps

# Find overlaps
overlaps = find_overlaps(file1, file2)

# Output the results
for overlap in overlaps:
    print(overlap)
