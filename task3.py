# %% [markdown]
# To complete this task, there is a need to write two functions where the first function needs to be called (is_discount_applicable) within the body of the second function (book_price). Below are the function signatures:
# 
#     def is_discount_applicable(age, is_military, major, gpa):
# 
# **Description**:  
# For this function, your task is to check if a customer is eligible to receive a discount based on their age, military status, major, and GPA, according to the following criteria:
# - Persons in military services: are eligible.
# - Seniors (60 and above): are eligible.
# - Students in the 'CSE' major with a GPA of at least 3.7 are also eligible.
# 
# **Parameters**: 
# 
# `age` (int, indicating customer’s age)  
# `is_military` (bool, indicating the military status of customer)  
# `major` (str, indicating customer’s major)  
# `gpa` (float, indicating customer’s gpa)  
# 
# **Assumptions**: `gpa` is non-negative (>= 0) with maximum value of 4.
# 
# **Return value**: A bool, indicating whether the customer is eligible for a discount or not.
# 
# **Examples**:
# 
#     is_discount_applicable(16, False, “CSE”, 3.8) → True
#     is_discount_applicable(37, True, “”, 0.0) → True
#     is_discount_applicable(24, False, “ISt”, 4.0) → False
#     is_discount_applicable(71, False, “”, 0.0) → True
# 
#     def book_price(age, is_military, major, gpa, book_category):
# 
# **Description**:  
# For this function, your task is to call ‘is_discount_applicable’ function (defined earlier) and calculate the book price that a customer needs to pay. The bookstore has the following pricing structure for different book categories:
# - "science" and "fiction": $30
# - "novel" and "horror": $20
# - "mystery": $10
# - "comic": $15
# - Not among the categories listed above: $0
# 
# The bookstore offers discounts based on the user's eligibility for the following book categories:
# - 20% discount for "comic" and "fiction" categories of books.
# - 40% discount for "novel" books.
# - No discount for other book categories.
# 
# Using the above information, calculate the book price for the customer after discounts have been applied.
# 
# **Parameters**:  
# `age` (int, indicating customer’s age)  
# `is_military` (bool, indicating the military status of customer)  
# `major` (str, indicating customer’s major)  
# `gpa` (float, indicating customer’s gpa)  
# `book_category` (str, indicating the category of book)  
# 
# **Assumptions**: `gpa` is non-negative (>= 0) with maximum value of 4. `book_category` is all lowercase
# 
# **Return value**: A float, representing the book price for the customer.
# 
# **Examples**:
# 
#     book_price(16, False, “CSE”, 3.8, “fiction”) → 24.0
#     book_price(37, True, “”, 0.0, “mystery”) → 10.0
#     book_price(24, False, “IST”, 4.0, “comic”) → 15.0

# %%
def is_discount_applicable(age: int, is_military: bool, major: str, gpa: float) -> bool:
    """Check if a customer is eligible to receive a discount.

    Persons in military services: are eligible.
    Seniors (60 and above): are eligible.
    Students in the 'CSE' major with a GPA of at least 3.7 are also eligible.

    Args:
        age (int): indicating customer's age
        is_military (bool): indicating the military status of customer
        major (str): indicating customer's major
        gpa (float): indicating customer's gpa

    Returns:
        bool: indicating whether the customer is eligible for a discount or not.
    """
    return is_military or age >= 60 or (major.lower() == "cse" and gpa >= 3.7)

# %%
print(is_discount_applicable(16, False, "CSE", 3.8))  # True
print(is_discount_applicable(37, True, "", 0.0))  # True
print(is_discount_applicable(24, False, "ISt", 4.0))  # False
print(is_discount_applicable(71, False, "", 0.0))  # True

# %%
def book_price(
    age: int,
    is_military: bool,
    major: str,
    gpa: float,
    book_category: str,
) -> float:
    """Calculate the book price that a customer needs to pay.

    The bookstore has the following pricing structure for different book categories:
    - "science" and "fiction": $30
    - "novel" and "horror": $20
    - "mystery": $10
    - "comic": $15
    - Not among the categories listed above: $0

    The bookstore offers discounts based on the user's eligibility for the following book categories:
    - 20% discount for "comic" and "fiction" categories of books.
    - 40% discount for "novel" books.
    - No discount for other book categories.

    Using the above information, calculate the book price for the customer after discounts have been applied.

    Args:
        age (int): indicating customer's age
        is_military (bool): indicating the military status of customer
        major (str): indicating customer's major
        gpa (float): indicating customer's gpa
        book_category (str): indicating the category of book

    Returns:
        float: representing the book price for the customer.
    """

    if book_category == "science":
        price = 30
        discount = 0
    elif book_category == "fiction":
        price = 30
        discount = 0.2
    elif book_category == "novel":
        price = 20
        discount = 0.4
    elif book_category == "horror":
        price = 20
        discount = 0
    elif book_category == "mystery":
        price = 10
        discount = 0
    elif book_category == "comic":
        price = 15
        discount = 0.2
    else:
        price = 0
        discount = 0

    if is_discount_applicable(age, is_military, major, gpa):
        return price - (discount * price)

    return price

# %%
print(book_price(16, False, "CSE", 3.8, "fiction"))  # 24.0
print(book_price(37, True, "", 0.0, "mystery"))  # 10.0
print(book_price(24, False, "IST", 4.0, "comic"))  # 15.0


