## How-to

Create these folders:

```
- gh_pages (a clone of https://github.com/lindsay-stevens/lindsay-stevens.github.io)
- gh_pages_pelican (a clone of this repo)
- venv (a py3.6 venv with "pip install pelican markdown" run in it)
```

- Update or add to `gh_pages_pelican/content/pages` Markdown files
  - It's possible to also do blog posts but not in use currently
- With venv active, (re)run `pelican content` from the repo root
- With the venv active, run `python -m pelican.serve` from the `output` folder
- When ready to publish:
  - Run `publish.bat`
  - Copy `pub_out` files over `gh_pages` files
  - Commit & push `gh_pages`


Refs: 

- Pelican docs: http://docs.getpelican.com/en/stable/index.html
- Flex theme: https://github.com/alexandrevicenzi/Flex
