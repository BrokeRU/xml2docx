from docxtpl import DocxTemplate, RichText
from cgi import escape
import os

# settings
examples_dir = 'examples'
examples_ext = 'xml'

# open template file
doc = DocxTemplate("input.docx")

context = {}

# for file in examples_dir with examples_ext add variable to context
for filename in os.listdir(examples_dir):
    if filename.endswith(examples_ext):
        with open(os.path.join(examples_dir, filename), encoding='utf-8') as file:
            var_name = filename.split('.')[0]
            print(var_name)
            context[var_name] = RichText(file.read())

# save file
doc.render(context)
doc.save("output.docx")

print('Done.')
