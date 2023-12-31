"""
Script has function to compare user submitted numbers to numbers
in a database.
"""
import sqlalchemy
import moneyFunc


def compare_numbers(user_numbers):
    """
    Compares user number with all  numbers in DB
    :param user_numbers: numbers played by user
    :return: amount of money won and amount of draws
    """
    engine = sqlalchemy.create_engine("sqlite:///database.db")
    metadata = sqlalchemy.MetaData()
    table = sqlalchemy.Table("daily_numbers", metadata,
                             autoload_with=engine)
    table = sqlalchemy.Table("daily_numbers", metadata,
                             autoload_with=engine)
    query = sqlalchemy.select(table)

    connection = engine.connect()

    result = connection.execute(query)

    # data is a list with [(id, date, numbers), (id, date, numbers)]
    data = result.fetchall()
    plays = len(data)
    wins_user = 0                              # amount of money won
    for nums in data:
        wins_user += moneyFunc.count_wins(user_numbers, str_to_list(nums[2]))

    return wins_user, plays


def str_to_list(value: str):
    """
    converts string to list
    :return: new list
    """
    new = [int(x) for x in value.split(", ")]
    return new


if __name__ == "__main__":
    # Test  for jack pot
    print(compare_numbers([8, 9, 11, 32, 33]))
    # Test for random
    print(compare_numbers([8, 9, 11, 16, 12]))
