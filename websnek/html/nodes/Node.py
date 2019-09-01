class Node(object):
    def __init__(self, metadata: dict,  children=[]):
        self.children = children
        self.metadata = metadata