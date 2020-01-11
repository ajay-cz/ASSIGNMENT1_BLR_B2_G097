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
    __root = None
    emp_count = 0

    def __init__(self):
        """

        """
        pass



    IN_ORDER_TEMPLATE = "{left} {curr} {right}"
    PRE_ORDER_TEMPLATE = "{curr} {left} {right}"
    POST_ORDER_TEMPLATE = "{left} {right} {curr}"

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
        Utility function to print the free formation
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
        """

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
        """not

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
        """

        :param node:
        :return:
        """
        if node is None:
            return ""
        left = self.__print_in_order_util(node.left)
        right = self.__print_in_order_util(node.right)
        curr = str(node.employee_id)
        return left + " " + right + " " + curr

    # print the left node, then the current node, then the right node.
    # this results in all the data in the tree being printed in sorted order.
    def print_in_order_traversal(self):
        # return "[" + self.__print_in_order_util(self.__root) + "]"
        return "[" + self.__print_tree_util(self.__root, self.IN_ORDER_TEMPLATE) + "]"

    def print_pre_order_traversal(self):
        """
         Print each node before it's sub tree
        :return:
        """
        return "[" + self.__print_pre_order_util(self.__root) + "]"

    # print each node after it's sub tree
    def print_post_order_traversal(self):
        """

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

    # default to printing the tree using an "in order" traversal.
    def __str__(self):
        """

        :return:
        """
        return self.print_in_order_traversal()
