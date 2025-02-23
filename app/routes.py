from app import app
from flask import render_template, request, redirect, url_for, session

app.secret_key= "hello"

@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.form

    if request.method=='POST':
        
        name = request.form.get('name')
        phone = request.form.get('phone')
        weather_updates = request.form.get('weatherUpdates') == "True"
        future_games = request.form.get('futureGames') == "True"

        
        session["user"] = {
            "name": name,
            "phone": phone,
            "weather_updates": weather_updates,
            "future_games": future_games,
        }
        print("User registered:", session["user"])
        return redirect(url_for("dashboard"))

    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    user = session.get("user")
    print("User session data:", user)
    
    if not user:
        return redirect(url_for("index"))
    #place holder list to track users input for the picks until database is done
    user_picks = []

    return render_template('dashboard.html', user=user, picks=user_picks)


@app.route('/submit-picks', methods=["POST"])
def submit_picks():
    user = session.get("user") #grab the current users session

    if not user:
        return redirect(url_for("index"))
    
    picks = {
        "pick1": request.form.get("pick1", "False"),
        "pick2": request.form.get("pick2", "False"),
        "pick3": request.form.get("pick3", "False"),
        "winner": request.form.get("winner", "Home"),
    }

#True is over false is under
    correct_answers = {
        "pick1": "True",
        "pick2": "False",
        "pick3": "True",
        "winner": "Home"
    }
    

#check against the correct answer
    points = 0
    results = {}
    for pick, user_choice in picks.items():
        if user_choice is not None:
            is_correct = user_choice == correct_answers[pick]
            results[pick] = {
                "choice": user_choice,
                "correct": is_correct
                }
            if is_correct:
                points +=1


#temporary placeholder for the points and results until we get the database in
    session["results"] = results
    session["points"] = points

    return redirect(url_for("results"))

@app.route('/results')
def results():
    user = session.get("user") #get current user

    if not user:
        return redirect(url_for("index"))
    
    results = session.get("results", {}) #default to empty if no results
    points = session.get("points", 0) #default 0 points

    return render_template("results.html", user=user, results=results, points=points)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
