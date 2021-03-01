def palindrome():
    inlet = open('input.dat', 'rb')
    data = inlet.read().strip()
    inlet.close()
    if data == data[::-1]:
        return True
    return False
