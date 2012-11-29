import sys
if len(sys.argv) == 1:
    print 'Error: No arguments given.'
    exit()
sum = 0
for num in sys.argv[1:]:
    sum += float(num)
print sum / (len(sys.argv) - 1)