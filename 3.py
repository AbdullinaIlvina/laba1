def replace_multiple_spaces(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            outfile.write(' '.join(line.split()) + '\n')


replace_multiple_spaces('data.txt', 'res.txt')