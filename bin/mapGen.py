#!/usr/local/bin/python3

# TODO add generation for blog theme and favorite pages.
# Consider adding meta tags for topics and/or favorites

from glob import glob
from os import path as P
import os

FILESDIR = '/home/es3649/workspace/studmane-web/public'

IGNORE = ['.css', '.js', '.ico', '.JPG', '.jpg', '.PNG', '.png', '.map', '.min', 'node_modules', 'blag/dist', 'files/gitignore']

# these variables define the css classes which correspond to these types of files
FOLDER_CLASS = "dir"
FILE_CLASS = "file"

def makeTag(tagType, classes=[], innerHtml="", attributes=dict()):
    """
    makes an html tag with the given stuff
    Arguments:
    tagType (str): the type of the tag: the 'a' in <a>
    class (iter): an iterable with the classes that are on the tab. They appear like so:
        <tagType class="class1 class2 class3">
    innerHtml (str): the things that will appear between the open and close tags, like so:
        <tabType>InnerHTML</tagType>
    attributes (dict): a dictionary of attrigutes to add to the tag:
        <tagType attribute1="value1" attribute2="value2"> (and so on)
    
    Return:
        (str) containing the entire tag
    """
    result = f"<{tagType}"
    if len(classes) != 0:
        result += ' class="'
        for i in range(len(classes)):
            if i != 0:
                result += " "
            result += classes[i]
        result += '"'

    if len(attributes) != 0:
        for key, value in attributes:
            result += f' {key}="{value}"'

    if innerHtml != "":
        result += f">{innerHtml}</{tagType}>"
    else:
        result += f"/>"

    return result

def globDown(path):
    """
    recurses down the directory tree and globs the files
    
    Argument:
    path (str): the path to glob down
    """

    result = "<ul>\n"

    # get the files
    g = P.join(path, '*')
    # print(f"==globbing {g}")
    raw_files = glob(g)
    raw_files.sort()

    # print("  Globbed:", raw_files)

    worked = 0
    
    for f in raw_files:
        # fp = P.join(path, f)
        # print(f)

        # is it a directory...
        if P.isdir(f) and not f in IGNORE:
            # print('  isdir')
            temp_res = globDown(f)
            if temp_res:
                # make the <li> tag, but remove the parent directory names and slash from the folder name
                trimmed = f
                if bool(path):
                    trimmed = f[len(path)+1:]
                result += f'<li class="{FOLDER_CLASS}">{trimmed}/</li>\n'
                result += temp_res
                worked += 1
            continue

        # is it a file...
        if P.isfile(f):

            # do we ignore this file?
            ignore = False
            for i in IGNORE:
                a, ext = P.splitext(f)
                if ext == i:
                    ignore = True
                    break
            
            if not ignore:
                # print('  is not IGNORE file')
                # print the html for this file
                result += f'<li class="{FILE_CLASS}"><a href="{f}">{P.basename(f)}</a></li>\n'
                worked += 1
        
    if worked == 0:
        return ""

    result += "</ul>\n"
    return result
    

def main():
    os.chdir(FILESDIR)
    print('<!DOCTYPE html>')
    print('<html>')
    print('  <head>')
    print('    <meta charset="utf8">')
    print('    <title>studmane.com - Site Map</title>')
    print('    <link rel="stylesheet" href="css/sitemap.css">')
    print('    <link rel="stylesheet" href="css/bootstrap.css">')
    print('    <link href="https://fonts.googleapis.com/css?family=Signika" rel="stylesheet">')
    print('  </head>')
    print('  <body>')
    print('    <div class="container">')
    print('      <div class="row justify-content-center">')
    print('        <div class="col-12-auto">')
    print('          <h1 class="title">Site Map</h1>')
    print('          <p class="disclaimer">(Generated autoamtically from working directory)</p>')
    print('        </div>')
    print('      </div>')
    print()
    print('      <div class="row justify-content-center">')
    print('        <div class="col-12-auto">')

    print(globDown(''))

    print('        </div>')
    print('      </div>')
    print('    </div>')
    print('  </body>')
    print('</html>')


    

if __name__ == "__main__":
    main()
