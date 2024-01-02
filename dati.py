from random_word import RandomWords
import os
randomWord = RandomWords()

def getRandomWord():
    getWord = randomWord.get_random_word()
    return getWord

password_login = os.getenv("PASSWORD_LOGIN")
email_login = os.getenv("EMAIL_LOGIN")
directory = os.getenv("DIRECTORY")
# edge_dir = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

bing_url = "https://www.bing.com/search?q=ss&form=QBLH&sp=-1&ghc=1&lq=0&pq=ss&sc=11-2&qs=n&sk=&cvid=133DE369E02F41CCA18BB28FBF10660F&ghsh=0&ghacc=0&ghpl="
