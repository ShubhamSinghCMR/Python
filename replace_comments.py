import os

# Define the comment block to replace
comment_block = """# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shuup Commerce Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree."""

# Replace the block with a single whitespace
replacement = " "

def replace_comment_block_in_file(file_path):
    """Replace the specified comment block in a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the comment block with a single whitespace
    updated_content = content.replace(comment_block, replacement)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

def traverse_directory(directory):
    """Traverse the directory and replace comment block in all files."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Process all files
            replace_comment_block_in_file(file_path)

if __name__ == "__main__":
    # Define your project folder path
    project_folder = r"C:\Users\DArk Lord\Documents\GitHub\Python-Projects\Project 7 - E-Commerce Platform"
    
    # Run the traversal and replacement
    traverse_directory(project_folder)
    print("Replacement complete.")
