"""
Programming for linguists

Implementation of the Reverse Polish Notation Converter
"""
from algorithms.calculator.reverse_polish_notation import ReversePolishNotation, Digit, BinaryOp
from data_structures.stack.stack import Stack
from algorithms.calculator.converter import ReversePolishNotationConverter


class ReversePolishNotationCalculator:
    """
    Calculator of expression in Reverse Polish Notation
    """
    def __init__(self):
        self.stack = Stack()

    def calculate(self, rpn_expression: ReversePolishNotation) -> float:
        """
        Main method of the ReversePolishNotationCalculator class.
        Calculating result of expression in Reverse Polish Notation.

        :param rpn_expression: expression in Reverse Polish Notation Format
        :return: result of the expression
        """
        for el in rpn_expression:
            if isinstance(el, Digit):
                el_d = el.digit
                self.stack.push(el_d)
            elif isinstance(el, BinaryOp):
                second_element = self.stack.top()
                self.stack.pop()
                first_element = self.stack.top()
                self.stack.pop()
                result = el._function(first_element, second_element)
                self.stack.push(result)
        result = self.stack.top()
        return result


if __name__ == '__main__':
    expression = {'Plus': '5+7+9', 'Minus': '78-4-20', 'Multiply': '46*7*8', 'Divide': '548/6/4', 'Power': '2^10',
                  'Brackets': '55-(20+5)', 'Mix': '75*2+(99/9)', 'With point': '.24-(78.5+9.5)'}
    for type_exp in expression:
        get_rnc = ReversePolishNotationConverter.convert(expression[type_exp])
        res_exp = ReversePolishNotationCalculator().calculate(get_rnc)
        to_check = eval(expression[type_exp])
        print(type_exp, '\t', expression[type_exp], '\t', 'my result:', round(res_exp, 3), '\t', 'check',
              round(to_check, 3), '\t', res_exp == to_check)
