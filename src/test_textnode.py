import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is an equivalent text node", TextType.BOLD)
        node2 = TextNode("This is an equivalent text node", TextType.BOLD, None)
        node3 = TextNode("This is an non-equivalent text node", TextType.BOLD, "https://youtube.com")
        node4 = TextNode("This is an non-equivalent text node", TextType.ITALIC)
        node5 = TextNode("This is an non-equivalent text node", TextType.BOLD, None)
        node6 = TextNode("This is an equivalent text node", TextType.BOLD, "https://youtube.com")
        node7 = TextNode("This is an equivalent text node", TextType.BOLD, "https://youtube.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node4)
        self.assertNotEqual(node3, node5)
        self.assertEqual(node6, node7)

if __name__ == "__main__":
    unittest.main()
