#!/usr/bin/env python3
"""Build a static copy of this repo that the docs preview can run from on GitHub Pages.

Locally, the preview runs on `python3 -m http.server` (see .claude/launch.json), and its
folder browser parses that server's auto-generated directory listings. GitHub Pages has no
directory listings, so this script writes an equivalent listing page (same `<ul><li><a>`
shape python emits) as `index.html` in every folder. With those in place, the preview
works unchanged on Pages.

It also publishes `.preview/` as `preview/`, because the Pages upload step skips
dot-folders.

Usage: python3 .preview/build_site.py <output-dir>
"""
import html
import os
import shutil
import sys
import urllib.parse

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = {'.git', '.github', '.claude', '.DS_Store', '_site'}

ROOT_REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta http-equiv="refresh" content="0; url=preview/index.html" />
<script>location.replace('preview/index.html');</script>
<title>Redirecting…</title>
</head>
<body>
<p>Redirecting to <a href="preview/index.html">the docs preview</a>…</p>
</body>
</html>
"""


def listing_html(entries):
    items = []
    for name, is_dir in entries:
        href = urllib.parse.quote(name) + ('/' if is_dir else '')
        label = html.escape(name) + ('/' if is_dir else '')
        items.append('<li><a href="%s">%s</a></li>' % (href, label))
    return ('<!DOCTYPE html>\n<html><head><meta charset="utf-8"><title>Directory listing</title>'
            '</head><body><ul>\n%s\n</ul></body></html>\n' % '\n'.join(items))


def main(out_dir):
    out_dir = os.path.abspath(out_dir)
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)

    def ignore(src, names):
        ignored = {n for n in names if n in SKIP}
        if os.path.abspath(src) == REPO_ROOT:
            ignored |= {'.preview', 'index.html'}
        return ignored

    shutil.copytree(REPO_ROOT, out_dir, ignore=ignore)
    shutil.copytree(os.path.join(REPO_ROOT, '.preview'), os.path.join(out_dir, 'preview'),
                    ignore=shutil.ignore_patterns('*.py'))
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(ROOT_REDIRECT)

    count = 0
    for dirpath, dirnames, filenames in os.walk(out_dir):
        if dirpath == out_dir or 'index.html' in filenames:
            continue  # the root and preview/ already have a real index.html
        entries = sorted([(d, True) for d in dirnames] + [(f, False) for f in filenames],
                         key=lambda e: e[0].lower())
        with open(os.path.join(dirpath, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(listing_html(entries))
        count += 1
    print('Built %s (%d folder listings)' % (out_dir, count))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('usage: build_site.py <output-dir>')
    main(sys.argv[1])
