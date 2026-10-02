# Bit Operation of 12 and 25
# 12 = 00001100 (in binary)
# 25 = 00011001 (in binary)

# Bitwise operations in Python
A = 12
B = 25

print(f"A = {A:08b}")
print(f"B = {B:08b}")
print("A & B =", A & B, "=", format(A & B, "08b"))
print("A | B =", A | B, "=", format(A | B, "08b"))
print("A ^ B =", A ^ B, "=", format(A ^ B, "08b"))

# Example with the binary layout
print("00001100")
print("& 00011001")
print("________")
print("00001000 = 8 (in decimal)") 