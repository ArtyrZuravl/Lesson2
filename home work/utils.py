import json


def load_candidates(path):
    with open(path, 'r', encoding="UTF-8") as file:
        users = json.load(file)
        return users
def get_candidate_id(candidate_id):
    users = load_candidates('candidates.json')
    for candidate in users:
        if candidate['id'] == candidate_id:
            return candidate
    return 'нет'
def get_candidates_name(candidate_name):
    users = load_candidates('candidates.json')
    for candidate in users:
        if candidate_name.lower() in candidate['name'].lower():
            return candidate

def get_candidates_skills(candidate_skill):
    users = load_candidates('candidates.json')
    users_skill = []
    for candidate in users:
        skill = candidate["skills"]
        skills = skill.split(", ")
        if candidate_skill in skills:
            users_skill.append(candidate)
    return users_skill





