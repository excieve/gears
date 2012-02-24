import os
from .base import ExecCompiler


SOURCE = '\n'.join((
    "(function() {",
    "  var template  = Handlebars.template,",
    "      templates = Handlebars.templates = Handlebars.templates || {};",
    "  templates['%(name)s'] = template(%(source)s);",
    "}).call(this);"))


class HandlebarsCompiler(ExecCompiler):

    result_mimetype = 'application/javascript'
    executable = 'node'
    params = [os.path.join(os.path.dirname(__file__), 'handlebars.js')]

    def process(self, asset):
        super(HandlebarsCompiler, self).process(asset)
        asset.processed_source = SOURCE % {
            'name': asset.attributes.path_without_suffix,
            'source': asset.processed_source}