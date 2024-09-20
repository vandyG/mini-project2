# %% [markdown]
# Manage a single parking lane
# 
#     def empty_or_full (parking_lane, capacity):
# 
# **Description**:  
# This function determines whether there is room in the parking lane and whether it is empty.
# 
# **Parameters**:  
# `parking_lane` (list of strings (list[str]) indicating the currently parked license plates)  
# `capacity` (an int, indicating the maximum number of cars that fit into the parking lane)  
# 
# **Assumptions**:  
# len(parking_lane) <= capacity, and capacity is positive (>= 1)
# 
# **Return value**: A str, as follows:
# - If parking_lane has no elements, return string "empty"
# - If the number of elements in parking_lane equals capacity, return string "full"
# - If the number of items in parking_lane is neither 0 nor capacity , return "neither"
# 
# **Examples**:
# 
#     empty_or_full(['RTY-5655', 'FF 22', 'LKJ-7250'], 3) → "full"
#     empty_or_full(['RTY-5655', 'FF 22', 'LKJ-7250'], 10) → "neither"
#     empty_or_full([], 1) → "empty"
# 
#     def park_cars (parking_lane, capacity, cars_to_park):
# 
# **Description**:  
# This function places more cars from cars_to_park into parking_lane, without exceeding capacity.
# 
# **Parameters**:  
# `parking_lane` (list of strings (list[str]) indicating the currently parked license plates)  
# `capacity` (an int, indicating the maximum number of cars that fit into the parking lane)  
# `cars_to_park` (list of strings (list[str]) indicating the cars to add to parking_lane)  
# 
# **Assumptions**: len(parking_lane) <= capacity, and capacity is positive (>= 1)
# 
# **Return value**: A list, representing the parking_lane after receiving updates from cars_to_park up to capacity. The cars in the returned list should preserve their original ordering from parking_lane followed by cars_to_park.
# 
# **Examples**:
# 
#     park_cars(['RTY-5655'], 2, ['FF 22', 'LKJ-7250']) → ['RTY-5655', 'FF 22']
#     park_cars(['RTY-5655'], 1, ['FF 22', 'LKJ-7250']) → ['RTY-5655']
#     park_cars(['RTY-5655'], 2, []) → ['RTY-5655']
#     
#     def retrieve_cars (parking_lane, cars_to_retrieve):
# 
# **Description**:  
# This function removes from parking_lane any cars that are in the list cars_to_retrieve.
# 
# **Parameters**:  
# `parking_lane` (list of strings (list[str]) indicating the currently parked license plates)  
# `cars_to_retrieve` (list of strings (list[str]) indicating the cars that need to be removed from parking_lane)  
# 
# **Assumptions**: parking_lane does not contain duplicate strings (no equal strings at different locations).
# 
# **Return value**: A list, representing the parking_lane list after removing cars from cars_to_retrieve. The cars in the returned list should preserve their original ordering.
# 
# **Examples**:
# 
#     retrieve_cars(['FF 22', 'LKJ-7250'], ['RTY-5655']) → ['FF 22', 'LKJ-7250']
#     retrieve_cars(['RTY-5655'], ['FF 22', 'LKJ-7250'])
#     retrieve_cars(['RTY-5655'], []) → ['RTY-5655'] → ['RTY-5655']
#     retrieve_cars(['RTY-5655'], ['RTY-5655']) → []
# 
# 
#     def check_cars (parking_lane, cars_to_check):
# 
# **Description**:  
# This function verifies whether all the cars in cars_to_check are in parking_lane.
# 
# **Parameters**:  
# `parking_lane` (list of strings (list[str]) indicating the currently parked license plates)  
# `cars_to_check` (list of strings (list[str]) indicating the cars to check)  
# 
# **Assumptions**: No assumptions.
# 
# **Return value**: A bool. This function returns True if all of the cars in cars_to_check are in parking_lane, and it returns False otherwise.
# 
# **Examples**:
# 
#     check_cars(['RTY-5655'], ['FF 22', 'LKJ-7250']) → False
#     check_cars(['FF 22', 'LKJ-7250'], ['RTY-5655']) → False
#     check_cars(['FF 22', 'LKJ-7250'], ['FF 22']) → True
#     check_cars(['RTY-5655'], []) → True

# %%

def empty_or_full(parking_lane: list[str], capacity: int) -> str:
    """Determines whether there is room in the parking lane and whether it is empty.

    Args:
        parking_lane (list of strings (list[str])): indicating the currently parked license plates
        capacity (an int): indicating the maximum number of cars that fit into the parking lane

    Returns:
        str: as follows:
        - If parking_lane has no elements, return string "empty"
        - If the number of elements in parking_lane equals capacity, return string "full"
        - If the number of items in parking_lane is neither 0 nor capacity , return "neither"
    """
    if len(parking_lane) == 0:
        return "empty"
    elif len(parking_lane) == capacity:
        return "full"
    else:
        return "neither"


def park_cars(
    parking_lane: list[str], capacity: int, cars_to_park: list[str]
) -> list[str]:
    """Places more cars from cars_to_park into parking_lane, without exceeding capacity.

    Args:
        parking_lane (list of strings (list[str])): indicating the currently parked license plates
        capacity (an int): indicating the maximum number of cars that fit into the parking lane
        cars_to_park (list of strings (list[str])): indicating the cars to add to parking_lane

    Returns:
        list: representing the parking_lane after receiving updates from cars_to_park up to capacity.
        The cars in the returned list should preserve their original ordering from parking_lane followed by
        cars_to_park.
    """
    for car in cars_to_park:
        if len(parking_lane) < capacity:
            parking_lane.append(car)
    return parking_lane


def retrieve_cars(parking_lane: list[str], cars_to_retrieve: list[str]) -> list[str]:
    """Removes from parking_lane any cars that are in the list cars_to_retrieve.

    Args:
        parking_lane (list of strings (list[str])): indicating the currently parked license plates
        cars_to_retrieve (list of strings (list[str])): indicating the cars that need to be removed from
        parking_lane

    Returns:
        list: representing the parking_lane list after removing cars from cars_to_retrieve. The cars in
        the returned list should preserve their original ordering.
    """
    for car in cars_to_retrieve:
        if car in parking_lane:
            parking_lane.remove(car)
    return parking_lane


def check_cars(parking_lane: list[str], cars_to_check: list[str]) -> bool:
    """Verifies whether all the cars in cars_to_check are in parking_lane.

    Args:
        parking_lane (list of strings (list[str])): indicating the currently parked license plates
        cars_to_check (list of strings (list[str])): indicating the cars to check

    Returns:
        bool: This function returns True if all of the cars in cars_to_check are in parking_lane, and it
        returns False otherwise.
    """
    for car in cars_to_check:
        if car not in parking_lane:
            return False
    return True

# %%

