def is_tallest_double_of_shortest(heights: list):
    if not heights or len(heights) < 2:
        return False

    shortest_height = float('inf')
    tallest_height = float('-inf')

    for height in heights:
        if height < shortest_height:
            shortest_height = height
        if height > tallest_height:
            tallest_height = height

    return tallest_height >= 2 * shortest_height
