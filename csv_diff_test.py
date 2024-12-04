from csv_diff import load_csv, compare
from csv import DictWriter
diff = compare(
    load_csv(open("core1.csv"), key="fsid"),
    load_csv(open("missing1.csv"), key="fsid")
)

# Get all the row headers across all the changes
headers = set({'change type'})
for key, vals in diff.items():
    for val in vals: # Multiple of the same difference 'type'
        headers = headers.union(set(val.keys()))

# Write changes to file
with open('changes1.csv', 'w', encoding='utf-8') as fh:
    w = DictWriter(fh, headers)
    w.writeheader()
    for key, changes in diff.items():
        for val in changes: # Add each instance of this type of change
            val.update({'change type': key}) # Add 'change type' data
            w.writerow(val)