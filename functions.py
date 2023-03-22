FILEPATH = "todofile.txt"

def showlist(functionlist):
    """Function to print out the todolist in a decent format"""
    for count, i in enumerate(functionlist):
        i = i.strip('\n')
        print(f'{count + 1}.{i}')


def fileread(filepath=FILEPATH):
    """Read the text file containing the todo list, return a list of todos"""
    with open(filepath, 'r') as todo_read:
        readtodos = todo_read.readlines()
    return readtodos


def filewrite(todos_arg, filepath=FILEPATH):
    """Write the modified todolist to a 'todofile.txt' textfile """
    with open(filepath, 'w') as todo_write:
        todo_write.writelines(todos_arg)


#This is an if statement that checks of the file is run in the main frame or no-
# if it is, it prints hello, if the file is imported and run by other file, then print will not be executed

def count(phrase):
    return phrase.count('.')


if __name__ == '__main__':
    print("Hello from functions")