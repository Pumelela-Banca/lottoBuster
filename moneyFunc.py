"""
Calculates the money gained if player played every
game since daly draw inception
"""


def count_wins(user_nums, winning_nums):
    """
    compares user numbers with winning numbers and counts
    possible winnable money
    :param user_nums: user numbers played
    :param winning_nums: winning numbers
    :return: amount of money won
    """
    wins = 0
    for ball in user_nums:
        if ball in winning_nums:
            wins += 1

    # TODO make winning_nums a class that shows actual wins for dates
    if wins == 0 or wins == 1:
        return -5
    elif wins == 2:
        return 5
    elif wins == 3:
        return 20
    elif wins == 4:
        return 500
    elif wins == 5:
        return 500000


if __name__ == "__main__":
    print(count_wins([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
