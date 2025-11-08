from htmlnode import LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node:TextNode):
    """
    Converts a TextNode to an HTML LeafNode.
    """

    match text_node.text_type:
        case TextType.TEXT:
            tag = None
            props = None
            value = text_node.text
        case TextType.BOLD:
            tag = "b"
            props = None
            value = text_node.text
        case TextType.ITALIC:
            tag = "i"
            props = None
            value = text_node.text
        case TextType.LINK:
            tag = "a"
            value = text_node.text
            props = {"href": text_node.url}
        case TextType.CODE:
            tag = "code"
            props = None
            value = text_node.text
        case TextType.IMAGE:
            tag = "img"
            value = ""
            props = {"src": text_node.url, "alt": text_node.text}
        case _:
            raise ValueError("The text type does not correspond to any implemented")
    return LeafNode(tag= tag,value= value, props=props)