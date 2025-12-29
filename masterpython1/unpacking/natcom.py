def wallet(n):
    if n < 0:
        return None
    return n

def plan_internet(montant):
    if montant >= 540:
        return f"Plan Internet 540 G activé. Solde restant: {montant - 540} G"
    elif montant >= 126:
        return f"Plan Internet 126 G activé. Solde restant: {montant - 126} G"
    elif montant >= 54:
        return f"Plan Internet 54 G activé. Solde restant: {montant - 54} G"
    else:
        return "Fonds insuffisants pour un plan Internet"
    
def plan_sms(montant):
    if montant >= 90:
        return f"Plan SMS 200 activé. Solde restant: {montant - 90} G"
    elif montant >= 60:
        return f"Plan SMS 150 activé. Solde restant: {montant - 60} G"
    elif montant >= 30:
        return f"Plan SMS 60 activé. Solde restant: {montant - 30} G"
    else:
        return "Fonds insuffisants pour un plan SMS"
    

def plan_apel(montant):
    if montant >= 90:
        return f"Plan Appel 200 minutes activé. Solde restant: {montant - 90} G"
    elif montant >= 60:
        return f"Plan Appel 150 minutes activé. Solde restant: {montant - 60} G"
    elif montant >= 30:
        return f"Plan Appel 100 minutes activé. Solde restant: {montant - 30} G"
    else:
        return "Fonds insuffisants pour un plan Appel"
    

def main():
    print("==== PLAN NATCOM ====")

    while True:
        print("\n1- Plan SMS")
        print("2- Plan Internet")
        print("3- Plan Appel")
        print("4- Quit")

        try:
            input_wallet = int(input("Entrer votre quantité d'argent: "))
            your_wallet = wallet(input_wallet)
            if your_wallet is None:
                print("Le montant doit être positif")
                continue
        except ValueError:
            print("Erreur: entre un nombre")
            continue

        try:
            main_plan = int(input("Choisissez un plan: "))
        except ValueError:
            print("Erreur: entre un nombre")
            continue

        if main_plan == 4:
            print("Merci d'avoir utilisé NATCASH")
            break

        if main_plan == 1:
            print(plan_sms(your_wallet))
        elif main_plan == 2:
            print(plan_internet(your_wallet))
        elif main_plan == 3:
            print(plan_apel(your_wallet))
        else:
            print("Choix invalide")
            continue

if __name__ == "__main__":
    main()        



