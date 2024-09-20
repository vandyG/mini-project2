# To complete this task, you need to write two functions to calculate student’s final grade:  

# >calculate_student_score and calculate_letter_grade, where the output of the first function will be use as the parameter for the second function.  

# Below are the required function signatures:

#     def calculate_student_score(PA, mid_term_exam, final_exam):
# **Description**:  
# For this function, your task is to calculate a student's weighted score based on their Programming Assignment (PA), mid-term, and final exam scores. If a student has a score of zero in the final exam, they will receive a weighted score of zero, regardless of their other scores. If the midterm exam is not taken (score is zero), the score of the final exam will be used as a replacement.

# Additionally, please take into account the following weightage for each score:
# - PA score carries a weight of 40%.
# - Mid-term exam score carries a weight of 30%.
# - Final exam score carries a weight of 30%.

# **Parameters**:  
# `PA` (float, denoting student’s PA score)  
# `mid_term_exam` (float, denoting student’s mid-term exam score)  
# `final_exam` (float, denoting student’s final exam score)  

# **Assumptions**:  
# scores are non-negative (>= 0) with a maximum value of 100.

# **Return value**:  
# A float, indicating the students’ weighted score.

# **Examples**:

#     calculate_student_score(100.0, 90.0, 95.0) → 95.5  
#     calculate_student_score(50.0, 70.0, 0.0) → 0.0  
#     calculate_student_score(80.0, 0.0, 50.0) → 62.0  

#     def calculate_letter_grade(score):
    
# **Description**:  
# For this function, your task is to assess a student's score and determine their final letter grade based on the following criteria:

# > Scores between (90 – 100] → “A”  
# > Scores between (80 – 90] → “B”  
# > Scores between (70 – 80] → “C”  
# > Scores between [60 – 70] → “D”  
# > Scores below 60 → “F”  

# **Parameters**:  
# `score` (float, denoting student’s score)

# **Assumptions**: `score` is non-negative (>= 0) with a maximum value of 100.
# **Return value**: A str, indicating the students’ final grade.

# **Examples**:

#     calculate_letter_grade(95.5) → “A”
#     calculate_letter_grade(0.0) → “F”
#     calculate_letter_grade(62.0) → “D”

def calculate_student_score(
    PA: float = 0.0, mid_term_exam: float = 0.0, final_exam: float = 0.0
) -> float:
    """Calculate studet score.

    Calculate a student's weighted score based on their Programming Assignment (PA), mid-term, and
    final exam scores. If a student has a score of zero in the final exam, they will receive a
    weighted score of zero, regardless of their other scores. If the midterm exam is not taken
    (score is zero), the score of the final exam will be used as a replacement.

    Additionally, please take into account the following weightage for each score:
    - PA score carries a weight of 40%.
    - Mid-term exam score carries a weight of 30%.
    - Final exam score carries a weight of 30%.

    Args:
        PA (float): denoting student's PA score
        mid_term_exam (float): denoting student's mid-term exam score
        final_exam (float): denoting student'ArithmeticErrors final exam score

    Returns:
        float: indicating the students' weighted score.
    """
    if final_exam == 0:
        return 0.0
    elif mid_term_exam == 0:
        return PA * 0.4 + final_exam * 0.3 + final_exam * 0.3
    else:
        return PA * 0.4 + final_exam * 0.3 + mid_term_exam * 0.3


def calculate_letter_grade(score: float) -> str:
    """Assess a student's score and determine their final letter grade.

    Scores between (90 - 100] -> “A”
    Scores between (80 - 90] -> “B”
    Scores between (70 - 80] -> “C”
    Scores between [60 - 70] -> “D”
    Scores below 60 -> “F”

    Args:
        score (float): denoting student's score

    Returns:
        str: indicating the students' final grade.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
