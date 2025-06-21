import requests
from os import system

def clear(): system("cls")

def resolve_batch(abc: str) -> list[int]:
    tmp = []
    tmp2 = []
    for itm in abc.split("\n"):
        tmp.append(itm)
    for itm in tmp:
        try:
            tmp2.append(int(itm))
        except:
            pass
    return tmp2
        

def getbatch() -> list[int]: # gets a random number
    url: str = "https://www.random.org/integers/?num=100&min=1&max=6&col=1&base=10&format=plain&rnd=new"
    
    res = requests.get(url).text
    
    return resolve_batch(res)

stats = {}
for number in getbatch():
    if not number in stats.keys():
        stats[number] = 1
        continue
    
    stats[number] += 1
    
    clear()
    for num, stat in stats.items():
        print(f"{num}: {stat}")

print("FINAL ^^^")