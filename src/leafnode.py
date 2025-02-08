from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value

        if self.props is None:
            start_tag = f"<{self.tag}>"
        else:
            start_tag = f"<{self.tag} {self.props_to_html(self.props)}>" 
        end_tag = f"</{self.tag}>"
        return f"{start_tag}{self.value}{end_tag}"
        

