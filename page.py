# Node data structure for holding necesary information

class Page():
    """
    A Node data structure meant to hold the link of the Wikipedia page,
    as well as all of the links found on that Wikipedia page.
    """

    def __init__(self, name):
        self.name = name
        self.children = []
