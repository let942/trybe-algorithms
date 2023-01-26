def find_duplicate2(nums):
    dic = {}
    for num in nums:
        if type(num) == int and num > 0 and num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    for element in dic:
        if dic[element] > 1:
            return element
    return False


def find_duplicate(nums):
    if len(nums) < 2:
        return False
    duplicated = duplicated_or_none(nums)
    if duplicated is None:
        return False
    return duplicated


def duplicated_or_none(nums):
    uniq_nums = set()
    duplicated = None
    for num in nums:
        if type(num) != int or num < 1:
            return None
        if num in uniq_nums:
            duplicated = num
        else:
            uniq_nums.add(num)
    return duplicated