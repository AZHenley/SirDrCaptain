# SirDrCaptain - super simple static website generator
# Follow the tutorial on making this: http://web.eecs.utk.edu/~azh/blog/staticwebsitegenerator.html
# Austin Z. Henley (2019)

# TODO:
#   Handle errors.
#   Refactor code into functions.
#   Generate RSS feed.
#   Make ToC template optional.

import os
import sys
import datetime
import markdown

if len(sys.argv)-1 != 4:
    print("Invalid usage. Try: python sirdrcaptain.py <html template> <toc template> <markdown dir> <output dir>")
    sys.exit(1)

templateFilePath = sys.argv[1]
tocFilePath = sys.argv[2]
mdFolderPath = sys.argv[3]
outputPath = sys.argv[4]
pages = {}

# Process the template.
fo = open(templateFilePath)
template = fo.read()
fo.close()

# Process each post. Convert MD to HTML then insert it into template.
for mdFileName in os.listdir(mdFolderPath):
    if not mdFileName.endswith(".md"):  # Only read md files.
        continue

    # For each MD file, first line is title, second is date, the rest is content.
    fo = open(os.path.join(mdFolderPath, mdFileName))
    title = fo.readline().strip()
    date = fo.readline().strip()
    content = fo.read().strip()
    fo.close()

    html = markdown.markdown(content) # MD -> HTML.
    pageName = mdFileName.rsplit('.', 1)[0]  # Remove file extension from file name.
    pages[pageName] = (title, date, html) # Store all the info from the page.

    # Replace annotations in the template with the contents.
    output = template.replace("@@@content@@@", html)
    output = output.replace("@@@title@@@", title)
    output = output.replace("@@@date@@@", date)
    outout = output.replace("@@@filename@@@@", pageName + ".html")
    fo = open(os.path.join(outputPath, pageName + ".html"), "w") # Write out an HTML file, one for each MD file.
    fo.write(output)
    fo.close()

# Build table of contents list.
fo = open(tocFilePath, "r")
tocTemplate = fo.read()
fo.close()
toc = []
for page in pages:
    # Replace annotations in the ToC template with the contents.
    tocEntry = tocTemplate.replace("@@@title@@@", pages[page][0])
    tocEntry = tocEntry.replace("@@@date@@@", pages[page][1])
    tocEntry = tocEntry.replace("@@@filename@@@", page + ".html")
    toc.append((tocEntry, datetime.datetime.strptime(pages[page][1], "%m/%d/%Y").date())) # Convert our American date strings into a date object.
toc.sort(key = lambda t: t[1]) # Sort by the dates.
tocAscending = "".join([t[0] for t in toc]) # Convert to string and drop the date object.
toc.reverse()
tocDescending = "".join([t[0] for t in toc]) # Don't know if we need ascending or descending.

# Reprocess pages for ToC annotations.
for page in pages:
    fo = open(os.path.join(outputPath, page + ".html"), "r")
    content = fo.read()
    fo.close()

    content = content.replace("@@@list ascending@@@", tocAscending) 
    content = content.replace("@@@list descending@@@", tocDescending)
    fo = open(os.path.join(outputPath, page + ".html"), "w")
    fo.write(content)
    fo.close()

# Commands: @@@content@@@ @@@title@@@ @@@date@@@ @@@filename@@@ @@@list ascending@@@ @@@list descending@@@
