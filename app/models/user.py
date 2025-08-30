import requests

def get_profil_info() :
    """
    Pre : (This function fecthes data from Leetcode)
    Post : Return profil_info (pfp, username, total question solved) (type : dict)
                  problem_info (easy, medium, hard and total solved) (type : dict)
                  stackInfo (url to the programming language icon and problem solved in %) (type : dict[dict])
                  the response.status_code (200 if we fecthed data, else it's another number)
           as a tuple.
    """
    username = "Younesdjzz"  # LeetCode username
    url = "https://leetscan.vercel.app/{}".format(username)
    response = requests.get(url)
        
    if response.status_code == 200 :  # It means we fetched data
        data = response.json()

        profil_info = {"pfp" : data['profile']['userAvatar'],
                       "username" : data['username'],
                       "totalSolved" : data['totalSolved']}
    
        problem_info = {"Easy" : {"difficulty" : "Easy",
                                  "solved" : data['easySolved'],
                                  "total" : data['totalEasy'],
                                  "div" : "easyStats",
                                  "id" : "easy-bar"},

                        "Medium" : {"difficulty" : "Medium",
                                    "solved" : data['mediumSolved'],
                                    "total" : data['totalMedium'],
                                    "div" : "mediumStats",
                                    "id" : "medium-bar"},

                        "Hard" : {"difficulty" : "Hard",
                                  "solved" : data['hardSolved'], 
                                  "total" : data['totalHard'],
                                  "div" : "hardStats",
                                  "id" : "hard-bar"}}
        
        stack_info = {"Python" : {"icon" : "static/stack/pythonIcon.png",
                                 "solved" : round((data['totalSolved'] - 8) / data['totalSolved'] * 100)},
                     "JavaScript" : {"icon" : "static/stack/javascriptIcon.jpg",
                                     "solved" : round((data['totalSolved'] - 62) / data['totalSolved'] * 100)},
                     "SQL" : {"icon" : "static/stack/sqlIcon.png",
                                     "solved" : round((data['totalSolved'] - 137) / data['totalSolved'] * 100)}}
    else:
        profil_info = None
        problem_info = None
        stack_info = None

    return profil_info, problem_info, stack_info, response.status_code