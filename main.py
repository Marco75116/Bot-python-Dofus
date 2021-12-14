import pytesseract
import pyautogui
from PIL import Image
from PIL import ImageGrab
import sqlite3
import time

pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

# these methods simulate mouse actions.
def cVi(nb):
    for i in range(nb):
       pyautogui.click(1109,345)
       time.sleep(0.2)
def cfo(nb):
    for i in range(nb):
        pyautogui.click(1111,374)
        time.sleep(0.2)
def csa(nb):
    for i in range(nb):
        pyautogui.click(1111,426)
        time.sleep(0.2)
def ccri(nb):
    for i in range(nb):
        pyautogui.click(1112,461)
        time.sleep(0.5)
def cdo(nb):
    for i in range(nb):
        pyautogui.click(1112,499)
        time.sleep(0.5)
def cpro(nb):
    for i in range(nb):
        pyautogui.click(1108,534)
        time.sleep(0.5)
def cPapro(nb):
    for i in range(nb):
        pyautogui.click(1166,534)
        time.sleep(0.2)
def cPavi(nb):
    for i in range(nb):
       pyautogui.click(1160,339)
       time.sleep(0.5)
def cPafo(nb):
    for i in range(nb):
        pyautogui.click(1158,380)
        time.sleep(0.5)
def cPasa(nb):
    for i in range(nb):
        pyautogui.click(1163,414)
        time.sleep(0.5)
def cPaterre(nb):
    for i in range(nb):
        pyautogui.click(1155,650)
        time.sleep(0.5)
def cPaeau(nb):
    for i in range(nb):
        pyautogui.click(1163,698)
        time.sleep(0.5)
def cPerneutre(nb):
    for i in range(nb):
        pyautogui.click(1109,571)
        time.sleep(0.5)
def cPerterre(nb):
    for i in range(nb):
        pyautogui.click(1113,611)
        time.sleep(0.5)

#this method makes it possible to identify and reorganize the data flows in a precise order
def findl1(carac):
    if carac.find('Vita')!=-1 or  carac.find('ar AIC    ')!=-1 or  carac.find('SPARC')!=-1 or  carac.find('SEA')!=-1 or  carac.find('SAIC')!=-1 or carac.find('SPER')!=-1  or  carac.find('aC')!=-1  or carac.find('aVERIC')!=-1 or carac.find('SEEAVIC UC')!=-1 or carac.find('SEER')!=-1 or carac.find('SPA')!=-1 or carac.find('SAC')!=-1 or carac.find('SEPA')!=-1 or carac.find('aA')!=-1  :
        return 0
    if carac.find('For') != -1 or carac.find('ey') != -1:
        return 1
    if carac.find('Sag')!=-1:
        return 2
    if carac.find('Crit')!=-1:
        return 3
    if carac.find('Domm')!=-1:
        return 4
    if carac.find('Pros')!=-1:
        return 5
    if carac.find('% Résistance N')!=-1:
        return 6
    if carac.find('%Résistance N')!=-1:
        return 6
    if carac.find('% Résistance Te')!=-1:
        return 7
    if carac.find('%Résistance Te')!=-1:
        return 7
    if carac.find('Terre')!=-1:
        return 8
    if carac.find('Eau')!=-1:
        return 9


#these methods will calculate and perform the necessary click from a data
def svita(caract):
        if caract[0]<185 and caract[0]!=-1:
            a=200-caract[0]
            a=a//15
            cPavi(a)
def sfo(caract):
        if caract[1]<44 and caract[1]!=-1:
            a=50-caract[1]
            a=a//3
            cPafo(a)
def ssa(caract):
        if caract[2]<22 and caract[2]!=-1:
            a=25- caract[2]
            a=a//3
            cPasa(a)
def scri(caract):
        if caract[3]<4 and caract[3]!=-1:
            ccri(1)
def sdo(caract):
        if caract[4]<4 and caract[4]!=-1:
            cdo(1)
def spro(caract):
        if caract[5]<22 and caract[5]!=-1:
            a=20-caract[5]
            a=a//3
            cPapro(a)
def spneutre(caract):
        if caract[6]<10 and caract[6]!=-1:
            cPerneutre(1)
def spterre(caract):
        if caract[7] < 10 and caract[7]!=-1:
            cPerterre(1)
def sterre(caract):
        if caract[8] < 7 and caract[8]!=-1 :
            a = 10 - caract[8]
            a=a//3
            cPaterre(a)
def seau(caract):
        if caract[9] < 7 and caract[0]!=-1:
            a = 10 - caract[9]
            a=a//3
            cPaeau(a)

#This method will take an image, retrieve the image data, and return a sorted list of the informations I need
def carac():
    time.sleep(1)
    screen = ImageGrab.grab(bbox=(376, 147, 606, 340))
#    screen.show()
    text = pytesseract.image_to_string(screen, config='')
    caractèrestoremove = "."
    text = text.replace(caractèrestoremove, "")
    print(text)
    l2 = text.split("\n")
    l1 = l2.copy()
    for i in range(len(l2)-1, -1, -1):
        if l2[i] == "" or l2[i] == " ":
            del l2[i]
    del l2[-1]
    print(l2)
    l1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(l2)):
        l1[findl1(l2[i])] = l2[i]
    print(l1)
    alphab = "abcdefghijklmnopqrstuvxyzT%EVFSCDPRéN|_ |"
    for i in range(len(l1)):
        for l in alphab:
            l1[i] = l1[i].replace(l, "")

    for i in range(len(l1)):
        l1[i] = l1[i].replace("O", "0")
        try:
            l1[i]= int(l1[i])
        except :
            l1[i]=-1
    print(l1)
    return l1



#this makes all functions work, cw=catecteristique wanted
def first(tab,cw0,cw1,cw2,cw3,cw4,cw5,cw6,cw7,cw8,cw9,cw10,cw11):
    if tab[0]<cw0 and tab[0]!=-1:
        cPavi(1)
    if tab[1] < cw1 and tab[1]!=-1:
        cPafo(1)
    if tab[5] < cw2 and tab[5]!=-1:
        a = 20 - tab[5]
        a = a // 3
        cPapro(a-1)
    if tab[0]<cw3 and tab[0]!=-1:
        a=200-tab[0]
        a=a//15
        cPavi(a-1)
    if tab[1] < cw4 and tab[1]!=-1:
        a = 50 - tab[1]
        a = a // 3
        cPafo(a-2)
    if tab[8] < cw5 and tab[8] != -1:
        time.sleep(0.5)
        cPaterre(1)
    if tab[9] < cw6 and tab[9] != -1:
        cPaeau(1)
    if tab[2] < cw7 and tab[2] != -1:
        a = 25 - tab[2]
        a = a // 3
        cPasa(a)
    if tab[6] < cw8 and tab[6] != -1:
        time.sleep(0.5)
        cPerneutre(1)
    if tab[7] < cw9 and tab[7] != -1:
        time.sleep(0.5)
        cPerterre(1)
    if tab[3] < cw10 and tab[3] != -1:
        time.sleep(0.5)
        ccri(1)
    if tab[4]< cw11 and tab[4] != -1:
        time.sleep(0.5)
        cdo(1)

#I loop until my object has the desired characteristics
while True:
    first(carac(),185,45,5,100,25,7,7,20,10,10,4,4)



