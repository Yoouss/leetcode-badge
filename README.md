# ⭐ My First Mini Project: **A Custom LeetCode Badge**

## 🎯 Objective
The goal is to display my badge on my personal **GitHub profile README**

## 🔍 Overview
This mini-project is built with **Flask**, a **Python** web framework, to fetch data from **LeetCode** using an **API** **every 24h**
- Hosted on [https://leetcode-badge.onrender.com/](https://leetcode-badge.onrender.com) (HTML/CSS)
- Hosted on the **repository** : app/static/badge.png (PNG image)

⚠️ The website is hosted on **Render** so it may be in a sleeping mode. Try again few minutes later
  
[![My LeetCode badge](https://raw.githubusercontent.com/Younesdjzz/leetcode-badge/main/app/static/badge.png)](https://leetcode.com/u/Younesdjzz/)

## 💡 The meaning behind this project
I wanted to **show my Leetcode stats on my GitHub profile**, but I only found a few models online and the **designs weren't optimal**... <br>
So I decided to **create my own custom-designed badge** after asking a few questions to **ChatGPT** to plan how I would make it 🤔 

It helped me **practice my HTML/CSS skills** and gave me the opportunity to **start my first personal project ever** ! 

## 🛠️ How did I Built It ?
- I built my badge **from scratch**, using **AI** as a tool to support my **learning** and strengthen my **software development skills** without losing control over it
- First, I designed it using **HTML/CSS**, then I wrote a Python **screenshot script** using **AI assistance**

## ❔How to use Flask ?
- First, **clone** the **repository** : <br>
git clone https://github.com/Younesdjzz/leetcode-badge.git <br>
cd leetcode-badge <br><br>
- Then, **install** the **requirement.txt** in an **virtual environment** : <br>
python -m venv venv <br>
source venv/bin/activate <br>
pip install -r requirements.txt <br><br>
- Finally, to **lunch Flask**, use : <br>
flask --app app --debug run
