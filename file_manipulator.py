import sys

class CommandError(Exception):
    pass

def validate_inputpath(inputpath):
    try:
        f = open(inputpath)
    except FileNotFoundError:
        print('!!! FileNotFoundError !!!')
        print('the file [' + inputpath + '] is not faound.')
        sys.exit('Error')
    f.close()

def reverse(inputpath, outputpath):
    contents = ''
    with open(inputpath) as f:
        contents = f.read()
    with open(outputpath, 'w') as f:
        f.write(contents[::-1])

def copy(inputpath, outputpath):
    contents = ''
    with open(inputpath) as f:
        contents = f.read()
    with open(outputpath, 'w') as f:
        f.write(contents)

def duplicate(inputpath, n):
    contents = ''
    with open(inputpath) as f:
        contents = f.read()
    with open(inputpath, 'a') as f:
        for _ in range(n):
            f.write(contents + '\n')

def replace(inputpath, needle, newstring):
    contents = ''
    with open(inputpath) as f:
        contents = f.read()
    if needle in contents:
        contents = contents.replace(needle, newstring)
    with open(inputpath, 'w') as f:
        f.write(contents)

def main():
    command = sys.argv[1]
    inputpath = sys.argv[2]
    validate_inputpath(inputpath)
    if command == 'reverse':
        outputpath = sys.argv[3]
        reverse(inputpath, outputpath)
    elif command == 'copy':
        outputpath = sys.argv[3]
        copy(inputpath, outputpath)
    elif command == 'duplicate-contents':
        try:
            n = int(sys.argv[3])
        except ValueError as ex:
            print("Do not input str: {}".format(ex))
            sys.exit()
        duplicate(inputpath, n)
    elif command == 'replace-string':
        needle = sys.argv[3]
        newstring = sys.argv[4]
        replace(inputpath, needle, newstring)
    else:
        raise CommandError(command)

    
if __name__ == '__main__':
    main()