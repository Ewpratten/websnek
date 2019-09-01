from ..html.nodes.ElementNode import Node
from .StyledNode import StyledNode

def matchesSelector(elem: Node, selector: dict):

    # Check tag
    if selector["type"] == "tag":
        return selector["name"] == elem.name

    # Check id
    if selector["type"] == "id":
        return selector["name"] == elem.getID()

    # Check classes
    if selector["type"] == "class":
        return selector["name"] in elem.getClasses()

    # Nothing matched
    return False

def getRulesForNode(elem: Node, stylesheet: dict):
    rules = []

    # Iterate through all defined rules
    for rule in stylesheet:

        # Iterate each selector for the rule
        for selector in rule["selectors"]:
            if type(elem) != dict and matchesSelector(elem, selector):

                # Add this rule's declatations to the ruleset
                rules += rule["declarations"]
    
    return rules

def buildStyleTree(root: Node, stylesheet: dict):
    output = StyledNode()

    # Set node and style data
    output.node = root
    output.style_values = getRulesForNode(root, stylesheet)

    # For each of root's children, add it to the style tree
    for child in root.children:
        if type(child) != dict:
            output.children.append(buildStyleTree(child, stylesheet))
    
    return output