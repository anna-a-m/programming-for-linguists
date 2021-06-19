"""
Programming for linguists

Implementation of the Reverse Polish Notation Converter
"""
from algorithms.calculator.reverse_polish_notation import (Digit, Op, ReversePolishNotation,
                                                           OpenBracket, CloseBracket, BinaryOp)
from algorithms.calculator.reverse_polish_notation.binary_op import Plus, Minus, Multiplier, Divider, Power
from data_structures.queue_ import QueueDS
from data_structures.stack import Stack


class ReversePolishNotationConverterState:
    """
    Class to store the state of RPN convert process
    """
    def __init__(self, expression_in_infix_notation: str):
        """
        :param expression_in_infix_notation: string with expression in infix notation
        """
        self.expression_in_infix_notation = QueueDS(expression_in_infix_notation)
        self.expression_in_postfix_notation = ReversePolishNotation()
        self.stack = Stack()

    def pop_from_stack_until_opening_bracket(self):
        """
        Help function
        :return:
        """
        for el in self.stack:
            if isinstance(el, OpenBracket):
                break
            self.expression_in_postfix_notation.put(el)


class ReversePolishNotationConverter:
    """
    Class for converting infix expressions to reverse polish notation
    """
    point = '.'

    @staticmethod
    def convert(expression_in_infix_notation: str) -> ReversePolishNotation:
        """
        Main method of the class.
        Convert an infix expression to reverse polish notation

        :return: ReversePolishNotation object
        """
        state = ReversePolishNotationConverterState(expression_in_infix_notation)
        digits = ['']
        bin_ops = {'+': Plus, '-': Minus, '*': Multiplier, '/': Divider, '^': Power}
        open_bracket_flag = False
        while not state.expression_in_infix_notation.empty():
            ls = state.expression_in_infix_notation.top()
            if ReversePolishNotationConverter.is_part_of_digit(ls):
                digits[-1] += ls
            elif ls in bin_ops.keys():
                if digits[-1]:
                    state.expression_in_postfix_notation.put(Digit(digits[-1]))
                    # print(state.expression_in_postfix_notation._expression_queue.top())
                    digits.pop()
                    digits.append('')
                if state.stack.empty():
                    state.stack.push(bin_ops[ls]())
                else:
                    if not open_bracket_flag:
                        ReversePolishNotationConverter.pop_from_stack_until_prioritizing(bin_ops[ls](), state)
                    else:
                        state.stack.push(bin_ops[ls]())
            elif ls == '(':
                state.stack.push(OpenBracket())
                open_bracket_flag = True
            elif ls == ')':
                open_bracket_flag = False
                if digits[-1]:
                    state.expression_in_postfix_notation.put(Digit(digits[-1]))
                    digits.pop()
                    digits.append('')
                state.pop_from_stack_until_opening_bracket()
            else:
                raise ValueError('Calculator does not support this kind of symbols', ls)
            state.expression_in_infix_notation.get()
        if digits[-1]:
            state.expression_in_postfix_notation.put(Digit(digits[-1]))
            digits.pop()
        if not state.stack.empty():
            for el in state.stack:
                state.expression_in_postfix_notation.put(el)
        return state.expression_in_postfix_notation

    @staticmethod
    def pop_from_stack_until_prioritizing(operator: Op, state: ReversePolishNotationConverterState):
        """
        Help function to move elements from stack to state elements (operators)
        until element on the top of the stack  has less priority then current operator
        :param operator: Instance of Op class - current operator
        :param state: State of the RPN convert process
        """
        stack = state.stack
        if stack.top() == operator or operator > stack.top():
            for top in stack:
                state.expression_in_postfix_notation.put(top)
        stack.push(operator)

    @staticmethod
    def read_digit(state) -> Digit:
        """
        Method to read a digit from self._infix_notation

        :param state: expression in Reverse Polish Notation Format
        :return: Instance of Digit class
        """
        return Digit(state)

    @staticmethod
    def is_part_of_digit(character: str) -> bool:
        """
        Help function to check if symbol is a part of floating point number
        :param character: current symbol
        :return: True if character can be part of a digit, else False
        """
        return character.isdigit() or character == ReversePolishNotationConverter.point

    @staticmethod
    def is_open_bracket(operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is open bracket

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the open bracket operator else False
        """
        return isinstance(operator, OpenBracket)

    @staticmethod
    def is_close_bracket(operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is close bracket

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the close bracket operator else False
        """
        return isinstance(operator, CloseBracket)

    @staticmethod
    def is_binary_operation(operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is binary operator

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the binary operator else False
        """
        return isinstance(operator, BinaryOp)
