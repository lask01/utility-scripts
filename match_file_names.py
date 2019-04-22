# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 19:26:05 2019

@author: lask01
"""

import os
import re


def match_file_names_in_directory_structure(root_path, regex):
    """
    Recurses a given directory location and returns a list of files whose names
    match a given regular expression.
    
    Args:
        root_path: A string directory location.
        regex: A string regular expression pattern to match.
        
    Returns:
        A list of list of file names that match regex.
    
    Raises:
        OSError: If the root_path is not found.
    """
    # This is checked in os.walk, but made explicitly fatal here so that a
    # non-existant string path raises an exception instead of returning an
    # empty list.
    if not os.path.isdir(root_path):
        raise OSError("Root directory not found")
    
    if regex == "":
        return []
    
    compiled_expression = re.compile(regex)
    matching_file_names = []
    
    for top_path, subdirs, files in os.walk(root_path):
        for filename in files:
            all_matches = compiled_expression.findall(filename)
            if all_matches:
                matching_file_names.append(filename)
            else:
                continue
            
    return matching_file_names
            

if __name__=="__main__":

    dir_root_path = input("Enter directory: ")
    regex = input("Enter regex: ")
    matches = match_file_names_in_directory_structure(dir_root_path, regex)
    print(matches)
