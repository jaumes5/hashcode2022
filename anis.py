import functools
import time
from functools import lru_cache

from frozendict import frozendict

from jaime import sort_collabs_skills


contributors = {}
projects_dict = {}
sorted_skills = {}


def solve(contributors_1, projects_dict_1):
    """
    projects : {"name": "Logging", "required_skills":  [{"name": "c++", "level": 2}], "days" : 3, "best_before_day" : 3, "score" : 100}
    contributors : [{"name" : "Bob", "skills" : [{"name": "c++", "level": 2}]}]
    """
    global contributors
    global projects_dict
    projects_dict = projects_dict_1
    contributors = contributors_1
    current_day = 0

    assignments = []
    current_projects = []
    done_projects = set()
    busy_collaborators = set()
    treshold_time = 0.01
    global sorted_skills
    sorted_skills = sort_collabs_skills(contributors)
    red_list = 1
    while True:
        start = time.time()
        if not any_project_profitable(projects_dict, current_day):
            break

        for (project, start_day, team) in current_projects:
            if is_project_done(project, start_day, current_day, team):
                busy_collaborators = busy_collaborators.difference(team)
                

        projects = sort_projects(projects_dict.values(), current_day)

        # optimisation for later
        # if is_project_unworthy(projects[0], current_day):
        #     break

        for project in projects[:min(len(projects) // red_list + 1, len(projects))]:
            if is_project_unworthy(project, current_day):
                del projects_dict[project["name"]]
                continue
            team = make_team(project["name"], tuple(busy_collaborators))
            if team: 
                assignments += [(project, team)]
                current_projects += [(project, current_day, team)]
                busy_collaborators.update(team)
                del projects_dict[project["name"]]
        
        current_day += 1
        if current_day % 5000 == 0:
            print(current_day, min(len(projects) // red_list + 1, len(projects)))
        final_time = time.time() - start
        if final_time > treshold_time:
            red_list = int(red_list * (final_time // treshold_time))
        # elif final_time * 100 < treshold_time and red_list >= 2:
        #     red_list = int(red_list / 2)
    make_team.cache_clear()
    return assignments


def sort_projects(projects, current_day):
    def get_project_sort_key(project):
        tmp = 0 if current_day < project["best_before"] else current_day - project["best_before"] + 1
        return (project["score"] - tmp) / project["num_days"]
    return sorted(projects, key=get_project_sort_key, reverse=True)

def is_project_doable(project, contributors, current_day,  busy_collaborators, current_projects):
    pass


@lru_cache
def make_team(project_name, busy_collaborators):
    project = projects_dict[project_name]
    skills = project['skills']
    cont = set(list(contributors.values())[0].keys()) - set(busy_collaborators)
    team = []
    if len(cont) >= len(skills):
        for skill, value in skills:
            if value > max(sorted_skills[skill], key=lambda a: a[1])[1]:
                return 0
            no_better = False
            for collab, _ in sorted_skills[skill]:
                if contributors[skill][collab] >= value and collab not in team and collab in cont:
                    team.append(collab)
                    break
                elif contributors[skill][collab] < value:
                    no_better = True
                    break
            else:
                return 0
            if no_better:
                return 0
            cont.remove(collab)
        return team
    return 0

def is_project_done(project, start_day, current_day, team):
    return current_day >= (start_day + project["num_days"])

def any_project_profitable(projects_dict, current_day):
    return any(is_project_worthy(p, current_day) for p in projects_dict.values()) 

def is_project_worthy(project, current_day):
    # 5 > (13 - 10)
    # 5 > (2 - 10)
    # print(f' {project["score"]} > ({current_day} - {project["best_before"]})')
    return project["score"] > (current_day - project["best_before"])

def is_project_unworthy(project, current_day):
    return project["score"] <= (current_day - project["best_before"])

def make_output_file(assignments, output_suffix):
    with open(f'output-{output_suffix}.txt', 'w') as f:
        f.write(f"{len(assignments)}\n")
        for a in assignments:
            f.write(f"{a[0]['name']}\n")
            f.write(f"{' '.join(a[1])}\n")
