from lxml import html
from .nodes.ElementNode import Node

def _toElementTree(em):
    """Converts lxml element to html.nodes.ElementNode.Node"""
    em_children = [{"type": "data", "body": em.text}]

    # Recursively parse through elements
    for element in em.getchildren():
        em_children.append(
            {"type": "element", "body": _toElementTree(element)})

    # Fetch metadata
    attributes = em.attrib
    name = em.tag

    # Return a node
    return Node(
        name,
        attributes=attributes,
        children=em_children
    )


def buildTree(file: str):
    doc = html.document_fromstring(file)

    return _toElementTree(doc)
