"""
Programming for linguists

Interfaces for brackets
"""
from algorithms.calculator.reverse_polish_notation.op import Op


class Bracket(Op):
    """
    Base interface for brackets
    """
    @staticmethod
    def _function(*args, **kwargs) -> float:
        return NotImplementedError


class OpenBracket(Bracket):
    """
    Interface for open bracket
    """
    priority = 1
    symbol = '('


class CloseBracket(Bracket):
    """
    Interface for close bracket
    """
    priority = 1
    symbol = ')'
