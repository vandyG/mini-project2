# %% [markdown]
# Manage two full lanes with the help with an empty spot, the bubble. The possible moves of a bubble are illustrated below.
# - Code O ("shift bubble to the Other lane"):  
# 
# **Parking Service**  
# 
#     RTY-5655 ZTR-0976
#     FF-22
#     LKJ-7250 N00B-DRV
#     BSD-9843 ONT123
# 
# **Parking Service**  
# 
#     RTY-5655 ZTR-0976
#              FF-22
#     LKJ-7250 N00B-DRV
#     BSD-9843 ERF-0076
# 
# - Code L ("shift bubble to the next Lower index):  
# 
# **Parking Service**  
# 
#     RTY-5655 ZTR-0976
#     FF-22
#     LKJ-7250 N00B-DRV
#     BSD-9843 ONT123
# 
# **Parking Service**  
# 
#     RTY-5655
#     FF-22   ZTR-0976
#     LKJ-7250 N00B-DRV
#     BSD-9843 ERF-0076
# 
# - Code H ("shift bubble to the next Higher index):  
# 
# **Parking Service**  
# 
#     RTY-5655 ZTR-0976 H
#     FF-22
#     LKJ-7250 N00B-DRV
#     BSD-9843 ONT123
# 
# **Parking Service**  
# 
#     RTY-5655 ZTR-0976
#     FF-22    N00B-DRV
#     LKJ-7250
#     BSD-9843 ERF-0076
# 
#     def swap_to_front (parking_lane, service_lane, car):
# 
# **Description**: 
# This function returns a list of move codes for the bubble to swap places with other cars so that eventually the specified car shifts to the front of its lane.
# 
# **Parameters**:  
# `parking_lane` (list of strings of the license plates or empty slot in the parking lane)
# `service_lane` (list of strings of the license plates or empty slot in the service lane)
# `car` (strrepresenting the license plate of the car that needs to be brought to the front)
# 
# **Assumptions**:  
# car is an element in one of the parking_lane or service_lane lists
# parking_lane and service_lane have equal lengths
# parking_lane and service_lane together do not contain any duplicate strings
# parking_lane and service_lane together contain the empty string '' in exactly one item.
# 
# **Return value**: A list[str] representing the codes of bubble moves that bring car to occupy the slot at index 0 in the lane list that contains car.

# %%
def swap_to_front(parking_lane, service_lane, car):
    """
    This function returns a list of move codes for the bubble to swap places with other
    cars so that eventually the specified car shifts to the front of its lane.

    Args:
        parking_lane (list of str): License plates or empty slot in the parking lane.
        service_lane (list of str): License plates or empty slot in the service lane.
        car (str): License plate of the car to be brought to the front.

    Returns:
        list of str: Codes of bubble moves to bring the car to the front.

    Assumptions:
        - 'car' is present in either 'parking_lane' or 'service_lane'.
        - 'parking_lane' and 'service_lane' have the same length.
        - No duplicates exist across 'parking_lane' and 'service_lane'.
        - Exactly one empty string '' is present across both lanes.
    """
    # Determine which lane the car is in
    car_lane = parking_lane if car in parking_lane else service_lane
    # Find the index of the car in its lane
    car_index = car_lane.index(car)
    
    # Determine which lane the bubble is in
    bubble_lane = parking_lane if "" in parking_lane else service_lane
    # Find the index of the bubble in its lane
    bubble_index = bubble_lane.index("")

    # Initialize the current index and the list of moves
    curr_index = car_index
    moves = []
    # Check if the car and the bubble are in the same lane
    is_same_lane = bubble_lane == car_lane

    # Iterate until the car reaches the front of its lane
    while curr_index != 0:
        # Get the moves to loop the bubble around the target car
        curr_moves = loop_around_target(is_same_lane, bubble_index, curr_index)
        # Extend the list of moves with the current moves
        moves.extend(curr_moves) 
        # Update the current index and the bubble index
        curr_index -= 1
        bubble_index = curr_index + 1
        # Since the bubble and the car are now next to each other in the same lane
        is_same_lane = True
    
    # Return the list of moves
    return moves

def go_beyond(distance, code):
    """
    This function returns a list of move codes for the bubble to go beyond a certain distance.

    Args:
        distance (int): The distance to go beyond.
        code (str): The move code to use.

    Returns:
        list of str: The list of move codes.
    """
    # Initialize an empty list to store the moves
    moves = []
    # Iterate over the distance
    for i in range(distance):
        # Append the move code to the list
        moves.append(code)
    # Return the list of moves
    return moves

def loop_around_target(is_same_lane: bool, bubble_index: int, target_index: int):
    """
    This function returns a list of move codes for the bubble to loop around a target index.

    Args:
        is_same_lane (bool): Whether the bubble and target are in the same lane.
        bubble_index (int): The index of the bubble.
        target_index (int): The index of the target.

    Returns:
        list of str: The list of move codes.
    """
    # If the bubble and the target are in the same lane and have the same index, raise an error
    if is_same_lane and bubble_index == target_index:
        raise ValueError("Target and bubble cannot be on same index.")
    
    # Calculate the distance between the bubble and the target
    distance = bubble_index - target_index
    # Initialize an empty list to store the moves
    moves = []

    # If the distance is negative, the bubble needs to move up
    if distance < 0:
        # Set the move code to "H"
        code = "H"
        # If the bubble and the target are not in the same lane, move the bubble to the other lane
        if not is_same_lane:
            moves.append("O")
        # Move the bubble up until it goes beyond the target
        moves.extend(go_beyond(abs(distance),code))
    # If the distance is positive, the bubble needs to move down
    else:
        # Set the move code to "L"
        code = "L"
        # If the bubble and the target are in the same lane, move the bubble to the other lane
        if is_same_lane:
            moves.append("O")
        # Move the bubble down until it goes beyond the target
        moves.extend(go_beyond(distance + 1, code))
        # Move the bubble to the other lane
        moves.append("O")
        # Move the bubble up one position
        moves.append("H")
    
    # Return the list of moves
    return moves


# %%
parking_lane = ["RTY-5655", "", "ABCD"]
service_lane = ["LKJ-7250", "NOOB-DRV", "BSD-9843"]
car_to_move = "BSD-9843"

expected_moves = ["O","H","O","L","L", "O", "H"]
result = swap_to_front(parking_lane, service_lane, car_to_move)

assert result == expected_moves, f"Expected {expected_moves}, but got {result}"
print("Test passed!")


