import os
import itertools

s = ['\n',' ', '\t']
data1 = {}
data2 = {}
n = 0
for a in itertools.product(s,repeat=10):
    data1[chr(n)] = ''.join(a)
    data2[''.join(a)] = chr(n)
    n+=1
    def encode(text):
        hash = ''
        for h in text:
            hash +=data1[h]
            return hash
            def decode(hash):
                text = ''
                while hash != '':
                    text+=data2[hash[:10]]
                    hash = hash[10:]
                    return text
                    def encodeFile(pathFile):
                        try:
                            hash = encode( open(pathFile , 'r').read() )
                            with open(pathFile,'w') as f:
                                f.write(hash)
                                except:
                                    exit('Error File')
                                    def decodeFile(pathFile):
                                        try:
                                            text = decode( open(pathFile , 'r').read() 
                                            with open(pathFile,'w') as f:
                                                f.write(text)
                                                except:
                                                    exit('Error File')
                                                    while 1:
                                                        os.system('clear')
                                                        print('\n\t\t1: Encode File')
                                                        print('\t\t2: Decode File')
                                                        i = input('\nEnter 1 or 2 : ')
                                                        if i != '1' and i != '2':
                                                            continue
                                                        p = input('Enter Path File : ')
                                                        if i == '1':
                                                            encodeFile(p)
                                                            else:
                                                                decodeFile(p)