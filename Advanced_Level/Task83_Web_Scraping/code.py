from bs4 import BeautifulSoup

html = """
<html>
<head><title>Sample Page</title></head>
<body>
    <h1>Data Analytics</h1>
    <p>Learn Web Scraping</p>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print("Title:", soup.title.text)
print("Heading:", soup.h1.text)
print("Paragraph:", soup.p.text)