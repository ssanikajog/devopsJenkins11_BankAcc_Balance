import sys
if len(sys.argv) == 3:
  ini = int(sys.argv[1])
  dep = int(sys.argv[2])

else:
  ini = 1000
  dep = 500

total = ini + dep
print("Initial Balance: ", ini)
print("Deposit: ", dep)
print("Total Balance: ", total)
