class Tree:
    """ Container class for Tree data structure """
    def __init__(self, data) -> None:
        self.data = data
        self.left_node = None
        self.right_node  = None 

    def get_node(self) -> object:
        return self.data

    def set_node( self, data ) -> object:
        self.data = data

    def __repr__(self) -> str:
        return f"{self.left_node}->{self.data}->{self.right_node}"



if __name__ == '__main__':
    t = Tree(24)
    t.left_node = Tree(35)
    t.right_right = Tree(45)
    print(t)