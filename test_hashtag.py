import markdown

text = """\
# Heading

#hashtag at beginning of line and #within line.

This is no#hashtag. 

#Markdown
<style>
a.hashtag {
  background-color: #e0e0e0;      /* hellgrauer Hintergrund */
  border-radius: 4px;             /* abgerundete Ecken */
  padding: 2px 6px;               /* innen etwas Abstand */
  color: #3b6ea5;                /* blaue Farbe für Links */
  text-decoration: none;          /* keine Unterstreichung */
  font-weight: 500;               /* etwas fetter */
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

a.hashtag:hover {
  background-color: #cfd8dc;      /* dunkleres Grau beim Hover */
  text-decoration: underline;     /* Unterstreichung beim Hover */
}
</style>
"""

html = markdown.markdown(text,
    extensions=["hashtag"],
    extension_configs={
        "hashtag": {
            "base_url": "https://tags.example.com/",
            "span_class": "hashtag"
        }
    }
)

print(html)
