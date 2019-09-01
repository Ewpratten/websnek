# from .Node import Node

# class ElementNode(Node):
#     def __init__(self, metadata: dict, attributes=[], children=[]):
#         self.attributes = attributes
#         super().__init__(metadata, children)


class Node(object):
    def __init__(self, name: str, attributes=[], children=[]):
        self.name = name
        self.attributes = attributes
        self.children = children

    def addChild(self, child):
        self.children.append({"type": "element", "body": child})

    def addData(self, data):
        self.children.append({"type": "data", "body": data})

    # def getElement
