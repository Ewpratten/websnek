import tinycss
from .rule import Rule


def parseCSS(file: str):
    """Converts tinycss pearser output to custom classes"""

    # Parse string into tinycss
    parser = tinycss.make_parser('page3')
    css_rules = parser.parse_stylesheet_bytes(file.encode()).rules

    # Parse tinycss into rules
    ruleset = []
    for rule in css_rules:
        selectors = []
        declarations = []

        next_sel_class = False
        for sel in rule.selector:

            # Check if the selector is an identity
            if sel.type == "IDENT" or sel.type == "HASH":

                # Determine selector type
                if next_sel_class:
                    sel_type = "class"
                elif sel.value[0] == "#":
                    sel_type = "id"
                    # Chop the name if a,id
                    sel.value = sel.value[1:]
                else:
                    sel_type = "tag"

                selectors.append({
                    "type": sel_type,
                    "name": sel.value
                })

            # If the current item is a ".", the next is a class
            elif sel.value == ".":
                next_sel_class = True

        for dec in rule.declarations:
            declarations.append((dec.name, dec.value.as_css()))

        ruleset.append({
            "selectors": selectors,
            "declarations": declarations
        })

    return ruleset
