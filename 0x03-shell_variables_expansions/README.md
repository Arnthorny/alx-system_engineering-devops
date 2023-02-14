#0x03	#Shell, init files, variables and expansions

11-binary_to_decimal:	This script converts BINARY variable from base 2 to base 10. It works because the default base for bash arithmethic operations is base 10. To specify a different base for a number, prefix the number with [base]#

12-combinations:	This script makes use of braces expansion to print all combinations of two letters, replaces the empty space separator with a new line and then greps out 'oo'.

13-print_float:		This script makes use of printf with the formating code "%.2f" to print variables to two d.p.

100-decimal_to...:	Uses printf with format code "%x" to convert the DECIMAL variable to hexadecimal

101-rot13:		This makes use of tr command to simulate the ROT13 cipher by replacing letters A-Z and a-z with N-Z+A-M and n-z+a-m. The ROT13 basically shifts each charcter by 13 places. E.g ABCD becomes NOPQ

102-odd:		This script uses cat to append a line number to each line, then deletes the excess prefixed spaces with tr. It then passes a regex which checks for the digit on each line, preceding a tab character. The -P option enables grep to interpret the regex as a Perl=compatible regex which then allows grouping in the regex. The last cut command removes other characters except the filenames.

103-water...:		This script uses tr to change the set the base of the variables. It converts the given base to base 5 '01234' and does addition in base 5. After addition it uses printd=f to convert the sum (now in base 10) to base 8 '01234567' as the given base was 'bestchol' an 8 letter string. tr is used again to convert the base 8 digit to base ;bestchol
