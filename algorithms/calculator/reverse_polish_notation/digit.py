"""
Programming for linguists

Interfaces for digits
"""
from typing import Union

from algorithms.calculator.reverse_polish_notation.element import Element


class Digit(Element):
    """
    Interface for presenting a digit
    """

    def __init__(self, digit_as_string: Union[float, str]):
        if isinstance(digit_as_string, str):
            digit_as_string = float(digit_as_string)
        self.digit = digit_as_string

    def __str__(self) -> str:
        """
        Magic method to present an instance of this class as string
        """
        return str(self.digit)

    def __eq__(self, other: 'Digit') -> bool:
        """
        Magic method to compare instances of Digit class
        """
        return float(self.digit) == Digit

