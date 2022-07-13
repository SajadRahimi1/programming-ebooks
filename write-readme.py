import os
import urllib.parse

add_str = "# Programming Ebooks\n"

for root, directories, files in os.walk("./", topdown=False):
    if ".git" in root or root == "./":
        pass
    else:
        for name in files:
            replacedRoot =  root.replace("./","")
            if "## "+replacedRoot not in add_str:
                add_str =add_str+"\n"+"## "+replacedRoot
            fullPath ="https://github.com/SajadRahimi1/programming-ebooks/blob/main/"+ urllib.parse.quote(replacedRoot+"/" + name)
            add_str = add_str+"\n"+f"- [{name}]({fullPath})"
        add_str+="\n### if your book has copy right and it's in this repo open issue and say it for remove it"     


def writeReadme():
   
    # open original file in read mode and dummy file in write mode
    with open("README.md", 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(add_str + '\n')
        # Read lines from original file one by one and append them to the dummy file

writeReadme()
