import logging
from dataclasses import dataclass
from decimal import Decimal
from itertools import combinations


PAYMENT: int = 0


@dataclass
class GameCombin:
    bet: int
    size: int


def multiplication(lst: list, combination: GameCombin):
    """計算組合賠率"""
    n = len(lst)
    if n < combination.size:
        yield 0
    for comb in combinations(range(n), combination.size):
        result = combination.bet
        global PAYMENT
        PAYMENT += combination.bet
        for idx in comb:
            result *= Decimal(str(lst[idx]))
        yield round(result)


one_game_combin = GameCombin(bet=100, size=1)
two_game_combin = GameCombin(bet=10, size=2)
three_game_combin = GameCombin(bet=10, size=3)
four_game_combin = GameCombin(bet=0, size=4)
five_game_combin = GameCombin(bet=0, size=5)
six_game_combin = GameCombin(bet=0, size=6)


odds_list = [2.8, 2.8, 3.2, 0, 0]
total = sum(multiplication(odds_list, one_game_combin))
total += sum(multiplication(odds_list, two_game_combin))
total += sum(multiplication(odds_list, three_game_combin))
total += sum(multiplication(odds_list, four_game_combin))
total += sum(multiplication(odds_list, five_game_combin))
total += sum(multiplication(odds_list, six_game_combin))

print(f"總共支付: {PAYMENT}\t中獎金額: {total}\t獲利: {total-PAYMENT}")
