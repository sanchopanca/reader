from jinja2 import Environment, PackageLoader


env = Environment(loader=PackageLoader('books', 'templates'))


def render_template(template_name, **kwargs):
    template = env.get_template(template_name)
    return template.render(**kwargs)