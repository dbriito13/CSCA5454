class TrieNode:
    def __init__(self, id, string, suffix_link=None, parent=None) -> None:
        self.string = string
        self.id = id
        self.suffix_link = suffix_link
        self.parent = parent
        self.edges = {}
        self.is_end = False

    def add_suffix_link(self, suffix_link):
        self.suffix_link = suffix_link

    def add_edge(self, label, destination):
        self.edges[label] = destination

    def __str__(self) -> str:
        return f"TrieNode[id: {self.id} | suffix_link: {self.suffix_link} | parent: {self.parent} ]"
