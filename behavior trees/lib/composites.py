from .status import *
from .node import Node

__all__ = ['Composite','Secuence','Selector']

class Composite(Node):
    type = 'Composite'
    children = None
    current_id = None
    chld = None

    def __init__(self, tree, idx, children):
        # these are NOT containers, they just point to their children
        self.children = []  # to prevent overriding
        super().__init__(tree, idx)
        for child in children:
            self.children.append(child)
        self.current_id = 0
    
    def update(self):
        child = self.children[self.current_id]
        child.update()


class Secuence(Composite):
    name = 'Secuence'

    def __repr__(self):
        lista = [str(c.idx) for c in self.children]
        return str(self.idx) + ' ' + self.type + ' ' + self.name + ' (' + ','.join(lista) + ')'
    
    def get_child_status(self, status):
        if status is Running:
            self.tree.set_to_check(self.children[self.current_id])

        elif status is Success:
            self.current_id += 1
            if self.current_id == len(self.children)-1:
                status = Success
            else:
                status = Running
        
        if self.parent is not None:
            self.parent.get_child_status(status)

        elif status is Success:
            self.tree.reset_to_check()


class Selector(Composite):
    name = 'Selector'

    def __repr__(self):
        return str(self.idx) + ' ' + self.type + ' ' + self.name + ' (' + ','.join([str(c) for c in self.children]) + ')'

    def get_child_status(self, status):
        if status is Running:
            self.tree.set_to_check(self.children[self.current_id])

        elif status is Failure:
            self.current_id += 1
            if self.current_id == len(self.children)-1:
                status = Failure
            else:
                status = Running

        if self.parent is not None:
            self.parent.get_child_status(status)

        elif status is Success:
            self.tree.reset_to_check()
