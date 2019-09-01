
class Node(object):
    def __init__(self, metadata: dict,  children=[]):
        self.children = children
        self.metadata = metadata


def buildTextNode(data: str):
    return Node({"type": "text", "body": data})


def buildElementNode(name: str, attrs: dict, children=[]):
    return Node({"type": "element", "name": name, "attrs": attrs}, children=children)
