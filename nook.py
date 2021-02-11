#!/usr/bin/python

import sys
import os
import shutil
import time


def del_node_modules(base_dir):
    paths_to_del = []
    dir_name = os.path.dirname(base_dir)
    if dir_name == 'node_modules':
        paths_to_del.append(base_dir)
        return

    # base_dir = '/Users/abdulaliyev/web-projects/react'
    os.chdir(base_dir)
    folder_items = os.listdir(os.getcwd())

    def loopThroughDir(pathName):
        # get a list of items
        inner_folder_items = os.listdir(pathName)

        # loop through list of items
        for item in inner_folder_items:
            full_path_name = pathName + '/' + item
            if item == 'node_modules' and os.path.isdir(full_path_name):
                paths_to_del.append(full_path_name)
            else:
                if os.path.isdir(full_path_name):
                    loopThroughDir(full_path_name)

    for item in folder_items:
        itemPath = base_dir + '/' + item
        if os.path.isdir(itemPath):
            loopThroughDir(itemPath)

    print('paths_to_del = before ')
    print(paths_to_del)

    for path in paths_to_del:
        print('>> Deleting ' + path)
        shutil.rmtree(path)
        time.sleep(1)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1]:
        if sys.argv[1] == '-h' or sys.argv[1] == '--h' or sys.argv[1] == '-help' or sys.argv[1] == '--help':
            print(
                'This app loops thgouth all subfolders and deletes all node_modules folders within it.')
            print("")
            print('To use this app, get a directory path pwd for a folder within which you want to delete all the node_modules folders.')
            print(
                "Use the app as follows: python nook.py '/Users/abdulaliyev/web-projects/'")
            print("You can also pass a list of folders separated by comma, for example: python nook.py '/Users/abdulaliyev/folder1/','/Users/abdulaliyev/folder2','/Users/abdulaliyev/folder3/'")
        else:
            list_of_paths = sys.argv[1].split(",")
            list_of_paths = list(map(lambda x: x.strip(), list_of_paths))
            for pathItem in list_of_paths:
                del_node_modules(pathItem)
    else:
        print('Please provide base path of the directory')
