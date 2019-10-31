import os
import sys
import markdown

#if len(sys.argv)-1 != 3:
#    print("Invalid usage. Try: sirdrcaptain <html template> <markdown dir> <output dir>")

templateFilePath = "/Users/azh/Dropbox/SirDrCaptain/example/template.html"
mdFolderPath = "/Users/azh/Dropbox/SirDrCaptain/example/posts"
outputPath = "/Users/azh/Dropbox/SirDrCaptain/example/output/"
pages = {}

# Process the template.
fo = open(templateFilePath)
# TODO: Handle errors.
template = fo.read()

# Process each post.
for mdFileName in os.listdir(mdFolderPath):
    if not mdFileName.endswith(".md"):  # Only read md files.
        continue
    fo = open(os.path.join(mdFolderPath, mdFileName))
    # TODO: What if file does not have 3 lines?
    title = fo.readline().strip()
    date = fo.readline().strip()
    content = fo.read().strip()
    fo.close()

    html = markdown.markdown(content) 
    pageName = mdFileName.rsplit('.', 1)[0]  # Remove file extension from file name.
    pages[pageName] = (title, date, html) # Store all the info from the page.

    # Output!

fo = open(templateFilePath)


# Commands: @@@content@@@ @@@title@@@ @@@date@@@ @@@list ascending@@@ @@@list descending@@@

    

#html = markdown.markdown("*austin*\n\n**henley**")
#print(html)

# sirdrcaptain <template file> <dir of markdown files> <dir for output>

# get template html file
# get recursive folder of md files... title first line, date second line
# replace %%%CONTENT%%%
# replace %%%TOC%%%