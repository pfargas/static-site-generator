from markdown_to_block import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from text_to_textnode import text_to_textnode
from text_to_html import text_node_to_html_node
from htmlnode import ParentNode, LeafNode
from textnode import TextType

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown) # Split markdown into blocks
    parent_node = ParentNode(tag="div", children=[]) # Root HTML node
    for block in blocks:
        type = block_to_block_type(block) # Determine block type
        if type == BlockType.CODE:
            # if it's a code block, don't parse inner text
            temporal_leaf_node = ParentNode(tag="pre", children=[LeafNode(tag="code", value=block[3:-3])])
            #---------------------------
        if type == BlockType.PARAGRAPH:
            leaf_nodes = text_to_children(block) # Convert block text to HTML nodes
            # If it's a paragraph, create a <p> tag and add text nodes as children
            temporal_leaf_node = ParentNode(tag="p", children=leaf_nodes)
            #---------------------------
        elif type == BlockType.HEADING:
            heading_level = block.count("#", 0, block.find(" "))
            leaf_nodes = text_to_children(block[heading_level+1:]) # Convert heading text to HTML nodes
            temporal_leaf_node = ParentNode(tag=f"h{heading_level}", children=leaf_nodes)
            #---------------------------
        elif type == BlockType.QUOTE:
            leaf_nodes = text_to_children(block[1:].lstrip()) # Convert quote text to HTML nodes
            temporal_leaf_node = ParentNode(tag="blockquote", children=leaf_nodes)
            #---------------------------
        elif type == BlockType.UNORDERED_LIST:
            temporal_leaf_node = process_unordered_list_block(block)
            #---------------------------
        elif type == BlockType.ORDERED_LIST:
            temporal_leaf_node = process_ordered_list_block(block)
            #---------------------------
        parent_node.children.append(temporal_leaf_node)
    return parent_node


def text_to_children(text: str) -> list:
    text_nodes = text_to_textnode(text)
    for tn in text_nodes:
        if tn.text_type == TextType.IMAGE:
            print("Found image:", tn)
            html_node = text_node_to_html_node(tn)
            print("Converted to HTML node:", html_node.to_html())


    html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
    return html_nodes

def process_unordered_list_block(block: str) -> ParentNode:
    lines = block.splitlines()
    list_items = []
    for line in lines:
        stripped_line = line.lstrip("- ").strip()
        item_nodes = text_to_children(stripped_line)
        list_item_node = ParentNode(tag="li", children=item_nodes)
        list_items.append(list_item_node)
    return ParentNode(tag="ul", children=list_items)

def process_ordered_list_block(block: str) -> ParentNode:
    lines = block.splitlines()
    list_items = []
    for line in lines:
        stripped_line = line.lstrip("0123456789. ").strip()
        item_nodes = text_to_children(stripped_line)
        list_item_node = ParentNode(tag="li", children=item_nodes)
        list_items.append(list_item_node)
    return ParentNode(tag="ol", children=list_items)

if __name__ == "__main__":
    sample_markdown = """- unordered1 **bold text**
        - *italic text* unordered2
        - `code text` unordered3
    """
    children = text_to_children(sample_markdown)
    parent_node = ParentNode(tag="ul", children=children)
    print(parent_node.to_html())

    markdown = """# Heading 1

    ## Heading 2

    ```
    this code must not be parsed **bold**
    ```

    This is a paragraph with **bold text**, *italic text*, and a [link](http://example.com).

    > This is a blockquote with an ![image](http://example.com/image.png).

    - Unordered list item 1 with `inline code`
    - Unordered list item 2

    1. Ordered list item 1
    2. Ordered list item 2
    """
    html_node = markdown_to_html_node(markdown)
    print(html_node.to_html())

