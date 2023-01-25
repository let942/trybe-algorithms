def study_schedule(permanence_period, target_time):
    count = 0
    if type(target_time) != int or target_time == 0:
        return None
    for tupla in permanence_period:
        if type(tupla[0]) != int or type(tupla[1]) != int:
            return None
        if tupla[0] <= target_time and tupla[1] >= target_time:
            count += 1
    return count