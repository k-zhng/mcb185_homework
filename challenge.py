import pandas as pd

# Define the genomic coordinates from the example
file1 = pd.DataFrame({
    'Chr': ['Chr1', 'Chr1', 'Chr2'],
    'Start': [100, 300, 100],
    'End': [200, 400, 150],
    'Label': ['D', 'E', 'F']
})

file2 = pd.DataFrame({
    'Chr': ['Chr1', 'Chr1', 'Chr2'],
    'Start': [110, 50, 200],
    'End': [112, 550, 300],
    'Label': ['A', 'B', 'C']
})

# Function to find overlaps
def find_overlaps(df1, df2):
    overlaps = []
    for index1, row1 in df1.iterrows():
        for index2, row2 in df2.iterrows():
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
