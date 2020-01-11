from abc import ABC


class EmployeeBinaryTreeNode(object):
    """
    Class that represents a BinaryTree Node. a EmployeeBinaryTreeNode contains a left child, right child &
    value of the current Node. The child nodes of this node in-turn would follow the properties of a EmployeeBinaryTreeNode
    """

    def __init__(self, emp_id, left=None, right=None):
        """
        Constructor of a BinaryTree Node. The 
        :param emp_id: 
        :param left: 
        :param right: 
        """
        self.left = None
        self.right = None
        self.swipe_count = 1
        self.employee_id = emp_id

    def __str__(self):
        """
        Prints the contents of the current node
        :return:
        """
        return str(self.employee_id)


class EmployeeBinaryTree(object):
    """ Class that represents a BinaryTree

    """

    def __init__(self):
        """

        """
        self.__root = None
        self.emp_count = 0

    IN_ORDER_TEMPLATE = "{left} {curr} {right}"
    PRE_ORDER_TEMPLATE = "{curr} {left} {right}"
    POST_ORDER_TEMPLATE = "{left} {right} {curr}"
    EMP_COUNT_STATUS = "{emp_id}, {swipe_count}, {availability}"

    def __print_pre_order_util(self, node):
        """
        Utility function to traverse & print the tree pre-order.
        :param node:
        :return:
        """
        if node is None:
            return ""
        curr = str(node.employee_id)
        left = self.__print_in_order_util(node.left)
        right = self.__print_in_order_util(node.right)
        return curr + " " + left + " " + right

    def __print_post_order_util(self, node):
        """ Utility function to traverse & print the tree post-order.

        :param node:
        :return:
        """
        if node is None:
            return ""
        left = self.__print_in_order_util(node.left)
        right = self.__print_in_order_util(node.right)
        curr = str(node.employee_id)
        return left + " " + right + " " + curr

    def __print_in_order_util(self, node):
        """
        Utility function to traverse & print the tree in-order.
        :param node:
        :return:
        """

        if node is None:
            return ""
        left = self.__print_in_order_util(node.left)
        curr = str(node.employee_id)
        right = self.__print_in_order_util(node.right)

        return left + " " + curr + " " + right

    def __print_tree_util(self, node, template):
        """
        Utility function to print the Tree formation
        :param node:
        :param template:
        :return:
        """
        if node is None:
            return ""
        left = self.__print_in_order_util(node.left)
        curr = str(node.employee_id)
        right = self.__print_in_order_util(node.right)
        return template.format(left=left, curr=curr, right=right)

    def __search_util(self, node, value):
        """ Utility function to Search the Binary Tree Nodes for a value

        :param node:
        :param value:
        :return:
        """
        if node is None:
            return None
        if node.employee_id == value:
            return node
        if value < node.employee_id:
            return self.__search_util(node.left, value)
        if value > node.employee_id:
            return self.__search_util(node.right, value)

    def __add_node_util(self, node, data):
        """ Utility function to Add a Binary Tree Nodes to the tree

        :param node:
        :param data:
        :return:
        """
        if data < node.employee_id:
            if node.left is None:
                node.left = EmployeeBinaryTreeNode(data)
                self.emp_count += 1
            else:
                self.__add_node_util(node.left, data)
        elif data > node.employee_id:
            if node.right is None:
                node.right = EmployeeBinaryTreeNode(data)
                self.emp_count += 1
            else:
                self.__add_node_util(node.right, data)
        else:
            node.swipe_count += 1

    def __print_inorder_range_util(self, node, min_value=None, max_value=None):
        """
        Utility function to traverse & print the tree in-order.
        :param node:
        :return:
        """

        if node is None:
            return ""

        output = ""
        # current = ""
        # right = ""

        if min_value:
            if node.left and int(node.employee_id) > int(min_value):
                output += self.__print_inorder_range_util(node.left, min_value, max_value)
                # print(left)

        if min_value and max_value:
            if int(min_value) <= int(node.employee_id) <= int(max_value):
                output += '%s,%s,%s\n' % (str(node.employee_id), str(node.swipe_count), 'Out' if node.swipe_count % 2 == 0 else 'In')

        if max_value:
            if node.right and int(node.employee_id) < int(max_value):
                output += self.__print_inorder_range_util(node.right, min_value, max_value)

        return output

    def print_inorder_range(self, min_value=None, max_value=None):
        return self.__print_inorder_range_util(self.__root, min_value, max_value)

    def print_in_order_traversal(self):
        """  Prints the In-Order Traversed form of the Tree.
        Prints the left node, then the current node, then the right node. This results in all the data in the tree
        being printed in sorted order.

        :return:
        """
        return self.__print_tree_util(self.__root, self.IN_ORDER_TEMPLATE)

    def print_pre_order_traversal(self):
        """  Prints the Pre-Order Traversed form of the Tree.
        Prints the current node, then the left node,  then the right node.  Print each node before it's sub tree

        :return:
        """
        return "[" + self.__print_pre_order_util(self.__root) + "]"

    def print_post_order_traversal(self):
        """  Prints the Post-Order Traversed form of the Tree.
        Prints the the right node, then the left node & then current node.  Print each node after it's sub tree

        :return:
        """
        return "[" + self.__print_post_order_util(self.__root) + "]"

    def add_node(self, data):
        """

        :param data:
        :return:
        """
        if self.__root is None:
            self.__root = EmployeeBinaryTreeNode(data)
        else:
            self.__add_node_util(self.__root, data)

    def contains(self, value):
        """

        :param value:
        :return:
        """
        return self.__search_util(self.__root, value)

    def __compare_nodes(self, node1, node2):
        """ Utility method to compare the contents of 2 nodes

        :param node1:
        :param node2:
        :return:
        """
        if node1.swipe_count >= node2.swipe_count:
            return node1
        else:
            return node2

    def __max_freq_node(self, root):
        """ Utility  recursive method to find the employee with max swipes

        :param root:
        :return:
        """
        # leaf node - hence max node is same as current node
        if root.left is None and root.right is None:
            return root
        # Non Leaf - with one child - right
        if root.left is None:
            return self.__compare_nodes(root, self.__max_freq_node(root.right))
        # Non Leaf - with one child - left
        elif root.right is None:
            return self.__compare_nodes(root, self.__max_freq_node(root.left))
        else:
            # Non Leaf - with 2 child
            max_child = self.__compare_nodes(
                self.__max_freq_node(root.left),
                self.__max_freq_node(root.right)
            )
            return self.__compare_nodes(root, max_child)

    def find_max_swipe_frequency(self):
        return self.__max_freq_node(self.__root)

    # default to printing the tree using an "in order" traversal.
    def __str__(self):
        """

        :return:
        """
        return self.print_in_order_traversal()
