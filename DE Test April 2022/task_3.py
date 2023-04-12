# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.



# Not sure if this means 11:20:03 would be 11+20+3 (1) or 1+1+2+3 (2).

# [TODO]: fix the function
def sum_current_time_1(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    list_of_nums = map(lambda x: int(x), time_str.split(":"))
    return sum(list_of_nums)

def sum_current_time_2(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    list_of_nums = map(lambda x: int(x),
                       [num for num in time_str.replace(':', '')])
    return sum(list_of_nums)
