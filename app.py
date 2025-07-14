from flask import Flask, render_template
import requests

app = Flask(__name__)
@app.route('/')
def index():
    username = "Younesdjzz"  # Your LeetCode username
    url = "https://leetscan.vercel.app/{}".format(username)

    response = requests.get(url)

    if response.status_code == 200 :
        data = response.json()

        profil_info = {"pfp" : data['profile']['userAvatar'],
                       "username" : data['username'],
                       "rank" : data['ranking'],
                       }
    
        problem_info = {"totalSolved" : data['totalSolved'], "totalQuestions" : data['totalQuestions'],
                        "easySolved" : data['easySolved'], "totalEasy" : data['totalEasy'],
                        "mediumSolved" : data['mediumSolved'], "totalMedium" : data['totalMedium'],
                        "hardSolved" : data['hardSolved'], "totalHard" : data['totalHard']
                        }
    else:
        profil_info = None
        problem_info = None

    return render_template('index.html', response_status=response.status_code, profil_info=profil_info, problem_info=problem_info)