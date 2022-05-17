

class Pracownik:
  def __init__(self, imie, wynagrodzenie):
    self.imie_pracownika=str(imie)
    self.wynagrodzenie_brutto=int(wynagrodzenie)


  def wynagrodzenie_netto(self)->float:

      podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne=self.wynagrodzenie_brutto

      skladki_na_ubezpieczenia_spoleczne_finansowane_przez_pracownika=round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne*0.0976,2) + round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne*0.015,2) + round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne*0.0245,2)
            
      podstawa_wymiaru_skladki_na_ubezpieczenie_zdrowotne=podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne-skladki_na_ubezpieczenia_spoleczne_finansowane_przez_pracownika
      
      skladka_na_ubezpieczenie_zdrowotne_do_pobrania_z_wynagrodzenia = round(podstawa_wymiaru_skladki_na_ubezpieczenie_zdrowotne*0.09,2)
      
      skladka_na_ubezpieczenie_zdrowotne_do_odliczenia_od_podatku = round(podstawa_wymiaru_skladki_na_ubezpieczenie_zdrowotne*0.075,2)
      
      koszty_uzyskania_przychodu=111.25
          
      podstawa_obliczenia_zaliczki_podatek_dochodowy=self.wynagrodzenie_brutto-koszty_uzyskania_przychodu-skladki_na_ubezpieczenia_spoleczne_finansowane_przez_pracownika

      zaliczka_podatek_dochodowy_przed_odliczeniem_skladki_zdrowotnej=round(podstawa_obliczenia_zaliczki_podatek_dochodowy*0.18,2) - 46.33
        
      zaliczka_na_podatek_dochodowy_do_pobrania=zaliczka_podatek_dochodowy_przed_odliczeniem_skladki_zdrowotnej-skladka_na_ubezpieczenie_zdrowotne_do_odliczenia_od_podatku
      
      netto=self.wynagrodzenie_brutto-skladki_na_ubezpieczenia_spoleczne_finansowane_przez_pracownika-skladka_na_ubezpieczenie_zdrowotne_do_pobrania_z_wynagrodzenia-zaliczka_na_podatek_dochodowy_do_pobrania

      return netto

  def skladki_pracodawcy(self)->float:
    
    podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne=self.wynagrodzenie_brutto
    
    skladki_obciazajace_pracodawce=round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne*0.0976,2)+round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne*0.065,2)+round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne*0.0193,2)+round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne*0.0245,2)+round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne*0.001,2)
    
    return skladki_obciazajace_pracodawce

  def koszty_pracodawcy(self)->float:
    
    podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne=self.wynagrodzenie_brutto
    
    koszty_pracodawcy=round(round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne)+round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne*0.0976,2)+round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne*0.065,2)+round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne*0.0193,2)+round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne*0.0245,2)+round(podstawa_wymiaru_skladek_na_ubezpieczenia_spoleczne*0.001,2),2)
    
    return koszty_pracodawcy
laczny_koszt_pracodawcy=0

i=int(input())
pracownicy=[]
for index in range(0,i):
  pracownik_kwota=input().split(" ")
  pracownik=Pracownik(pracownik_kwota[0], pracownik_kwota[1])
  pracownicy.append(pracownik_kwota)

for index in range(0,i):
  pracownik_index=Pracownik(pracownicy[index][0],pracownicy[index][1])
  laczny_koszt_pracodawcy+=pracownik_index.koszty_pracodawcy()
  print(pracownicy[index][0]+ " " +str(format(pracownik_index.wynagrodzenie_netto(),'.2f'))+ " " +str(pracownik_index.skladki_pracodawcy())+ " " +str(pracownik_index.koszty_pracodawcy()))

print(float(format(laczny_koszt_pracodawcy,'2f')))
