def calculate_mean(values: list[float]) -> float:
    if not values:
        raise ValueError("Input list cannot be empty")
    return sum(values) / len(values)
