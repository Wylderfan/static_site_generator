from textnode import TextNode
from textnode import TextType

text_type = TextType.ITALIC
text = "Hello, World!"

print(TextNode(text, text_type, "https://youtube.com"))
