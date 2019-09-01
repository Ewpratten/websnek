from ..html.nodes.ElementNode import Node

class StyledNode(object):
    node: Node
    style_values: list
    children: list = []