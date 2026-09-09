aantal_rijen = 3
aantal_kolommen = 2
test =  [
            [c for c in range(aantal_kolommen)]         
            for r in range(aantal_rijen)
        ]   

print(test)