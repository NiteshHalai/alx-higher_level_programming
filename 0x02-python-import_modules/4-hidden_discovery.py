#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4
    
list_of_names = dir(hidden_4)
for i in list_of_names:
    if i[2] != '_':
        print(i)
