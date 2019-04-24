#!/usr/bin/env python3

#This file will search every part of a given directory, and produce a directory tree.
#As an optional, you can even search for file(s)/folder(s). The Results will be shown on the directory tree AND on plane text below it.


import os

class dirtree():
    indent = 0
    path_ext = ''
    found_keywords = []

    #The optional params(which are 'search' and 'keyword' are used to determine whether the user wants to search or not.
    def __init__(self, starting_path, **kwargs): 
        self.starting_path = starting_path
        self.kwargs = kwargs

    #This will start the directory tree/file search
    def startDirTree(self): 
        try:
            #Get the filenames and foldernames
            for (dirpath, foldernames, filenames) in os.walk(self.starting_path + self.path_ext):
                break

            if self.indent != 0: #if indent is 0, then that means file/folder naming is on the first column. Dont print this out if so
                print("   " * self.indent + "|")

            if len(filenames) == 0: #if there are no files, write NONE
                print("   " * self.indent + "|`--*EMPTY*")
            else:
                for file in filenames:
                    try: #Sometimes kwargs will not contain any key, so try to look for it. If there is nothing, do the stuff under except
                        if self.kwargs["search"] == "yes" and self.kwargs["keyword"] == file[:len(self.kwargs["keyword"]) + 1]: #If 'search' = 'yes' and 'keyword' = the first few characters (or all) of the file name being currently looked at
                            if self.indent != 0:
                                print("   " * self.indent + "|`--{} [FILE]".format(file) + " <---- *FILE FOUND*")
                            else:
                                print("{} [FILE]".format(file) + " <---- *FILE FOUND*")
                            self.found_keywords.append(self.starting_path + self.path_ext) #Add the directory location to a list. There might be more files that fit this specific keyword
                        else:
                            print("   " * indent + "{} [FILE]".format(file))
                        
                    except:
                        if self.indent != 0:
                            print("   " * self.indent + "|`--{} [FILE]".format(file))
                        else:
                            print("{} [FILE]".format(file))
            
            if self.indent != 0:        
                print("   " * self.indent + "|")
            
            for folder in foldernames:
                try: #if keys are not set, then pass this
                    if self.kwargs["search"] == "yes" and self.kwargs["keyword"] == folder[:len(self.kwargs["keyword"]) + 1]: #If 'search' = 'yes' and 'keyword' = the first few characters (or all) of the folder name being currently looked at
                        print("   " * self.indent + "{} [FOLDER]".format(folder) + " <---- *FOLDER FOUND*")
                        self.found_keywords.append(self.starting_path + self.path_ext)
                    else:
                        print("   " * self.indent + "{} [FOLDER]".format(folder))
                except:  
                    print("   " * self.indent + "{} [FOLDER]".format(folder))
                    
                self.path_ext += '/' + folder #Add folder name to end of directory. This is for recursion to work
                self.indent += 1 #This is for formatting

                #When the recursive function starts to return true, that means we need to un-indent and go back a directory
                if self.startDirTree() == True:
                    self.path_ext = self.path_ext[:len(self.path_ext) - (len(folder) + 1)] #Remove the last bit of the current directory
                    self.indent -= 1 #Un-indent
                    
            return True
        except:
            print("Something went wrong... are you sure the directory is correct?")

#This function will start the user interface, if preferred. Helps makes things slightly more intuitive
def enableInterface():
    while 1:
        starting_path = input("What directory would you like to scan? Note: Don't forget the starting forward-slash if applicable! ")
        kwargs = input("Would you like to search for a file/folder? (yes/no) ")
        if kwargs == "yes":
            word = input("What is the keyword that you would like to look for? ")
            tree = dirtree(starting_path, search = "yes", keyword = word)
            tree.startDirTree()
            print("Keywords have been found in these directories:")
            for foundEntities in tree.found_keywords:
                print(foundEntities)
        else:
            tree = dirtree(starting_path)
            tree.startDirTree()

    
    
enableInterface()
        
#If doing things manually is preferred, comment out the above enableInterface() and use the below comments as a template:

#If you plan on searching for something:
#tree = dirtree('[DIRECTORY]', search = "yes", keyword = "[ENTER KEYWORD]")
#tree.startDirTree()
#print(tree.found_keywords)

#If you plan on NOT searching:
#tree = dirtree('[DIRECTORY]')
#tree.startDirTree()
