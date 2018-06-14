
def read_file(filename):

    # Return an array of text
    f = open(filename, 'r')
    data = f.readlines()
    f.close()
    return data