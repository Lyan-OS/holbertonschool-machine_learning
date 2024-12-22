#!/usr/bin/env python3
import numpy as np


class Node:
    def __init__(self, feature=None, threshold=None,
                 left_child=None, right_child=None,
                 is_root=False, depth=0):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        if self.is_leaf:
            return self.depth
        if self.left_child:
            left_depth = self.left_child.max_depth_below()
        else:
            self.depth
        if self.right_child:
            right_depth = self.right_child.max_depth_below()
        else:
            self.depth
        return max(left_depth, right_depth)

    def count_nodes_below(self, only_leaves=False):
        if self.is_leaf:
            return 1
        if self.left_child:
            left_count = self.left_child.count_nodes_below(
                only_leaves=only_leaves)
        else:
            0
        if self.right_child:
            right_count = self.right_child.count_nodes_below(
                only_leaves=only_leaves)
        else:
            0
        if only_leaves:
            return left_count + right_count
        return 1 + left_count + right_count

    def __str__(self):
        """generate a string representation of the tree"""
        node_str = f"{
            'root' if self.is_root else 'node'} [feature={
                self.feature}, threshold={self.threshold}]"
        if self.left_child:
            left_str = left_child_add_prefix(str(self.left_child))
        else:
            left_str = ""
        if self.right_child:
            right_str = right_child_add_prefix(str(self.right_child))
        else:
            right_str = ""
        return f"{node_str}\n{left_str}{right_str}"

    def get_leaves_below(self):
        """Recursively collects all leaves below this node."""
        leaves = []
        if self.left_child:
            leaves.extend(self.left_child.get_leaves_below())
        if self.right_child:
            leaves.extend(self.right_child.get_leaves_below())
        return leaves

    def update_bounds_below(self):
        """Recursively computes and propagates bounds for each node."""
        if self.is_root:
            self.upper = {0: np.inf}
            self.lower = {0: -np.inf}

        for child in [self.left_child, self.right_child]:
            if child:
                child.lower = self.lower.copy()
                child.upper = self.upper.copy()

                if child == self.left_child:
                    child.upper[self.feature] = self.threshold
                elif child == self.right_child:
                    child.lower[self.feature] = self.threshold

        # Recurse on children
        for child in [self.left_child, self.right_child]:
            if child:
                child.update_bounds_below()


def left_child_add_prefix(text):
    """Add prefix for the left child."""
    lines = text.split("\n")
    new_text = "    +--" + lines[0] + "\n"
    for x in lines[1:]:
        new_text += "    |  " + x + "\n"
    return new_text


def right_child_add_prefix(text):
    """Add prefix for the right child."""
    lines = text.split("\n")
    new_text = "    +--" + lines[0] + "\n"
    for x in lines[1:]:
        new_text += "       " + x + "\n"
    return new_text


class Leaf(Node):
    def __init__(self, value, depth=None):
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        return 1

    def __str__(self):
        return f"-> leaf [value={self.value}]"

    def get_leaves_below(self):
        return [self]

    def update_bounds_below(self):
        pass


class Decision_Tree():
    def __init__(self, max_depth=10, min_pop=1, seed=0,
                 split_criterion="random", root=None):
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def __str__(self):
        return self.root.__str__()

    def get_leaves(self):
        return self.root.get_leaves_below()

    def update_bounds(self):
        self.root.update_bounds_below()
