import datetime
import os

import yaml


def entry_to_xml(title: str, link: str, updated: str):
    header = "<entry>"
    title = f"""<title type="html"><![CDATA[{title}]]></title>"""
    id = f"""<id>{link}</id>"""
    updated = f"""<updated>{updated}</updated>"""
    content = f"""<content type="html"><![CDATA[<iframe src="{link}"></iframe>]]></content>"""
    link = f"""<link href="{link}"></link>"""
    footer = "</entry>"
    return "\n".join([header, title, id, link, updated, content, footer])


with open("feed.yaml", "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)

header = f"""
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <id>https://github.com/Gudsfile/Pochurl</id>
    <title>Pochurl - what do I have to read?</title>
    <updated>{datetime.datetime.now().isoformat()}</updated>
    <generator>https://github.com/Gudsfile/Pochurl</generator>
    <icon>https://en.wikipedia.org/static/favicon/wikipedia.ico</icon>
"""

feed = ""

feed = "\n".join([entry_to_xml(**entry) for entry in data["entry"]])

footer = """
</feed>
"""

content = f"""
{header}
{feed}
{footer}
"""

if not os.path.exists("public"):
    os.mkdir("public")

with open("public/feed.xml", "w", encoding="utf-8") as file:
    file.write(content)
