#this script convert the str for the sanswitch

def wwnformat(wwn):
    i = 0
    form = ''
    wwn = wwn.lower()
    while i < 16:
        s = ''.join(wwn[i:i + 2])
        i = i + 2
        form = form + ':' + s
    return form[1:]

finput = open("input.txt","r",encoding="utf8")
foutput = open("output.txt","w",encoding="utf8")
for line in finput.readlines():
    temp=line.lower()
    foutput.writelines(wwnformat(temp)+"\n")
finput.close()
foutput.close()