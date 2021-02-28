examples = list()
with open('in_file.txt', mode='r') as f:
    for line in f:
        line = line.rstrip()
        examples.append(f'{line} = {eval(line)}')
with open('out_file.txt', mode='w') as f:
    for example in examples:
        f.write(example + '\n')
