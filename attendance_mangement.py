# -*- coding: utf-8 -*-
import logging
import os

from binary_tree import EmployeeBinaryTree

LOG = logging.getLogger(__name__)


class EmployeeAttendanceMonitoringSystem(object):
    """
    A Class to represent an attendance monitoring system. The unique integer ID number of every employee is noted 
    whenever the employee swipes his card in the office. First time an employee enters into the office, 
    the attendance counter is set to 1. From then onwards, each time an employee leaves the office premises for 
    tea break or lunch break the counter is incremented, and incremented again when he enters back. 
    If the counter is odd on a day, it means the employee is in the office premises and if the counter is even, 
    it means he is out of the premises.
    
    The Employee - Attendance relation is maintained in a Binary Tree structure
    """

    def __init__(self, input_file_name):
        """ Constructor for the Employee

        """
        self.__emp_tree = EmployeeBinaryTree()
        self.__output_file_contents = []
        self.__populate_inputs(input_file_name)

    @staticmethod
    def _read_input_file(file_name):
        """ Utility method to read from a file

        """
        if file_name:
            file_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data_files'), file_name)
            with open(file_path, 'r') as f:
                # return [str(line.strip()) for line in f.readlines()]
                return f.readlines()
        return None

    @staticmethod
    def _write_output_file(file_name, contents, rewrite=False):
        """ Utility method to write to a file

        """
        if file_name:
            file_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data_files'), file_name)
            with open(file_path, 'w' if rewrite else 'a') as f:
                return f.writelines("%s\n" % l for l in contents)
        return None

    def __populate_inputs(self, input_file):
        """ Utility method to read the inputs from the input file and creates an Employee Node & populates the Tree

        """
        input_file_contents = EmployeeAttendanceMonitoringSystem._read_input_file(input_file)
        for emp_id in input_file_contents:
            self.__readEmployeesRec(self.__emp_tree, emp_id.strip('\n'))
        # print(self.__emp_tree)

    def __readEmployeesRec(self, emp_tree, emp_id):
        """
        This function reads from the inputPS1.txt file the ids of employees entering and leaving the organization premises.
        One employee id should be populated per line (in the input text file) indicating their swipe (entry or exit).
        The input data is used to populate the tree. If the employee id is already added to the tree,
        then the attendance counter is incremented for every subsequent occurrence of that employee id in the input file.

        """
        if emp_tree and emp_id:
            if emp_id.isdigit():
                emp_tree.add_node(int(emp_id))
            # print(emp_tree)

    def __getHeadcountRec(self, tree_node):
        """ This function counts the number of unique IDs stored in the tree and prints the employee headcount for the day

        """
        return tree_node.emp_count

    def __searchIDRec(self, emp_tree, emp_id):
        """ This function searches whether a particular employee has attended today or not.

        """
        employee_node = emp_tree.contains(emp_id)
        if employee_node:
            return employee_node.swipe_count
        return 0

    def __howOften_Rec(self, emp_tree, emp_id):
        """ This function counts the number of times a particular employee swiped today and if the employee is currently
         in the office or outside

        """
        employee_node = emp_tree.contains(emp_id)
        if employee_node:
            return employee_node.swipe_count
        return 0

    def __frequentVisitorRec(self, emp_tree):
        """ This function searches for the employee who has swiped the most number of times

        """
        freq_node = emp_tree.find_max_swipe_frequency()
        if freq_node:
            return freq_node.employee_id, freq_node.swipe_count
        return None, None

    def __printRangePresent(self, start_emp_id, end_emp_id):
        """ This function prints the employee ids in the range StartId to EndId and how often they have entered the organization

        """
        return self.__emp_tree.print_inorder_range(min_value=start_emp_id, max_value=end_emp_id)

    def parseCommands(self, file_name='promptsPS1.txt'):
        """ This function reads from the PRovided prompts file and executes the corresponding commands

        """
        try:
            prompt_file_contents = EmployeeAttendanceMonitoringSystem._read_input_file(file_name)
            query_list = [(line.rstrip('\n').split(':')) for line in prompt_file_contents]
            # print("Total number of employees today: %s" % self.__getHeadcountRec(self.__emp_tree))
            self.__output_file_contents.append("Total number of employees today: %s" % self.__getHeadcountRec(self.__emp_tree))

            start_id, end_id = None, None

            for command in query_list:
                operator = command[0].lower()
                operand = command[1:]

                if 'searchid' == operator:
                    emp_id = operand[0].strip()
                    val = self.__searchIDRec(self.__emp_tree, emp_id)
                    if val > 0:
                        # print('Employee id "%s" is present today.' % emp_id)
                        self.__output_file_contents.append('Employee id "%s" is present today.' % emp_id)
                    else:
                        # print('Employee id "%s" is absent today.' % emp_id)
                        self.__output_file_contents.append('Employee id "%s" is absent today.' % emp_id)

                elif 'howoften' == operator:
                    emp_id = operand[0].strip()
                    val = self.__howOften_Rec(self.__emp_tree, emp_id)
                    if val in [0, None]:
                        # print('Employee id "%s" did not swipe today' % emp_id)
                        self.__output_file_contents.append('Employee id "%s" did not swipe today' % emp_id)
                    else:
                        if val % 2 != 0:
                            # print('Employee id "%s" swiped "%s" times today and is currently in office' % (emp_id, val))
                            self.__output_file_contents.append(
                                'Employee id "%s" swiped "%s" times today and is currently in office' % (emp_id, val))
                        else:
                            # print('Employee id %s swiped %s times today and is currently not in office' % (emp_id, val))
                            self.__output_file_contents.append(
                                'Employee id "%s" swiped "%s" times today and is currently not in office' % (
                                    emp_id, val))

                elif 'range' == operator:
                    start_id, end_id = operand

            if self.__emp_tree.emp_count > 0:
                # print('Employee id "%s" swiped the most number of times today with a count of "%s"' % self.__frequentVisitorRec(self.__emp_tree))
                self.__output_file_contents.append('Employee id "%s" swiped the most number of times today with a count of "%s"' % self.__frequentVisitorRec(self.__emp_tree))

            if start_id and end_id:
                start_id = start_id.strip()
                end_id = end_id.strip()
                # print('Range: %s to %s' % (start_id, end_id))
                # print('Employee attendance:')
                # print(self.__printRangePresent(start_id, end_id))

                self.__output_file_contents.append('Range: %s to %s' % (start_id, end_id))
                self.__output_file_contents.append('Employee attendance:')
                self.__output_file_contents.append(self.__printRangePresent(start_id, end_id))


        except ValueError as ve:
            LOG.error("Numeric Value expected as an Employee ID (Error in value given in the prompt file: {0})".format(ve))
        except IOError as ie:
            LOG.error("Error in prompt file: {0} - {1}".format(file_name, str(ie)))

    def generate_output_file(self, output_file_name, overwrite_output_file=True):
        """ A Utility methods that writes the contents of the output to a file

        """
        if self.__output_file_contents:
            EmployeeAttendanceMonitoringSystem._write_output_file(output_file_name, self.__output_file_contents, rewrite=overwrite_output_file)
            print("\nPlease refer to %s for the overall attendance for the given input files." % os.path.join(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data_files', output_file_name))))


if __name__ == '__main__':

    input_file_name = 'inputPS1.txt'
    output_file_name = 'output.txt'
    prompt_file_name = 'promptsPS1.txt'

    org_emp_attendance = EmployeeAttendanceMonitoringSystem(input_file_name)
    org_emp_attendance.parseCommands(file_name=prompt_file_name)
    org_emp_attendance.generate_output_file(output_file_name, overwrite_output_file=True)
