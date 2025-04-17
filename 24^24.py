import itertools
import time
import string

cipher_text = input("Enter the cipher text (lowercase only): ")

letters = sorted(set(cipher_text))

start = time.time()

perms = list(itertools.permutations(string.ascii_lowercase, len(letters)))
i = 0
while i < len(perms):
    print(f"{i + 1}: {''.join(perms[i])}")
    i += 1

end = time.time()

print(f"\nNumber of attempts: {len(perms)}")
print(f"Time taken: {end - start:.2f} seconds")
