def hex_to_binary(n):
    # 10진수로
    if ord('0') <= ord(n) <= ord('9'):
        num = int(n)
    else:
        num = ord(n) - ord('A') + 10
    # 2진수로
    binary = ''
    for i in range(4):
        binary = str(num % 2) + binary
        num //= 2
    return binary

print(hex_to_binary('2'))