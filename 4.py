import csv

def find_books_by_author(input_file, output_file, author):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        for row in reader:
            if row[0] == author and int(row[2]) < 2019:
                outfile.write(f"{row[1]}\n")


find_books_by_author('data.csv', 'res.txt', 'Пушкин')