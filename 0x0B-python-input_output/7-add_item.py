#!/usr/bin/python3
""" adds all arguments to a Python list, and then save them to a file """


if __name__ == "__main__":
    import sys
    import ('5-save_to_json_file').save_to_json_file
    import ('6-load_from_json_file').load_from_json_file

    try:
        arg_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        arg_list = []

    arg_list.extend(sys.aragv[1:])

    save_to_json_file(arg_lists, add_item.json)
