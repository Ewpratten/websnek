class Node(object):
    def __init__(self, name: str, attributes={}, children=[]):
        self.name = name
        self.attributes = attributes
        self.children = children

    def addChild(self, child):
        self.children.append({"type": "element", "body": child})

    def addData(self, data):
        self.children.append({"type": "data", "body": data})

    def getID(self):
        return self.attributes.get("id", "")
    
    def getClasses(self):
        return self.attributes.get("class", "").split(" ")