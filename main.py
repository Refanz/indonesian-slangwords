import csv

# Save slangwords duct to JSON file
def add_slang(slang, meaning):
    with open('data/indonesian-slangwords.csv', 'a', newline='', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow([slang, meaning])

# Input slang
slang = input("Input slang: ")
meaning = input("Input meaning: ")