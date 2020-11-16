import markdown
import jinja2
import os
from os.path import splitext

TEMPLATE_FILE = "post.html"
markdown_posts = os.listdir('markdown')

for file in markdown_posts:
    with open("markdown/%s" % file) as f:
        content = f.read()

    title = ' '.join(word.title() for word in file[:-3].split('-'))
    
    md = markdown.markdown(content, extensions=['codehilite'])

    template_loader = jinja2.FileSystemLoader(searchpath="templates")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(TEMPLATE_FILE)
    output = template.render(title=title, content=md)

    html_filename = splitext(file)[0] + '.html'

    with open('blog/%s' % html_filename, 'w+') as f:
        f.write(output)