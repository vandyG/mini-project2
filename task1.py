"""This module contains a function that recommends a gift based on user's preference and budget."""

# For this function, your task is to recommend a gift based on user's preference and
# budget, the parameters of the function. The function should return a string recommending a gift
# based on the following conditions:

# | Preference        | Budget                                  | Gift (return string) |
# |-------------------|-----------------------------------------|----------------------|
# | electronics       | Equal or under $100                     | "gaming earbuds"     |
# | electronics       | Above $100 but under or equal $200      | "headphone"          |
# | electronics       | Above $200                              | "smart watch"        |
# | clothing          | Equal or under $25                      | "tops"               |
# | clothing          | Equal or under $50 but above $25        | "jackets"            |
# | clothing          | Equal or under $100 but above $50       | "shoes"              |
# | clothing          | Above $100                              | "suits"              |
# | jewelry           | Under $500                              | "ring"               |
# | jewelry           | Equal or above $500 but under $1000     | "necklace"           |
# | jewelry           | Equal or above $1000                    | "bracelet"           |
# | not listed above  | any price                               | "decorative gifts!"  |


def gift_recommender(preference, budget):
    """Recommends a gift based on user's preference and budget.

    Args:
        preference: The user's preference for the gift.
        budget: The user's budget for the gift.

    Returns:
        A string recommending a gift based on the user's preference and budget.
    """
    if preference == "electronics":
        if budget <= 100:
            return "gaming earbuds"
        elif budget <= 200:
            return "headphone"
        else:
            return "smart watch"
    elif preference == "clothing":
        if budget <= 25:
            return "tops"
        elif budget <= 50:
            return "jackets"
        elif budget <= 100:
            return "shoes"
        else:
            return "suits"
    elif preference == "jewelry":
        if budget < 500:
            return "ring"
        elif budget < 1000:
            return "necklace"
        else:
            return "bracelet"
    else:
        return "decorative gifts!"
