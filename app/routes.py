from app import app
from flask import render_template, request, redirect, url_for, session

app.secret_key= "hello"

@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.form

    # Process 'Contact Information' HTML Form
    if request.method=='POST':
        
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        
        # IMPLEMENT WEATHER NOTIFCATION
        weather_updates = request.form.get('weatherUpdates') == "True"
        future_games = request.form.get('futureGames') == "True"
        
        # SQL: Insert User into Database
         
        session["user"] = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "weather_updates": weather_updates,
            "future_games": future_games,
        }
        print("User registered:", session["user"])
        return redirect(url_for("dashboard"))

    return render_template('index.html')

# @app.route('/dashboard')
# def dashboard():
#     user = session.get("user")
#     print("User session data:", user)
    
#     if not user:
#         return redirect(url_for("index"))
#     #place holder list to track users input for the picks until database is done
#     user_picks = []

#     return render_template('dashboard.html', user=user, picks=user_picks)


@app.route('/dashboard', methods=["GET","POST"])
def dashboard():
    user = session.get("user") #grab the current users session

    if not user:
        return redirect(url_for("index"))
    user_picks = []
    
    if request.method == 'POST':

        picks = {
            "pick1": request.form.get("pick1",True),
            "pick2": request.form.get("pick2",False),
            "pick3": request.form.get("pick3",False),
        }

    #True is over false is under
        correct_answers = {
            "pick1": True,
            "pick2": False,
            "pick3": True,
        }
        

    #check against the correct answer
        points = 0
        results = []
        userChoices = []
        for pick, user_choice in picks.items():
            if user_choice is not None:
                is_correct = user_choice == correct_answers[pick]
                results.append(is_correct)
                userChoices.append(user_choice)
                if is_correct:
                    points +=1


    #temporary placeholder for the points and results until we get the database in
        session["results"] = results
        session["userChoices"] = userChoices
        session["points"] = points
        print(results)
        print(userChoices)
        return render_template('results.html', results=results, userChoices=userChoices)
    return render_template('dashboard.html', user=user, picks=user_picks)

@app.route('/results')
def results():
    user = session.get("user") #get current user

    if not user:
        return redirect(url_for("index"))
    
    results = session.get("results", []) #default to empty if no results
    userChoices = session.get("userChoices", [])
    points = session.get("points", 0) #default 0 points
    print(results)
    print(userChoices)
    print(points)
    return render_template("results.html", user=user, results=results, points=points, userChoices = userChoices)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
