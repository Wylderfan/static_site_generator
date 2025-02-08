from leafnode import LeafNode
from textnode import TextType

def has_url(url):
    if url is not None:
        return True
    raise ValueError("TextNode needs a url")

def textnode_to_htmlnode(textnode):
    match textnode.text_type:
        case TextType.NORMAL:
            return LeafNode(value=textnode.text) 
        case TextType.BOLD:
            return LeafNode(tag="b", value=textnode.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=textnode.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=textnode.text)
        case TextType.LINK:
            href_dict = {}
            if has_url(textnode.url):
                href_dict["href"] = textnode.url
            return LeafNode(tag="a", value=textnode.text, props=href_dict)
        case TextType.IMAGE:
            img_dict = {}
            if has_url(textnode.url):
                img_dict["src"] = textnode.url
                img_dict["alt"]= textnode.text
            return LeafNode(tag="img", value="", props=img_dict)
        case _:
            raise ValueError("TextNode needs a TextType value")
