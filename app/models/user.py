import requests

def get_profil_info() :
    """
    Pre : (This function fecthes data from Leetcode)
    Post : Return profil_info (pfp, username, rank) (type : dict)
                  problem_info (easy, medium, hard and total solved) (type : dict)
                  stackInfo (url to the programming language icon and problem solved) (type : dict[dict])
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
                    "rank" : data['ranking'],}
    
        problem_info = {"totalSolved" : data['totalSolved'], "totalQuestions" : data['totalQuestions'],
                        "easySolved" : data['easySolved'], "totalEasy" : data['totalEasy'],
                        "mediumSolved" : data['mediumSolved'], "totalMedium" : data['totalMedium'],
                        "hardSolved" : data['hardSolved'], "totalHard" : data['totalHard']}
        
        stackInfo = {"Python" : {"icon" : "static/stack/pythonIcon.jpg",
                                 "solved" : data['totalSolved'] - 5},
                     "JavaScript" : {"icon" : "static/stack/javascriptIcon.jpg",
                                     "solved" : data['totalSolved'] - 60}}
    else:
        profil_info = None
        problem_info = None
        stackInfo = None

    return profil_info, problem_info, stackInfo, response.status_code