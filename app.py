import requests

username = "Younesdjzz"  # Your LeetCode username
url = "https://leetscan.vercel.app/{}".format(username)

response = requests.get(url)

if response.status_code == 200 :
    data = response.json()
    
    print("Profil LeetCode :")
    print(f"- Photo de profil        : {data['profile']['userAvatar']}")
    print(f"- Pseudo                 : {data['username']}")
    print(f"- Rang (rank tier)       : {data['ranking']}")
    print(f"- Total résolus          : {data['totalSolved']} / {data['totalQuestions']}")
    print()
    
    print("Détail par difficulté :")
    print(f"  • Easy    : {data['easySolved']} / {data['totalEasy']}")
    print(f"  • Medium  : {data['mediumSolved']} / {data['totalMedium']}")
    print(f"  • Hard    : {data['hardSolved']} / {data['totalHard']}")
    
else:
    print("Erreur", response.status_code, ": Echec de la récupération des données :(")