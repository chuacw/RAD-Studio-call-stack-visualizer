class Edge:
    def __init__(self, prev, curr) -> None:
        self.prev = prev
        self.curr = curr
        self.attributes = {}  # Dictionary to hold node attributes

    def __setitem__(self, key, value):
        # Set node attributes using dict-style syntax
        self.attributes[key] = value

    def __getitem__(self, key):
        # Get node attributes using dict-style syntax
        if key in self.attributes:
            return self.attributes[key]
        raise KeyError(f"Attribute '{key}' not found.")

    def output(self):
        # Format the node attributes
        attributes_str = ""
        if self.attributes:
          attributes_str = ''.join([f'{key} = "{value}"' for key, value in self.attributes.items()])
          attributes_str = f'[{attributes_str}]'
        # attributes_str = f'[{attributes_str}]' if attributes_str else ''
        # Generate and return the node output string
        result = f'{self.prev.node_id} -> {self.curr.node_id} {attributes_str};\n'
        return result
        
class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.attributes = {}  # Dictionary to hold node attributes

    def __setitem__(self, key, value):
        # Set node attributes using dict-style syntax
        self.attributes[key] = value

    def __getitem__(self, key):
        # Get node attributes using dict-style syntax
        if key in self.attributes:
            return self.attributes[key]
        raise KeyError(f"Attribute '{key}' not found.")

    def output(self):
        # Format the node attributes
        attributes_str = ''.join([f'{key} = "{value}"' for key, value in self.attributes.items()])
        attributes_str = f'[{attributes_str}]' if attributes_str else ''
        # Generate and return the node output string
        result = f'{self.node_id} {attributes_str};\n'
        return result
    
class Graph:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        self.attributes = {}  # Dictionary to hold attributes
        self.nodes = []

    def __setitem__(self, key, value):
        # Set attributes using dict-style syntax
        self.attributes[key] = value

    def add_node(self, node: str) -> Node:
        """
        Adds a node to the graph.

        :param node: The node to be added.
        """
        new_node = Node(node)
        if new_node not in self.nodes:
            self.nodes.append(new_node)
        return new_node

    def add_edge(self, prev: Node, curr: Node):
        new_edge = Edge(prev, curr)
        if new_edge not in self.nodes:
            self.nodes.append(new_edge)
        return new_edge

    def output(self):
        # Format the attributes
        attributes_str = '; '.join([f'{key} = "{value}"' for key, value in self.attributes.items()])
        attributes_str = f'node [{attributes_str}]' if attributes_str else ''
        # Generate and return the output string with all nodes
        result = ""
        items = ""
        node = ""
        if self.attributes:
            for key, value in self.attributes.items():
                node += f'node [{key} = "{value}"];\n'
            items += node
        if self.nodes:
            for node in self.nodes:
                items += "\t" + node.output()
        result += f'{self.param2} "{self.param1}"'
        result += " {\n"
        result += f'{items}'
        result += "}\n"
        return result
    
    @property
    def node(self) -> dict:
        """
        Provides access to node attributes.

        :return: A dictionary representing node attributes.
        """
        return self.attributes    