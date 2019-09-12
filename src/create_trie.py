
# Create a trie from the dictionary file, where each node contains a character from the word
# Plus a flag to indicate whether or not the current node is the end of a valid word


class Node:
    def __init__(self, root_value):
        self.value = root_value
        self.children = []
        self.valid_end_of_word = False


def insert(root, word):
    node = root
    for char in word:
        # Check if node's children contains this character
        char_in_children = False
        for child in node.children:

            if child.value == char:
                char_in_children = True
                node = child  # Want to keep traversing down this child
                break

        # If the char wasn't in the node's children, want to add it
        if not char_in_children:
            new_child = Node(char)
            node.children.append(new_child)
            node = new_child

    # The loop has ended and the end of the word has been reached
    node.valid_end_of_word = True








