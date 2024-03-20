def longest_sequence(n: int) -> int:
    # convert n to binary
    binary = bin(n)[2:]
    previous_length = 0
    current_length = 0
    max_length = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            current_length += 1
        else:
            if i < len(binary) - 1 and binary[i + 1] == '1':
                previous_length = current_length
                current_length = 0
            elif i < len(binary) - 1 and binary[i + 1] == '0':
                previous_length = 0
                current_length = 0
        max_length = max(max_length, previous_length + current_length + 1)
    return max_length