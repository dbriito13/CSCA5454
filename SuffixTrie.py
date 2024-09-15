from TrieNode import TrieNode
from utils import *


class SuffixTrie:
    def __init__(self, string) -> None:
        self.root = TrieNode(0, string)
        self.curr_id = 1

    def insert_suffix(self, suffix):
        current_node = self.root
        i = 0
        found_match = False
        edge_to_split = None

        while i < len(suffix):
            # Is there any node starting with the first letter in suffix
            for label, destination in current_node.edges.items():
                if label.startswith(suffix[i]):
                    found_match = True
                    common_len, common_prefix = get_common_prefix(label, suffix)
                    if common_len == len(label):
                        # If common prefix is the whole label, move down the tree
                        current_node = destination
                        # Move position of prefix to after the common prefix
                        i += common_len
                        break
                    else:
                        edge_to_split = label
                        # Split edge

            if found_match and edge_to_split:
                remaining_label, remaining_suffix = (
                    edge_to_split[common_len:],
                    suffix[i + common_len :],
                )

                # New node for the common prefix
                common_Node = TrieNode(destination.id, common_prefix)
                common_Node.add_edge(remaining_label, current_node.edges[edge_to_split])

                current_node.add_edge(common_prefix, common_Node)

                # Get edge to delete
                del current_node.edges[edge_to_split]

                if remaining_suffix:
                    common_Node.add_edge(
                        remaining_suffix,
                        TrieNode(self.curr_id, remaining_suffix),
                    )
                else:
                    common_Node.is_end = True

                return

            if not found_match:
                # If no node started had a common prefix with the suffix, insert it
                current_node.edges[suffix[i:]] = TrieNode(self.curr_id, suffix)
                self.curr_id += 1
                return

    def search(self, substring):
        current_node = self.root
        i = 0

        while i < len(substring):
            first_char = substring[i]
            edge_found = False

            for label, edge in current_node.edges.items():
                if label.startswith(first_char):
                    _, common_prefix = get_common_prefix(label, substring[i:])
                    common_len = len(common_prefix)

                    if common_len > 0:
                        if common_len == len(substring[i:]):
                            return True
                        elif common_len < len(label):
                            return False
                        else:
                            current_node = edge
                            i += common_len
                            edge_found = True
                            break

            if not edge_found:
                return False

        return True

    def create_trie_naive(self, string):
        for i in range(len(string)):
            self.insert_suffix(string[i:])


# Example usage
trie = SuffixTrie("banana")
text = "banana"
trie.create_trie_naive(text)

# Search for substrings
print(trie.search("ana"))  # True
print(trie.search("nana"))  # True
print(trie.search("ban"))  # True
print(trie.search("apple"))  # False
