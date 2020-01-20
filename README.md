# mkdocs-markdownextradata-plugin

A MkDocs plugin that render meraid graph to mermaid style


## Installation


Install the package with pip:

```bash
pip install git+https://github.com/sebastienwarin/mkdocs-mermaid-plugin
```

## Usage

Enable this plugin in your `mkdocs.yml`:

```yaml
plugins:
    - markdownmermaid

extra_javascript:
    - https://unpkg.com/mermaid@8.4.5/dist/mermaid.min.js
```

> **Note:** Don't forget to include the mermaid.min.js (local or remotely) in your `mkdocs.yml`

To override the [default options](https://mermaid-js.github.io/mermaid/#/mermaidAPI?id=mermaidapi), declare them in you `mkdocs.yml` file.

For example :

```yaml
plugins:
    - markdownmermaid:
        init_options:
            - startOnLoad: true
            - theme: "forest"
            - themeCSS: ".node rect { fill: red; }"
            - flowchart:
                - curve: "cardinal"
                - useMaxWidth: true

```

More information about mermaid in the [Mermaid documentation](https://mermaid-js.github.io/mermaid/)
More information about plugins in the [MkDocs documentation][mkdocs-plugins]



[mkdocs-plugins]: http://www.mkdocs.org/user-guide/plugins/