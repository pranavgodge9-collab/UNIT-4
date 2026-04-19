import csv

def count_rows(file_path, skip_header=True):
    with open(file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        if skip_header:
            next(reader, None) 
        return sum(1 for row in reader)

print(f"Total data rows: {count_rows('data.csv')}")
