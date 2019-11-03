# SirDrCaptain

SirDrCaptain is a very simple *static website generator* written in Python. I made it for my generating my [blog](http://web.eecs.utk.edu/~azh/blog.html) and even wrote a [tutorial](http://web.eecs.utk.edu/~azh/blog/staticwebsitegenerator.html) on making it.

The features include:

 - Write posts using Markdown
 - Separate post content from HTML
 - Automatically update lists of posts 
 - Generate RSS feed (coming soon, maybe)
 
You need an HTML file that will act as your template and a set of markdown files (one for each page). Then SirDrCaptain will convert the markdown to HTML and fill in each post's content, title, and date along with any lists of posts into the template. You also need to provide another HTML file that will be used for each item in listings of posts (e.g., table of contents or recent posts in chronological order). This will often just be a line containing something like `<li>@@@title@@@</li>`.
 
The [/example/](https://github.com/AZHenley/SirDrCaptain/tree/master/example) directory has an example of this.
 
SirDrCaptain is a glorified *find-and-replace* tool, looking for:
 
 - @@@content@@@ inserts the converted markdown content
 - @@@title@@@ inserts the post's title 
 - @@@date@@@ inserts the post's date
 - @@@filename@@@ inserts the post's resulting HTML filename
 - @@@list ascending@@@ inserts a list of all posts in ascending order by date
 - @@@list decending@@@ inserts a list of all posts in decending order by date
  
To run it: `sirdrcaptain <html template> <toc template> <markdown dir> <output dir>` 
  
There are a number of assumptions that SirDrCaptain makes. Each markdown file must have the post title in the first line, the date in the second line, and the content is everything else. The dates are in %m/%d/%Y format. The ToC template can use the same @@@ annotations, except the list ones.
  
**TODO:**

 - Handle errors.
 - Refactor code.
 - Generate RSS feed.
 - Make ToC template (and eventually RSS template) optional.
