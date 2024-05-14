from tabulate import tabulate as tab
import time

############################## VARIABLES ######################################
head = ["1. Equipment", "2. Pistols", "3. SMGs", "4. Rifles", "5. Utility"]

Money = 10000

Kevlar = 650
Helmet = 350
Zeus_x27 = 200
Defuse_Kit = 400

USP_S = 200
Dual_Berettas = 300
P250 = 300
Five_Seven = 500
Desert_Eagle = 700

Nova = 1050
MP9 = 1250
MP7 = 1500
XM1014 = 2000
P90 = 2350

SSG_08 = 1700
FAMAS = 2050
M4A1_S = 2900
M4A4 = 3100
AWP = 4750

Flash = 200
Smoke = 300
HE = 300
Molotov = 400
Decoy = 50

weapon_list = {"kevlar": Kevlar, "helmet": Helmet, "zeus": Zeus_x27, "defuse": Defuse_Kit,  "usp": USP_S, "dualies": Dual_Berettas, "p250": P250, "five": Five_Seven, "deagle": Desert_Eagle,  "nova": Nova, "mp9": MP9, "mp7": MP7, "xm1014": XM1014, "p90": P90,  "ssg": SSG_08, "famas": FAMAS, "m4a1": M4A1_S, "m4a4": M4A4, "awp": AWP,  "flash": Flash, "smoke": Smoke, "he": HE, "molotov": Molotov, "decoy": Decoy}

# Definere underkategoriene og dataen i en tabell
mydata = [

    ["Kevlar Vest \n" + str(Kevlar) + "$", "USP-S \n" + str(USP_S) + "$", "Nova \n" + str(Nova) + "$", "SSG 08 \n" + str(SSG_08) + "$", "Flashbang \n" + str(Flash) + "$"],
    ["Kevlar Helmet \n" + str(Helmet) + "$", "Dual Berettas \n" + str(Dual_Berettas) + "$", "MP9 \n" + str(MP9) + "$", "FAMAS \n" + str(FAMAS) + "$", "Smoke Grenade \n" + str(Smoke) + "$"],
    ["Zeus x27 \n" + str(Zeus_x27) + "$", "P250 \n" + str(P250) + "$", "MP7 \n" + str(MP7) + "$", "M4A1-S \n" + str(M4A1_S) + "$", "Heavy Explosive Grenade \n" + str(HE) + "$"],
    ["Defuse Kit \n" + str(Defuse_Kit) + "$", "Five-Seven \n" + str(Five_Seven) + "$", "XM1014 \n" + str(XM1014) + "$", "M4A4 \n" + str(M4A4) + "$", "Incendiary Grenade \n" + str(Molotov) + "$"],
    ["", "Desert Eagle \n" + str(Desert_Eagle) + "$", "P90 \n" + str(P90) + "$", "AWP \n" + str(AWP) + "$", "Decoy Grenade \n" + str(Decoy) + "$"]
    
]

print(tab(mydata, headers=head, tablefmt="grid"))
time.sleep(2)

while True:
    buy = input("\nWhat weapon would you like to buy?: \n")

    if buy in weapon_list:
        price = weapon_list.get(buy)

        if Money >= price:
            Money -= price
            print(f"\nYou bought {buy}. Remaining money: {Money}")

            available_count = Money // price
            print(f"You can buy this weapon {available_count} more times.")
        else:
            print("Insufficient funds!")

        time.sleep(2)
        print("\nPress 'q' to quit or press Enter to continue shopping.")
        if input() == 'q':
            print("Goodbye!")
            break