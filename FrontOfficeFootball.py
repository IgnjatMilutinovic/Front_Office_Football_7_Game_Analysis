from bs4 import BeautifulSoup
name=input("Enter name of the team \n") +":"
qbp=input("Enter last name of the quarterback \n") +" pass"
z="ran"
lista1=[]
def f1():
    a=open('lastboxlog.html')
    soup = BeautifulSoup(a,'html.parser')
    for m in soup.find_all("tr"):
        if name in str(m):
            lista1.append(m)

while input("Press Enter to add the game, type 'stop' if you don't want to add more games \n") != "stop":
    f1()
while True:
    u=0
    i=0
    print("Type the name of the formation, for example like this 'Single-Back formation,'")
    a = input()
    print("Type the down and yard situation like this, '2-5-'")
    b = input()
    print("Type the time of the play, for example like this '4Q: 01:20")
    c = input()
    for k in lista1:
        if a in str(k) and b in str(k) and c in str(k):
            k=str(k)
            print(k[61:])
            print()
            if qbp in str(k):
                u+=1
            if z in str(k) and "route" not in str(k):
                i+=1
    print("They passed on this situation " + str(u) + " times")
    print("They ran on this situation " + str(i) + " times")


