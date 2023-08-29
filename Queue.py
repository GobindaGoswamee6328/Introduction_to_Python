
from collections import deque

bank = deque (["joy","Bijoy","Anis"])
print(bank)

bank.popleft()
print(bank)
bank.popleft()
bank.popleft()

if not bank:
    print("No Person Left")
