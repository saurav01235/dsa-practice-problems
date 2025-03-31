def convert_zigzag(s, numRows):
    # Edge case: if rows are 1 or string is too short for zigzag
    if numRows == 1 or numRows >= len(s):
        return s

    # Create an empty list of strings for each row
    rows = [""] * numRows
    print(rows)

    # Control variables
    curr_row = 0
    direction = 1   # 1 means up -1 means low
    going_up = False  # move up until 0 index matches

    # Traverse through each character
    for char in s:
        print(curr_row)
        rows[curr_row] += char

        if curr_row < numRows - 1 and not going_up:
            direction = 1
        elif curr_row == numRows - 1:
            going_up = True
            direction = -1

        if curr_row == 0:
            going_up = False
            direction = 1

        curr_row += direction







    print(rows)
    # Combine rows into the final result
    return "".join(rows)
#
#
# Test it out
str1 = "PAYPALISHIRING"
row = 3
result = convert_zigzag(str1, row)

print("Zigzag Output String:", result)
