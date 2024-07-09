n = int(input("O ile przesunąć?: "))
print("Proszę wprowadzić wiadmość z małych liter (spacje dozwolone)")
text = input("Wprowadź wiadomość: ")
alf=['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']
opcja= int(input("[1-kodowanie 0-dekodowanie]: "))
def encrypt_decrypt(n, text, opcja):
    global wynik 
    wynik =""
    for znak in text:
        if isinstance(znak, str):
            if opcja == 1:
              if znak == ' ':
                znak == ' '
              elif alf.index(znak) <= 34 - n:
                znak = alf[alf.index(znak) + n] 
              else:
                znak = alf[alf.index(znak) - 34 - 1 + n]
            elif opcja == 0:
              if znak == ' ':
                znak == ' '
              elif alf.index(znak) >= n:
                znak = alf[alf.index(znak) - n] 
              else:
                znak = alf[34 + 1 + alf.index(znak) - n]
        wynik += znak
encrypt_decrypt(n, text, opcja)
print("Przesunięcie:",n,'  ',"Oryginalny tekst:",text,"  ","Wynik:",wynik)