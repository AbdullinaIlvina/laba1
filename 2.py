def count_lines_and_words(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        outfile.write(f"строк – {len(lines)}\n")
        for i, line in enumerate(lines, 1):
            words = len(line.split())
            outfile.write(f"строка {i}: слов – {words}\n")


count_lines_and_words('data.txt', 'res.txt')