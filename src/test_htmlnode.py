import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        )
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank" ')

    def test_empty_nodehtml(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        self.assertRaises(NotImplementedError, node.to_html)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_span(self):
        node = LeafNode( "span", "Hello, world!")
        self.assertEqual(node.to_html(), "<span>Hello, world!</span>")

    def test_no_value(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode("p", None)
            node.to_html()
        self.assertEqual(str(context.exception), "LeafNode must have a value")

    def test_img_tag(self):
        node = LeafNode(tag="img", value="", props={"src": "image.png", "alt": "An image"})
        self.assertEqual(node.to_html(), '<img src="image.png" alt="An image"/>')

    def test_link_tag(self):
        node = LeafNode(tag="a", value="Link text", props={"href": "http://example.com"})
        self.assertEqual(node.to_html(), '<a href="http://example.com">Link text</a>')


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_child(self):
        child_node = LeafNode("b","child")
        child_node2 = LeafNode("i", "child2")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><b>child</b><i>child2</i></div>")

    def test_to_html_multiple_child_and_parents(self):
        child_node = LeafNode("b","child")
        child_node2 = LeafNode(None, value="child2")
        child_node3 = LeafNode("b","child3")
        child_node4 = LeafNode("i", "child4")
        parent_node = ParentNode("p", [child_node, child_node2])
        parent_node2 = ParentNode("h1", [child_node3])
        parent_node3 = ParentNode("h2", [child_node4])
        grandparent_node = ParentNode("div", [parent_node, parent_node2, parent_node3])

        solution= "<div><p><b>child</b>child2</p><h1><b>child3</b></h1><h2><i>child4</i></h2></div>"

        self.assertEqual(grandparent_node.to_html(), solution)
        