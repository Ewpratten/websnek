from .Node import Node

class TextNode(Node):
    def __init__(self, metadata: dict,  body):
        self.body = body
        super().__init__(metadata, [])