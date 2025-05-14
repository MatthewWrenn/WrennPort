from pathlib import Path #importing the path libs

rootDir = Path("files") #setting the files directory as the root path.
filePath = rootDir.iterdir() #getting the  files in the root directory.

for path in filePath: #For loop for each file in the dir
    newFileName = f"It1-  {path.stem} {path.suffix}" #an F-string to rename the files
    newFilePath = path.with_name(newFileName) #file path to use the /files directory
    path.rename(newFilePath)#renaming the files