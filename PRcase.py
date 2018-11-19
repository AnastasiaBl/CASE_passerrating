'''Case-study #4 web page parsing
Developers:Anastasia Bliznyak.
'''
import urllib.request
f_in = open('input.txt', 'r')
f_out = open('output.txt', 'w')
url = f_in.readlines()
for i in url:
    f = urllib.request.urlopen(i)
    s = f.read()
    text = str(s)
    part_name = text.find("player-name")
    name = text[text.find('>', part_name)+1:text.find('&', part_name)]
    print(name)
    part_totals = text.find("player-totals")
    totals = text[text.find('>', part_totals) + 1: text.find('/tr', part_totals)]
    totals = totals.replace('TOTAL', '')
    totals = totals.replace('t', '')
    totals = totals.replace('n', '')
    totals = totals.replace('\\', '')
    totals = totals.replace('</d>', '')
    totals = totals.replace('<d>', ' ')
    totals = totals.replace('<', '')
    totals = totals.replace(',', '')
    totals1 = totals.split(' ')
    COMP = int(totals1[1])
    ATT = int(totals1[2])
    YDS = int(totals1[4])
    TD = int(totals1[6])
    INT = int(totals1[7])
    PASSER_RATING = ((((COMP / ATT - 0.3) * 5) + ((YDS / ATT - 3) * 0.25) + ((TD / ATT) * 20) + (2.375 - (INT / ATT * 25))) / 6) * 100
    PASSER_RATING = round(PASSER_RATING,2)
    print('{:<20}{:<7}{:<7}{:<7}{:<7}{:<7}{:<7}'.format(name, COMP, ATT, YDS, TD, INT, PASSER_RATING), file=f_out)
f_out.close()
f_in.close()