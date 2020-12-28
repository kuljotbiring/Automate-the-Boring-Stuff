import shutil

"""first parameter is name of file. second is where you want to copy to"""
# shutil.copy('./hello.txt', ./mydocuments/coolfolder)

"""you can also use copy to rename at the same time"""
# shutil.copy('./hello.txt', ./mydocuments/coolfolder/spam.txt)

"""to copy multiple files you can use copy tree
    first param is what you wanna copy and second what you want to save it as"""
# shutil.copytree('c:\\delicious', 'c:\\delicious\backup')

"""Move file to new location"""
# shutil.move('c:\\span,txt', 'c:\\delicious\\walnut')

"""rename a file just use move but in same directory"""
# shutil.move('c:\\delicious\\walnut\\spam.txt', 'c:\\delicious\\walnut\\eggs.txt')
