

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        output = ""
        if self.props is None:
            return output

        for k, v in self.props.items():
            output += f' {k}="{v}"'

        return output

    def __repr__(self):
        output = "HTMLNode:\n"
        output += f"\ttag: {self.tag}\n"
        output += f"\tvalue: {self.value}\n"
        output += f"\tchildren: {self.children}\n"
        output += f"\tprops: {self.props}\n"

        return output


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value is required")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is required")

        if self.children is None:
            raise ValueError("chilren is required")

        output = f"<{self.tag}{self.props_to_html()}>"
        for node in self.children:
            output += node.to_html()
        output += f"</{self.tag}>"

        return output
