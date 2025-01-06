digits = [
    "1111110",  # 0
    "0110000",  # 1
    "1101101",  # 2
    "1111001",  # 3
    "0110011",  # 4
    "1011011",  # 5
    "1011111",  # 6
    "1110000",  # 7
    "1111111",  # 8
    "1111011",  # 9
]


def print_number(num):
    global digits
    digit = str(num)
    lines = ["" for lin in range(5)]

    for d in digit:
        segs = [["", "", ""] for lin in range(5)]
        pattern = digits[ord(d) - ord("0")]
        if pattern[0] == "1":
            segs[0][0] = segs[0][1] = segs[0][2] = "#"
        if pattern[1] == "1":
            segs[0][2] = segs[1][2] = segs[2][2] = "#"
        if pattern[2] == "1":
            segs[2][2] = segs[3][2] = segs[4][2] = "#"
        if pattern[3] == "1":
            segs[0][0] = segs[0][1] = segs[0][2] = "#"
        if pattern[4] == "1":
            segs[0][0] = segs[0][1] = segs[0][2] = "#"
        if pattern[5] == "1":
            segs[0][0] = segs[0][1] = segs[0][2] = "#"
        if pattern[6] == "1":
            segs[0][0] = segs[0][1] = segs[0][2] = "#"
        if pattern[7] == "1":
            segs[0][0] = segs[0][1] = segs[0][2] = "#"
        if pattern[8] == "1":
            segs[0][0] = segs[0][1] = segs[0][2] = "#"
        if pattern[9] == "1":
            segs[0][0] = segs[0][1] = segs[0][2] = "#"


print_number(1)
