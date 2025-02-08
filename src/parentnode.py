from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag value")
        elif self.children is None:
            raise ValueError("ParentNode must have a children value")
        
        start_tag = f"<{self.tag}>"
        end_tag = f"</{self.tag}>"
        value = ""

        for node in self.children:
            value = value + node.to_html()

        return f"{start_tag}{value}{end_tag}"

