import re

def find_text_in_brackets(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for i, line in enumerate(infile, 1):
            matches = re.findall(r'\((.*?)\)', line)
            if matches:
                outfile.write(f"строка {i}: {'; '.join(matches)}\n")


find_text_in_brackets('data.txt', 'res.txt')