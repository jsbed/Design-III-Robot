import fnmatch
import os
import subprocess
import sys


# Define Pyside converters command line
PysideUIC = "pyside-uic"
PysideRCC = "pyside-rcc"


def createPackageFolder(folder_fullpath):
    """ Create a package folder with the appropriate __init__.py file."""    
    
    # Ensure folder exist
    if not os.path.exists(folder_fullpath):
        os.makedirs(folder_fullpath)
    
    # Ensure package file exist
    package_filename = os.path.join(folder_fullpath, "__init__.py" )
    if not os.path.exists(package_filename):
        open(package_filename, 'w').close()


def uicFile(folder_fullpath, filename):
    """ Run the Qt ui converter tool on a specific file."""
    
    # Ensure package folder exist
    createPackageFolder(os.path.join(folder_fullpath, "GeneratedFiles"))
    
    # Set proper file input and output
    input_fullpath = os.path.join(folder_fullpath, filename) 
    output_fullpath = os.path.join(folder_fullpath, "GeneratedFiles", os.path.splitext(filename)[0] + ".py")
        
    # Execute uic tool
    print("  -  " + input_fullpath)
    subprocess.call([PysideUIC, input_fullpath, "-o", output_fullpath])

def qrcFile(folder_fullpath, filename):
    """ Run the Qt qrc converter tool on a specific file."""
    
    # Ensure package folder exist
    createPackageFolder(os.path.join(folder_fullpath, "GeneratedFiles"))
    
    # Set proper file input and output
    input_fullpath = os.path.join(folder_fullpath, filename) 
    output_fullpath = os.path.join(folder_fullpath, "GeneratedFiles", os.path.splitext(filename)[0] + "_rc.py")
        
    # Execute rcc tool
    print("  -  " + input_fullpath)
    subprocess.call([PysideRCC, input_fullpath, "-o", output_fullpath])

# Location to run UI convert will be passed to us by parameter
location = sys.argv[1]

print("Converting all .ui and .qrc files in " + location)

# Find every ui/qrc file that is under the project folder
for root, dirnames, filenames in os.walk(location):
    for filename in fnmatch.filter(filenames, '*.ui'):
        uicFile(root, filename)
    
    for filename in fnmatch.filter(filenames, '*.qrc'): 
        qrcFile(root, filename)  
    
print()
print("Completed!")        