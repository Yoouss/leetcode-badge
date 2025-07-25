from flask import Flask, render_template
import requests, time

app = Flask(__name__)
CACHE = {}

@app.route('/')
def index():
    def get_profil_info(data) :
        """
        Pre : This function takes data, a json file, as parameter
        Post : Return profil_info (pfp, username, rank)
                      problem_info (easy, medium, hard and total solved)
               as a tuple.
        """
        profil_info = {"pfp" : data['profile']['userAvatar'],
                        "username" : data['username'],
                        "rank" : data['ranking'],}
    
        problem_info = {"totalSolved" : data['totalSolved'], "totalQuestions" : data['totalQuestions'],
                        "easySolved" : data['easySolved'], "totalEasy" : data['totalEasy'],
                        "mediumSolved" : data['mediumSolved'], "totalMedium" : data['totalMedium'],
                        "hardSolved" : data['hardSolved'], "totalHard" : data['totalHard']}

        return profil_info, problem_info
    
    now = time.time()

    if all(k in CACHE for k in ("profil_info", "problem_info", "timestamp")) and now - CACHE["timestamp"] <= 86400 : # update of CACHE after 24h
        profil_info = CACHE["profil_info"]
        problem_info = CACHE["problem_info"]
        response_status_code = 200

    else :
        username = "Younesdjzz"  # LeetCode username
        url = "https://leetscan.vercel.app/{}".format(username)
        response = requests.get(url)
        response_status_code = response.status_code # 200 if we fetched data
        
        if response.status_code == 200 :
            data = response.json()
            profil_info, problem_info = get_profil_info(data)
            CACHE["profil_info"] = profil_info
            CACHE["problem_info"] = problem_info
            CACHE["timestamp"] = now
    
        else:
            profil_info = None
            problem_info = None

    return render_template('index.html', response_status=response_status_code, profil_info=profil_info, problem_info=problem_info)