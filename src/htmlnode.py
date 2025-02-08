

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        try:
            props = self.props_to_html(self.props)
        except ValueError:
            props = None

        if self.value is None:
            value = None
        else:
            value = "\"" + self.value + "\""

        if self.tag is None:
            tag = None
        else:
            tag = "\"" + self.tag + "\""
        return f"HTMLNode(tag={tag}, value={value}, children={self.children}, props={props})"

    def to_html(self):
        raise NotImplementedError("Child class needs to override")
    def props_to_html(self, props):
        if isinstance(props, dict):
            props_list = list(props)
            props_str = ""
            for prop in props_list:
                props_str += f"{prop}=\"{props[prop]}\" "
            return props_str[:-1]
        else:
            raise ValueError("No dictionary available in HTMLNode.props")
