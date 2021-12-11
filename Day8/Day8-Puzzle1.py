lines = open("Day8\\Day8.txt", "r").readlines()


for row in lines:
    
    digits = {0: "abcefg", 1: "cf", 2: "acdeg", 3:"acdfg", 4:"bcdf", 5:"abdfg", 6:"abdefg", 7:"acf", 8:"abcdefg", 9:"abcdfg"}

    decode = {"a":"abcdefg", "b":"abcdefg", "c":"abcdefg", "d":"abcdefg","e": "abcdefg", "f":"abcdefg", "g":"abcdefg"}
    
    spl = row.split(" | ")
    
    data = spl[1].split()
    
    data.extend(spl[0].split())
    
    print(*data)
    
    for num in data:
        l = len(num)
        c = -1
        if l == 2:
            c = 1
        if l == 4:
            c = 4
        if l == 3:
            c = 7
        # if l == 7:
        #     c = 8
        if c != -1:
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
            #remove value if determined one
            done = True
            for k in decode:
                if len(decode[k]) == 1:
                    done = False
                    for i in decode:
                        if i != k:
                            decode[i] = decode[i].replace(decode[k], "")
            
            print(num, "->", c, decode)
                

