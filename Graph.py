class AttributeContainer:
    def __init__(self):
        self.attributes = {}

    def __setitem__(self, key, value):
        # Set node attributes using dict-style syntax
        self.attributes[key] = value

    def __getitem__(self, key):
        # Get node attributes using dict-style syntax
        if key in self.attributes:
            return self.attributes[key]
        raise KeyError(f"Attribute '{key}' not found.")

    def format_attributes(self):
        return ''.join([f'{key} = "{value}"' for key, value in self.attributes.items()])

class Node(AttributeContainer):
    def __init__(self, node_id):
        super().__init__()
        self.node_id = node_id

    def output(self):
        # Generate and return the node output string
        attributes_str = f'[{self.format_attributes()}]' if self.attributes else ''
        return f'{self.node_id} {attributes_str};\n'

class Edge(AttributeContainer):
    def __init__(self, prev, curr):
        super().__init__()
        self.prev = prev
        self.curr = curr

    def output(self):
        attributes_str = f'[{self.format_attributes()}]' if self.attributes else ''
        result = f'{self.prev.node_id} -> {self.curr.node_id} {attributes_str};\n'
        return result

class Graph(AttributeContainer):
    def __init__(self, param1, param2):
        super().__init__()
        self.param1 = param1
        self.param2 = param2
        self.nodes = []

    def add_node(self, node: str) -> Node:
        """
        Adds a node to the graph.

        :param node: The node to be added.
        """
        new_node = Node(node)
        if new_node not in self.nodes:
            self.nodes.append(new_node)

        return new_node

    def add_edge(self, prev: Node, curr: Node) -> Edge:
        new_edge = Edge(prev, curr)
        if new_edge not in self.nodes:
            self.nodes.append(new_edge)
            
        return new_edge

    def output(self):
        # Generate and return the output string with all nodes
        items = ""
        if self.attributes:
            for key, value in self.attributes.items():
                items += f'node [{key} = "{value}"];\n'
        
        for node in self.nodes:
            items += "\t" + node.output()

        result = f'{self.param2} "{self.param1}" {{\n{items}}}\n'
        return result

    @property
    def node(self) -> dict:
        return self.attributes

class quotedGraph(Graph):
    def output(self):
        # Generate and return the output string with all nodes
        items = ""
        if self.attributes:
            for key, value in self.attributes.items():
                items += f'node [{key} = "{value}"];\n'
        
        for node in self.nodes:
            if not isinstance(node, Node): 
                items += "\t" + node.output()

        result = f'{self.param2} "{self.param1}" {{\n{items}}}\n'
        return result
    