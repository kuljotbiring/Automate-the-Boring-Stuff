import os
import shutil

# get the current working directory
os.getcwd()

"""one method to delete is os.unlink"""
# os.unlink('bacon.txt')

"""delete a folder using os.rmdir - the folder must be completely empty"""
# os.rmdir('./myCoolFolder')

"""Need to use shutil module to recursively remove folder with stuff in it"""
# shutil.rmtree('./myCoolFolder')