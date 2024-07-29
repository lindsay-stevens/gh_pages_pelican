## How-to

Create these folders:

```
- gh_pages (a clone of https://github.com/lindsay-stevens/lindsay-stevens.github.io)
- gh_pages_pelican (a clone of this repo)
- venv (a py3.12 venv with "pip install -r requirements.txt" run in it)
```

- Update or add to `gh_pages_pelican/content/pages` Markdown files
  - It's possible to also do blog posts but not in use currently
- With venv active, (re)run `pelican content` from the repo root
- With the venv active, run `pelican --listen` from the repo root
- When ready to publish:
  - Run `pelican content -o pub_out -s .\publishconf.py`
  - Copy `pub_out` files over `gh_pages` files
  - Commit & push `gh_pages`

Convert pages to ODT for formatting as a Resume (powershell):

```
pandoc.exe -f markdown -t odt -o resume.odt (get-item .\content\pages\*.md).FullName
```

Refs: 

- Pelican docs: http://docs.getpelican.com/en/stable/index.html
- Flex theme: https://github.com/alexandrevicenzi/Flex
  - To update, clone latest tag into `.\themes` folder, update `pelicanconf.py` refs
