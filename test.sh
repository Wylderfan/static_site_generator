python3 -m unittest discover -s src
echo "Print html node tests:"
python3 src/test_htmlnode.py
echo "\n"
echo "Print leaf node tests:"
python3 src/test_leafnode.py
echo "Print parent node tests:"
python3 src/test_parentnode.py
echo "Print text to html node tests:"
python3 src/test_textnode_to_htmlnode.py



