import requests

def details(choice , charinfo):
    if(choice == 1):
        description = (charinfo[0]['description']).split(",")
        print(f"\n\n\nName : {charinfo[0]['name']}\nDescription :  ")
        for i in description:
            print("• ",i)
    if(choice == 2):
        print(f"              Powers\n")
        powers = charinfo[0]['powers']
        a = 1
        for i in powers:
            print(a,": " , i)
    if(choice == 3):
        pass
            
        

def main():
    ask = input("Enter the Marvel character you want to look for : ")
    url = "https://marvel-heroic-api-unlock-the-mcu-legendary-characters.p.rapidapi.com/name"

    querystring = {"q": ask}

    headers = {
        "X-RapidAPI-Key": "19e5dcc0f8msh806dd6c69c770e6p1255f7jsndd58c2594a47",
        "X-RapidAPI-Host": "marvel-heroic-api-unlock-the-mcu-legendary-characters.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    character_detail  = response.json()
    print(character_detail)

    if(response.status_code == 200):
        
        while True:
            detail = int(input(f"Which of the following you want to know about {ask} :\n1.PERSONAL PROFILE\n2.POWERS\n3.MOVIES\n4.FAMOUS QUOTES BY {ask}\n5.ALSO KNOW AS\n6.TO SEARCH FOR OTHER CHAR\n7.EXIT"))
            if(detail >= 7):
                return
            if (details(detail,character_detail) == None):
                main()
            else:
                pass

            

    else:
        print("Error Could not find the character you were looking for :(\n\n\n")
        main()




if(__name__ == "__main__"):
    main()