import random
import matplotlib.pyplot as plt
import numpy as np

worpen_max = 100000

def worp_met_twee_dobbelstenen():
    dobbelsteen_a = random.randint(1, 6)
    dobbelsteen_b = random.randint(1, 6)
    return dobbelsteen_a + dobbelsteen_b

def simuleer_potje_monopoly(startgeld_speler_a, startgeld_speler_b):
    bord_waardes = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180, 0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300, 0, 320, 200, 0, 350, 0, 400]
    
    # Initialize both players
    posities = [0, 0]  # [player A position, player B position]
    geld = [startgeld_speler_a, startgeld_speler_b]
    bezittingen = [[0]*40, [0]*40]  # [player A properties, player B properties]
    
    total_properties_bought = 0
    
    for beurt_nummer in range(worpen_max):
        # Players alternate turns
        for speler in [0, 1]:  # 0 = player A, 1 = player B
            if total_properties_bought >= 28:  
                break
                
            getalworp = worp_met_twee_dobbelstenen()
            oude_positie = posities[speler]
            
            
            if oude_positie + getalworp >= 40:
                geld[speler] += 200
            
            
            nieuwe_positie = (oude_positie + getalworp) % 40
            posities[speler] = nieuwe_positie
            
            
            property_price = bord_waardes[nieuwe_positie]
            if property_price > 0:
                # Check
                if bezittingen[0][nieuwe_positie] == 0 and bezittingen[1][nieuwe_positie] == 0:
                    if geld[speler] >= property_price:
                        bezittingen[speler][nieuwe_positie] = 1
                        geld[speler] -= property_price
                        total_properties_bought += 1
            
            
            if total_properties_bought >= 28:
                break
    
    # A - B
    straten_a = sum(bezittingen[0])
    straten_b = sum(bezittingen[1])
    verschil = straten_a - straten_b
    
    return verschil

def simuleer_groot_aantal_potjes_monopoly(aantal_potjes, startgeld_speler_a, startgeld_speler_b):
    totaal_verschil = 0
    verschil_lijst = []
    
    for i in range(aantal_potjes):
        verschil = simuleer_potje_monopoly(startgeld_speler_a, startgeld_speler_b)
        totaal_verschil += verschil
        verschil_lijst.append(verschil)
    
    gemiddeld_verschil = totaal_verschil / aantal_potjes
    return gemiddeld_verschil, verschil_lijst

def evenwicht():
    startgeld_a = 1500
    extra_geld_options = [0, 50, 100, 150, 200]
    resultaten = []
    
    for extra_geld in extra_geld_options:
        startgeld_b = 1500 + extra_geld
        gemiddeld_verschil, _ = simuleer_groot_aantal_potjes_monopoly(10000, startgeld_a, startgeld_b)
        resultaten.append((extra_geld, gemiddeld_verschil))
        print(f"Startgeld [1500,{startgeld_b}]: speler A gemiddeld {gemiddeld_verschil:.2f} meer straten (speler B heeft {extra_geld} euro extra)")
    
    
    for i in range(len(resultaten) - 1):
        current_extra, current_diff = resultaten[i]
        next_extra, next_diff = resultaten[i + 1]
        
        
        if current_diff > 0 and next_diff <= 0:
            equilibrium_extra = current_extra + (current_diff / (current_diff - next_diff)) * 50
            return equilibrium_extra
    
    
    return resultaten[-1][0]

# 3a
print("Deelopdracht 3a: Voordeel van speler A")
gemiddeld_verschil, verschil_lijst = simuleer_groot_aantal_potjes_monopoly(10000, 1500, 1500)
print(f"Monopoly simulator: twee spelers, 1500 euro startgeld, 10000 potjes")
print(f"Gemiddeld heeft speler A {gemiddeld_verschil:.2f} meer straten in bezit als alle straten verdeeld zijn")
# 3b
print("\nDeelopdracht 3b: Evenwicht zoeken")
evenwicht_extra = evenwicht()
print(f"\nMonopoly simulator: 2 spelers")
print(f"Als we speler B {evenwicht_extra:.0f} euro meer startgeld meegeven hebben beide spelers gemiddeld evenveel straten in bezit")

# histogogoa
plt.hist(verschil_lijst, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title(f"Verschil in straten tussen speler A en B (gemiddeld: {gemiddeld_verschil:.2f})")
plt.xlabel("Aantal meer straten van speler A t.o.v. speler B")
plt.ylabel("Aantal simulaties")
plt.axvline(gemiddeld_verschil, color='red', linestyle='--', label='Gemiddeld verschil')
plt.legend()
plt.show()