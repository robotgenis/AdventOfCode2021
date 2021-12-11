
def runDecode(c, num, decode, digits):
    decode = decode.copy()
    remove = "abcdefg"
    
    #determine all variables not in digit value
    for i in digits[c]:
        remove = remove.replace(i, "")
    #remove all other value from the currently connected ones
    for k in num:
        for i in remove:
            decode[k] = decode[k].replace(i, "")
    
    #remove from on decode
    removeFrom = "abcdefg"
    for i in num:
        removeFrom = removeFrom.replace(i, "")
    
    #removed connected values from all other connections
    for k in removeFrom:
        for i in digits[c]:
            decode[k] = decode[k].replace(i, "")
    return decode

lines = open("Day8\\Day8.txt", "r").readlines()



total = 0
for row in lines:
    
    digits = {0: "abcefg", 1: "cf", 2: "acdeg", 3:"acdfg", 4:"bcdf", 5:"abdfg", 6:"abdefg", 7:"acf", 8:"abcdefg", 9:"abcdfg"}

    decode = {"a":"abcdefg", "b":"abcdefg", "c":"abcdefg", "d":"abcdefg","e": "abcdefg", "f":"abcdefg", "g":"abcdefg"}
    
    spl = row.split(" | ")
    
    data = spl[1].split()
    
    data.extend(spl[0].split())
    
    print(*data)
    

    while True:
        
        decodeCopy = decode.copy()
        for num in data:
            l = len(num)
            
            #find possible numbers
            possible = []
            
            for i in digits:
                if len(digits[i]) == l:
                    test = runDecode(i, num, decode, digits)
                    for k in test:
                        if len(test[k]) == 0:
                            break
                    else:
                        possible.append(i)

            c = -1
            if(len(possible) == 1):
                c = possible[0]
                
            if c != -1:
                
                decode = runDecode(c, num, decode, digits)

                #remove value if determined one
                done = True
                for k in decode:
                    if len(decode[k]) == 1:
                        done = False
                        for i in decode:
                            if i != k:
                                decode[i] = decode[i].replace(decode[k], "")
                
                #print(num, "->", possible, decode)
            else:
                #print(num, "->", possible)
                pass
        if decodeCopy == decode:
            break
    print(decode)
    #decode final message with decode
    n = ""
    for num in spl[1].split():
        st = ""
        for letter in num:
            st += decode[letter]
        
        st = "".join(sorted(st))
            

        for i in digits:
            if digits[i] == st:
                 n += str(i)
    print(n)
    total += int(n)
        
print(total)           

