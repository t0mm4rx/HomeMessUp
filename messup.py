import random
import sys
import os

adjectives = []
nouns = []
exts = []

nb_files = int(sys.argv[1])
path = sys.argv[2]

total = 0

with open('adjectives_en.txt') as file:
    adjectives = file.readlines()

with open('nouns_en.txt') as file:
    nouns = file.readlines()

with open('extensions.txt') as file:
    exts = file.readlines()

def random_adjective():
    index = random.randint(0, len(adjectives) - 1)
    a = adjectives[index].replace('\n', '')
    return a

def random_noun():
    index = random.randint(0, len(nouns) - 1)
    a = nouns[index].replace('\n', '')
    return a

def random_ext():
    index = random.randint(0, len(exts) - 1)
    a = exts[index].replace('\n', '')
    return a

def random_number():
    length = random.randint(1, 5)
    string = ""
    for i in range(length):
        string = string + str(random.randint(0, 9))
    return string

def random_title():
    """
        - 0: fun_file_0
        - 1: file_0
        - 2: file
        - 3: 0
        - 4: FunFile0
        - 5: FunFile
        - 6: File
        - 7: funfile0
        - 8: funfile
        - 9: fun-file-0
        - 10: fun-file
    """
    style = random.choice(list(range(11)))

    ext = random_ext()
    number = random_number()
    adjective = random_adjective()
    noun = random_noun()

    if (style == 0):
        return str(adjective + "_" + noun + "_" + number + "." + ext)
    elif (style == 1):
        return str(adjective + "_" + noun + "." + ext)
    elif (style == 2):
        return str(noun + "." + ext)
    elif (style == 3):
        return str(number + "." + ext)
    elif (style == 4):
        return str(adjective.capitalize() + noun.capitalize() + number + "." + ext)
    elif (style == 5):
        return str(adjective.capitalize() + noun.capitalize() + "." + ext)
    elif (style == 6):
        return str(noun.capitalize() + "." + ext)
    elif (style == 7):
        return str(adjective + noun + number + "." + ext)
    elif (style == 8):
        return str(adjective + noun + "." + ext)
    elif (style == 9):
        return str(adjective + "-" + noun + "-" + number + "." + ext)
    elif (style == 10):
        return str(adjective + "-" + noun + "." + ext)
    else:
        return str(adjective + "_" + noun + "_" + number + "." + ext)

def random_title_folder():
    """
        - 0: fun_file_0
        - 1: file_0
        - 2: file
        - 3: 0
        - 4: FunFile0
        - 5: FunFile
        - 6: File
        - 7: funfile0
        - 8: funfile
        - 9: fun-file-0
        - 10: fun-file
    """
    style = random.choice(list(range(11)))

    ext = random_ext()
    number = random_number()
    adjective = random_adjective()
    noun = random_noun()

    if (style == 0):
        return str(adjective + "_" + noun + "_" + number)
    elif (style == 1):
        return str(adjective + "_" + noun )
    elif (style == 2):
        return str(noun)
    elif (style == 3):
        return str(number)
    elif (style == 4):
        return str(adjective.capitalize() + noun.capitalize() + number)
    elif (style == 5):
        return str(adjective.capitalize() + noun.capitalize())
    elif (style == 6):
        return str(noun.capitalize())
    elif (style == 7):
        return str(adjective + noun + number)
    elif (style == 8):
        return str(adjective + noun)
    elif (style == 9):
        return str(adjective + "-" + noun + "-" + number)
    elif (style == 10):
        return str(adjective + "-" + noun + ".")
    else:
        return str(adjective + "_" + noun + "_" + number)

def create_file(filename):
    size = random.randint(1, 1024 * 1024 * 10 / 16)
    with open(path + "/" + filename, 'w+') as file:
        file.write(str(os.urandom(size)))
        file.close()
    return os.path.getsize(path + "/" + filename)

def create_folder(name):
    os.makedirs(path + '/' + name)

for i in range(nb_files):
    total += create_file(random_title())

for i in range(random.randint(1, 10)):
    name = random_title_folder()
    create_folder(name)
    for i in range(random.randint(1, nb_files / 2)):
        total += create_file(name + "/" + random_title())


print("Generated", str(int(total / 1024 / 1024)), "MO of data :)")
