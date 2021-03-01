def reverse():
    with open('input.dat', 'rb') as in_file, open('output.dat', 'wb') as out_file:
        out_file.write(in_file.read()[::-1])
