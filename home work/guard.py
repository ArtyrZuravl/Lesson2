from flask import Flask, request, render_template
import json
from utils import load_candidates, get_candidate_id, get_candidates_name, get_candidates_skills

app = Flask(__name__)
users = load_candidates("candidates.json")

@app.route("/")
def hello():

     return render_template("crom.html", candidates=users)


@app.route('/candidate/<int:id>')
def card(id):
     user_card = get_candidate_id(id)
     return  render_template("card.html", candidate=user_card)

@app.route('/search/<string:name>')
def users_name(name):
     users_name = get_candidates_name(name)
     return render_template('filter_name.html', candidate=users_name)

@app.route('/skills/<string:skill>')
def users_skill(skill):
     users_skills = get_candidates_skills(skill)
     return render_template("skills.html", count=len(users_skills), candidates=users_skills, skill=skill )

app.run(debug=True)
