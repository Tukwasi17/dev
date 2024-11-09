import random

binary_num = ''.join([str(random.choice([0, 1])) for _ in range(4)])
decimal_num = int(binary_num, 2)

print(f"random binary number: {binary_num}, decimal: {decimal_num}")