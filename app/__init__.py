from flask import Flask, render_template
import time
from app.models.user import *

app = Flask(__name__)
CACHE = {}

@app.route('/')
def index():
    now = time.time()

    if all(k in CACHE for k in ("profil_info", "problem_info", "timestamp")) and now - CACHE["timestamp"] <= 86400 : # update of CACHE after 24h
        profil_info = CACHE["profil_info"]
        problem_info = CACHE["problem_info"]
        stackInfo = CACHE["stackInfo"]
        response_status = 200

    else :
        profil_info, problem_info, stackInfo, response_status = get_profil_info()
        CACHE["profil_info"] = profil_info
        CACHE["problem_info"] = problem_info
        CACHE["stackInfo"] = stackInfo
        CACHE["timestamp"] = now

    return render_template('index.html',
                            response_status = response_status,
                            profil_info = profil_info,
                            problem_info = problem_info,
                            stackInfo = stackInfo)