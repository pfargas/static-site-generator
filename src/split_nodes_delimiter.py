from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list:
    """
    Splits TextNode objects in old_nodes by the specified delimiter,
    creating new TextNode objects with the specified text_type for the
    text segments found between the delimiters."""
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter in text: {node.text}")

        for i, part in enumerate(parts):
            if part == '':
                continue
            if i%2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes
            

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    pattern = r"(?<!\!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def split_nodes_image(old_nodes: list[TextNode]) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        patterns = extract_markdown_images(node.text)
        text = node.text
        for alt_text, url in patterns:
            img_markdown = f"![{alt_text}]({url})"
            split_parts = text.split(img_markdown, 1)
            new_nodes.append(TextNode(split_parts[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url=url))
            text = split_parts[1]
        new_nodes.append(TextNode(text, TextType.TEXT))
    return [n for n in new_nodes if n.text != '']

def split_nodes_link(old_nodes: list[TextNode]) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        patterns = extract_markdown_links(node.text)
        text = node.text
        for link_text, url in patterns:
            link_markdown = f"[{link_text}]({url})"
            split_parts = text.split(link_markdown, 1)
            new_nodes.append(TextNode(split_parts[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, url=url))
            text = split_parts[1]
        new_nodes.append(TextNode(text, TextType.TEXT))
    return [n for n in new_nodes if n.text != '']

       
