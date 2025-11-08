from textnode import TextType


class HTMLNode:
    def __init__(self, tag: str=None, value: str=None, children: list=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):

        final_string = ""

        for key, value in self.props.items():
            final_string += f'{key}="{value}" '
        return final_string
    

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict=None):
        super().__init__(tag=tag, value=value, props=props)
        if self.value is None:
            raise ValueError("LeafNode must have a value")

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if  self.tag is None:
            return self.value
        elif self.tag == "img":
            return f'<img src="{self.props.get("src", "")}" alt="{self.props.get("alt", "")}"/>'
        elif self.tag == "a":
            return f'<a href="{self.props.get("href", "#")}">{self.value}</a>'
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict=None):
        super().__init__(tag=tag,children=children , props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        return f"<{self.tag}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
        