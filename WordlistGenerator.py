#import time
#from progress.bar import IncrementalBar
def GenerateWords(leght, words = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    Programm = True
    password = list("0" * leght)
    final = []
    len_passord = len(words) ** leght
    #print(len_passord)
    #bar = IncrementalBar('[*] Generate passwords', max=len_passord, suffix='%(percent).1f%%')
    while Programm:
        i = leght - 1
        while i >= 0:
            if i != 0:
                if int(password[i]) >= len(words):
                    password[i-1] = int(password[i-1]) + 1
                    password[i] = 0
            i -= 1
            if password[0] == len(words):
                Programm = False
        if Programm != False:
            temp = ""
            for i in range(leght):
                temp += words[int(password[i])]
            final.append(temp)
            password[leght - 1] = int(password[leght - 1]) + 1
        #bar.next()
   #bar.finish()
    return final

if __name__ == "__main__":
    #start_time = time.time()
    passwd = GenerateWords(4)
    #print("--- %s seconds ---" % (time.time() - start_time))
    #По желанию
    #file = open("passwd.txt", "w")
    #for item in passwd:
    #    file.write(f"{item}\n")
    #file.close()
