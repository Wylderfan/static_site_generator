from parentnode import ParentNode
from leafnode import LeafNode

def test_parentnode(node):
    print(node.to_html())

if __name__ == "__main__":
    node = ParentNode(
        tag="p",
        children=[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ])
    node2 = ParentNode(
        tag="p",
        children=[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            node,
            LeafNode(None, "Normal text"),
        ])
    node3 = ParentNode(tag=None, children=None)
    node4 = ParentNode(tag="p", children=None)
    print("Testing ParentNode")
    test_parentnode(node)
    print("Testing ParentNode inside a ParentNode")
    test_parentnode(node2)
    print("Testing Error Detection")
    try:
        test_parentnode(node3) # will catch exception
    except ValueError as e:
        print(e)
    try:
        test_parentnode(node4) # will catch exception
    except ValueError as e:
        print(e)



    
