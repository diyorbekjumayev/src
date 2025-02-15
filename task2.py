# task2.py
def typeBasedTransformer(**kwargs):
    transformed_dict = {}

    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            transformed_dict[key] = value ** 2  # Square the number
        elif isinstance(value, str):
            transformed_dict[key] = value[::-1]  # Reverse the string
        elif isinstance(value, bool):
            transformed_dict[key] = not value  # Invert the boolean
        elif isinstance(value, (list, tuple)):
            transformed_dict[key] = value[::-1]  # Reverse the list/tuple
        elif isinstance(value, dict):
            transformed_dict[key] = {v: k for k, v in value.items()}  # Swap keys and values
        else:
            transformed_dict[key] = value  # Leave unchanged if unsupported

    return transformed_dict
