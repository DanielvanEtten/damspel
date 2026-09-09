# Dit spelletje is gebouwd door Daniël van Etten

Het spelletje is een eerste implementatie van dammen. Dit is een multi-player spelletje waarbij damstukken met de muis verplaatst kunnen worden. 
Beide spelers maken gebruik van dezelfde computer en muis.

# De volgende regels zijn geïmplementeerd:

Speelbord met 10*10 vlakken.
Zet-validatie: Controleert of zetten diagonaal en in de juiste richting (vooruit) worden uitgevoerd.
Slaglogica: Ondersteunt het overslaan en direct verwijderen van vijandelijke stenen.
Slagverplichting: Het spel controleert actief of een speler kan slaan. Als er een slag mogelijk is, dwingt het spel de speler om te slaan. Dit gebeurt door niet-slagen te verbieden vergezeld van een begrijpelijke pop-up met foutmelding.
Beurtwisseling: Automatische wisseling tussen de witte en zwarte speler na een succesvolle zet. Wit start altijd.
Geïmplementeerd als pure tekst. Stenen zijn niet grafisch weergegeven maar als tekst: "wit" of "zwart"

# Afhankelijkheden:
* game2dboard <br>
&nbsp;&nbsp;&nbsp;&nbsp;installeer als volgt:  <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        pip3 install game2dboard
* tkinter <br>
&nbsp;&nbsp;&nbsp;&nbsp; installeer als volgt: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        pip3 install tkinter

# to-do:
    1: implementeren van een dam halen
    2: spelbord mooier maken met kleurvlakken en plaatjes van damstenen
    3: tellers bijhouden van geslagen stukken


