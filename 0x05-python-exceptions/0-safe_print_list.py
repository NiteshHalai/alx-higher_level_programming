
def safe_print_list(my_list=[], x=0):
    for i in range (0, x):
        try:
            print(my_list[i], end='')
        except:
            sys.exit(1)
    return x
