from htmlnode import HTMLNode

class TestHTMLNode():
    def test_print(self):
        node1 = HTMLNode(tag="h1", value="Hello, World!", props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(tag="h1", value="Hello, World!")
        print(f"node1: {node1}\nnode2: {node2}")

if __name__ == "__main__":
    test = TestHTMLNode()
    test.test_print()
