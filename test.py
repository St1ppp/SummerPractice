def tokeniser(expression): # "2+3-5"
        minusflag = 1
        expression += ' '
        tokenlist = []
        token = ''
        chr = 0
        while chr < len(expression):
            if expression[chr] in ' ,':
                 chr += 1
            elif expression[chr] == '-' and minusflag == 1:
                token += expression[chr]
                while expression[chr + 1] in "0123456789.":
                    token += expression[chr + 1]
                    chr += 1
                tokenlist.append(token)
                token = ''
                chr += 1
                minusflag = 0
            elif expression[chr] in "0123456789.":
                token += expression[chr]
                while expression[chr + 1] in "0123456789.":
                    token += expression[chr + 1]
                    chr += 1
                tokenlist.append(token)
                token = ''
                chr += 1
            elif expression[chr] in "sctelm":
                token = expression[chr] + expression[chr + 1] + expression[chr + 2] + ('t' if expression[chr + 3] == 't' else '')
                tokenlist.append(token)
                token = ''
                chr += 3 + (1 if expression[chr + 3] == 't' else 0)
            else:
                token = expression[chr]
                tokenlist.append(token)
                token = ''
                chr += 1
        return tokenlist

print(tokeniser("-5 + 3"))