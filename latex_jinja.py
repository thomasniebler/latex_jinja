import jinja2
import os


env = jinja2.Environment(
    block_start_string='<BLOCK>',
    block_end_string='</BLOCK>',
    variable_start_string='<VAR>',
    variable_end_string='</VAR>',
    trim_blocks=True,
    loader=jinja2.FileSystemLoader(os.path.abspath("latex_templates"))
)

template = env.get_template("latex_template.tex")
print(template.render(my_var="hund"))
