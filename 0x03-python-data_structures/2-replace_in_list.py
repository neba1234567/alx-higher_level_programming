#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
	my_list.pop(idx)
	my_list.insert(idx, element)
        return my_list
