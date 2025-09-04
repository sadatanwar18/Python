class InvalidSnacksError(Exception):
    pass

def bill(snack, packs):
    menu = {"lays": 20, "juice": 50}
    try:
        if snack not in menu:
            raise InvalidSnacksError("snack is not available")
        if not isinstance(packs, int):
            raise TypeError("packs should be in integer")
        
        total = menu[snack] * packs

        print(f"your bill for {packs} pack of {snack} : ruupees {total}")
    
    except Exception as e :
        print("Error: ", e)
    finally: 
        print("Thanks")

bill("chips", 2)
bill("lays", "teen")
bill("juice", 3)