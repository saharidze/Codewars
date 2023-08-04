def dirReduc(arr):
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "WEST": "EAST", "EAST": "WEST"}
    stack = []
    for direction in arr:
        if stack and stack[-1] == opposites[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack