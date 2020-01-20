from mkdocs.plugins import BasePlugin
from bs4 import BeautifulSoup
import json

try:
    unicode
except NameError:
    # Python 3 doesn't have `unicode` as `str`s are all Unicode.
    unicode = str

class MarkdownMermaidPlugin(BasePlugin):

    def transform_options(self, source, toJson = True):
        options = {}
        for opt in source:
            option = {}
            for key, value in opt.items():
                option[key] = self.transform_options(value, False) if isinstance(value, list) else value
            options.update(option)
        return json.dumps(options) if toJson else options
   
    def on_post_page(self, output_content, config, **kwargs):
        soup = BeautifulSoup(output_content, 'html.parser')
        mermaids = soup.find_all("code",class_="mermaid")
        for mermaid in mermaids:
            # replace code with div
            mermaid.name = "div"
            # replace <pre> 
            mermaid.parent.replace_with(mermaid)

        if mermaids:
            new_tag = soup.new_tag("script")
            if 'init_options' in self.config:
                new_tag.string = "mermaid.initialize({config});".format(config=self.transform_options(self.config['init_options']))
            else:
                new_tag.string = "mermaid.initialize({startOnLoad:true});"
            soup.body.append(new_tag)
            
        return unicode(soup)