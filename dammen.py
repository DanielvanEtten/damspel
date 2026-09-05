from game2dboard import Board
from tkinter import messagebox
#https://github.com/mjbrusso/game2dboard/tree/master

aantal_kolommen = 10
aantal_rijen = 10

spelbord = None
scherm = None
geselecteerde_steen = None
actieve_speler = "wit"

#functie definities
def maak_spelbord():
    #met nested list comprehension eerst rijen dan kolommen invullen. Stenen alleen op oneven r+c combinaties
    return [
        [
            "zwart" if (r + c) % 2 != 0 and r < 4 else
            "wit" if (r + c) % 2 != 0 and r >= aantal_rijen - 4 else
            "leeg"
            for c in range(aantal_kolommen)
        ]
        for r in range(aantal_rijen)
    ]


def update_scherm():
    #poets waarde "leeg" weg voor presentatie
    visueel_bord = [[None if cel == "leeg" else cel for cel in rij] for rij in spelbord]
    scherm.load(visueel_bord)
    

def verwijder_vijand(van_rij, van_kol, naar_rij, naar_kol):
    tussen_rij = (van_rij + naar_rij) // 2
    tussen_kol = (van_kol + naar_kol) // 2
    spelbord[tussen_rij][tussen_kol] = "leeg"


def is_geldige_zet(van_rij, van_kol, naar_rij, naar_kol, speler):
    
    #Controleert de zet en geeft een tuple terug: (is_geldig, is_slagzet)

    if not (0 <= naar_rij < aantal_rijen and 0 <= naar_kol < aantal_kolommen):
        return False, False

    klik_waarde = spelbord[naar_rij][naar_kol]
    vijand = "zwart" if speler == "wit" else "wit"

    rij_verschil = naar_rij - van_rij
    kol_verschil = abs(naar_kol - van_kol)

    # 1. Normale loopzet
    juiste_richting = (
        (speler == "wit" and rij_verschil == -1)
        or
        (speler == "zwart" and rij_verschil == 1)
    )
    if juiste_richting and kol_verschil == 1 and klik_waarde == "leeg":
        return True, False  # Geldig, maar GEEN slagzet

    # 2. Slagzet
    juiste_slag_richting = (
        (speler == "wit" and rij_verschil == -2)
        or
        (speler == "zwart" and rij_verschil == 2)
    )
    if juiste_slag_richting and kol_verschil == 2 and klik_waarde == "leeg":
        tussen_rij = (van_rij + naar_rij) // 2
        tussen_kol = (van_kol + naar_kol) // 2

        # Data-check: staat er daadwerkelijk een vijand?
        if spelbord[tussen_rij][tussen_kol] == vijand:
            return True, True  # Geldig EN een slagzet

    return False, False


def kan_steen_slaan(r, c, speler):
    stap_rij = -2 if speler == "wit" else 2
    for stap_kol in [-2, 2]:
        geldig, slag = is_geldige_zet(r, c, r + stap_rij, c + stap_kol, speler)
        if geldig and slag:
            return True
    return False


def speler_heeft_slagopties(speler):
    for r in range(aantal_rijen):
        for c in range(aantal_kolommen):
            if spelbord[r][c] == speler:
                if kan_steen_slaan(r, c, speler):
                    return True
    return False

#Interface functies
def vakje_geklikt(btn, row, col):
    global geselecteerde_steen, actieve_speler

    klik_waarde = spelbord[row][col]

    if klik_waarde == actieve_speler:
        geselecteerde_steen = (row, col)
        print(f"Geselecteerd: {actieve_speler} op (rij {row}, kolom {col})")
        return

    if geselecteerde_steen:
        van_rij, van_kol = geselecteerde_steen

        # Vraag direct aan de logica of de zet geldig is én of het een slag betreft
        is_geldig, is_slagzet = is_geldige_zet(van_rij, van_kol, row, col, actieve_speler)

        if is_geldig:
            moet_slaan = speler_heeft_slagopties(actieve_speler)

            # Slagverplichting controle op basis van de zet-data
            if moet_slaan and not is_slagzet:
                print("Ongeldige zet: Slaan is verplicht!")
                messagebox.showwarning("Slagverplichting", "Je bent verplicht om te slaan!")
                geselecteerde_steen = None
                return

            # Verplaats de steen
            spelbord[row][col] = actieve_speler
            spelbord[van_rij][van_kol] = "leeg"

            # Verwijder de vijand als de logica heeft bevestigd dat dit een slagzet is
            if is_slagzet:
                verwijder_vijand(van_rij, van_kol, row, col)

            geselecteerde_steen = None
            actieve_speler = "zwart" if actieve_speler == "wit" else "wit"
            

            print(f"Zet succesvol! Nu aan de beurt: {actieve_speler}")
            update_scherm()

        else:
            print("Ongeldige zet!")
            geselecteerde_steen = None

##Het "hoofdprogramma"
def main():
    global spelbord, scherm
    
    # Initialiseer data en interface
    spelbord = maak_spelbord()
    
    scherm = Board(aantal_rijen, aantal_kolommen)
    scherm.title = f"Rechthoekig Dammen ({aantal_kolommen}x{aantal_rijen})"
    scherm.cell_size = 70
    scherm.on_mouse_click = vakje_geklikt
    
   
    update_scherm()
    scherm.show()


if __name__ == "__main__":
    main()