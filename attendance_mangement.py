# -*- coding: utf-8 -*-
import logging
import os

from binary_tree import EmployeeBinaryTree

LOG = logging.getLogger(__name__)


class EmployeeAttendanceProblem(object):
    """
    A Class representing an Employee Structure as a BinaryTree ADT
    """

    def __init__(self, input_file_name, output_file_name):
        """

        :param input_file_name:
        :param output_file_name:
        """
        self.__emp_tree = EmployeeBinaryTree()
        self.__input_file_name = input_file_name
        self.__output_file_name = output_file_name
        self.__populate_inputs(input_file_name)

    @staticmethod
    def _read_input_file(file_name):
        """ Utility method to read from a file

        :param file_name:
        :return:
        """
        if file_name:
            file_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'), file_name)
            with open(file_path, 'r') as f:
                # return [str(line.strip()) for line in f.readlines()]
                return f.readlines()
        return None

    @staticmethod
    def _write_output_file(file_name, contents, rewrite=False):
        """

        :param file_name:
        :return:
        """
        if file_name:
            file_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'), file_name)
            with open(file_path, 'w' if rewrite else 'a') as f:
                return f.writelines(contents)
        return None

    def __populate_inputs(self, input_file):
        """

        :param input_file_name:
        :return:
        """
        input_file_contents = EmployeeAttendanceProblem._read_input_file(input_file)
        for emp_id in input_file_contents:
            self.__readEmployeesRec(self.__emp_tree, emp_id.strip('\n'))

    def __readEmployeesRec(self, emp_tree, emp_id):
        """
        This function reads from the inputPS1.txt file the ids of employees entering and leaving the organization premises.
        One employee id should be populated per line (in the input text file) indicating their swipe (entry or exit).
        The input data is used to populate the tree. If the employee id is already added to the tree,
        then the attendance counter is incremented for every subsequent occurrence of that employee id in the input file.
        :param emp_tree:
        :param emp_id:
        :return:
        """
        if emp_tree and emp_id:
            emp_tree.add_node(emp_id)
            print(emp_tree)

    def __getHeadcountRec(self, tree_node):
        """

        :param tree_node:
        :return:
        """
        return tree_node.emp_count

    def __searchIDRec(self, emp_tree, emp_id):
        """

        :param emp_tree:
        :param emp_id:
        :return:
        """
        employee_node = emp_tree.contains(emp_id)
        if employee_node:
            return employee_node.swipe_count
        return 0

    def __howOften_Rec(self, emp_tree, emp_id):
        employee_node = emp_tree.contains(emp_id)
        if employee_node:
            return employee_node.swipe_count
        return 0

    def __frequentVisitorRec(self, emp_tree):
        pass

    def __printRangePresent(self, start_emp_id, end_emp_id):
        return '', '', ''

    def parseCommands(self, file_name='promptsPS1.txt'):
        """

        :param file_name:
        :return:
        """
        output_file_contents = []
        try:
            prompt_file_contents = EmployeeAttendanceProblem._read_input_file(file_name)
            query_list = [(line.rstrip('\n').split(':')) for line in prompt_file_contents]

            print("Total number of employees today: %s" % self.__getHeadcountRec(self.__emp_tree))

            start_id, end_id = None, None

            for command in query_list:
                operator = command[0].lower()
                operand = command[1:]

                if 'searchid' == operator:
                    emp_id = operand[0]
                    val = self.__searchIDRec(self.__emp_tree, emp_id)
                    if val > 0:
                        print('Employee id %s is present today.' % emp_id)
                    else:
                        print('Employee id %s is absent today.' % emp_id)
                elif 'howoften' == operator:
                    emp_id = operand[0]
                    val = self.__howOften_Rec(self.__emp_tree, emp_id)
                    if val in [0, None]:
                        print('Employee id %s did not swipe today' % emp_id)
                    else:
                        if val % 2 != 0:
                            print('Employee id %s swiped %s times today and is currently in office' % (emp_id, val))
                        else:
                            print('Employee id %s swiped %s times today and is currently not in office' % (emp_id, val))
                elif 'range' == operator:
                    start_id, end_id = operand
                    print('Range: %s to %s' % (start_id, end_id))
                    emp_id, count, presence = self.__printRangePresent(start_id, end_id)
                    print('%s, %s, %s' % (emp_id, count, presence))

            self.__frequentVisitorRec(self.__emp_tree)

        except ValueError as ve:
            LOG.error("Error in value given in the prompt file: {0}".format(ve))
        except IOError as ie:
            LOG.error("Error in prompt file: {0} - {1}".format(file_name, str(ie)))


if __name__ == '__main__':
    # EmployeeAttendanceProblem._write_output_file('output.txt', EmployeeAttendanceProblem._read_input_file('inputPS1.txt'), rewrite=True)
    org_emp_attendance = EmployeeAttendanceProblem('inputPS1.txt', 'output.txt')
    org_emp_attendance.parseCommands()
