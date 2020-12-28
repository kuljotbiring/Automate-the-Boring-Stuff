import os

"""os.walk returns the root folder you want to check use in a for loop
    returns 3 values; name of folder, its subfolders as a list and list of files in folder"""

for folderName, subfolders, filenames in os.walk('/Users/kj/Desktop/Certificates/Automate the Boring Stuff'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

    """Now we can do stuff to all this"""
    for subfolder in subfolders:
        if 'fish' in subfolder:
            os.rmdir(subfolder)

    for file in filenames:
        if file.endswith('.py'):
            continue # can have it do something here like shutil.copy()
