import pyautogui 
from time import sleep
from random_word import RandomWords

randomWord = RandomWords()

#Installare RandomWord e pyautogui per far funzionare lo script
#Prima di far partire lo script hoverare col mouse la barra di ricerca di bing, non toccare il mouse sennò il click fallisce

def getRandomWord():
    getWord = randomWord.get_random_word()
    return getWord

word = 0  # counter delle parole scritte
sleep(5)  # hai 5 secondi per hoverare prima del click
while (word < 30):  # inizia il loop, appena arriva a 30 parole scritte si interrompe
    pyautogui.click()  # clicca col mouse
    counter = len(str(word))  # fa un check sulla lunghezza della parola e la cancella
    while counter > 0:  # Se la parola è maggiore di 0 fa il check per cancellarla
        pyautogui.press('backspace')  # clicca indietro fino ad arrivare a 0
        counter -= 1  
    pyautogui.write(getRandomWord())  # scrive una parola random da questa libreria
    pyautogui.press('enter',1,5)  # preme invio, 1 per farlo cliccare (con 0 non clicca), 5 è il wait
    sleep(5)  # ulteriore wait per evitare che bing non calcoli i punti
    word += 1  # aumenta il counter di word di 1 e ricomincia il loop
    print(f"Ricerca numero {word} finita")
print("Finito il loop")