from textnode_to_htmlnode import textnode_to_htmlnode
from textnode import TextNode, TextType


def test(node):
    print(textnode_to_htmlnode(node))
    
if __name__ == "__main__":
    node_list = [
        TextNode("Hello, World!", TextType.NORMAL),
        TextNode("BOLD TEXT", TextType.BOLD),
        TextNode("italic text", TextType.ITALIC),
        TextNode("print(\"Hello, World!\")", TextType.CODE),
        TextNode("google.com", TextType.LINK, url="https://google.com"),
        TextNode("This is my favorite image", TextType.IMAGE, url="https://google.com/image")
    ]
    for node in node_list:
        test(node)
