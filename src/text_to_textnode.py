from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnode(text: str) -> list:
    """
    Converts a plain text string into a list of TextNode objects,
    identifying different text styles such as bold, italic, code, links, and images.
    """
    nodes = [TextNode(text, TextType.TEXT)]
    # nodes is a single TextNode of type TEXT initially
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    # nodes is now split into TEXT and BOLD TextNodes
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    # nodes is now split into TEXT, BOLD, and ITALIC TextNodes
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    # nodes is now split into TEXT, BOLD, ITALIC, and CODE TextNodes
    nodes = split_nodes_image(nodes)
    # nodes is now split into TEXT, BOLD, ITALIC, CODE, and IMAGE TextNodes
    nodes = split_nodes_link(nodes)
    # nodes is now split into TEXT, BOLD, ITALIC, CODE, IMAGE, and LINK TextNodes

    # Finally, what was a single string representing a markdown block is transformed
    # into a list of TextNode objects representing the different inline text styles.
    return nodes