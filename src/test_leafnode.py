from leafnode import LeafNode

def test_html(leafnode):
    return leafnode.to_html()
if __name__ == "__main__":
    node1 = LeafNode(tag="p", value="This is a paragraph of text!")
    node2 = LeafNode(tag="h", value="This is a Header!")
    node3 = LeafNode(tag="a", value="This is a link!", props={"href": "https://www.google.com"})
    node4 = LeafNode(tag="b", value="THIS IS BOLD TEXT")
    print(f"Test 1: {test_html(node1)}")
    print(f"Test 2: {test_html(node2)}")
    print(f"Test 3: {test_html(node3)}")
    print(f"Test 4: {test_html(node4)}")
