rawstr = input('Enter a number:')
#If the code in try works the except is skipped
try:
    ival = int(rawstr)
except:
    ival = -1

#If the code in try fails, it jumps to the except and runs that code
if ival > 0:
    print('Nice work')
else:
    print('Not a number')