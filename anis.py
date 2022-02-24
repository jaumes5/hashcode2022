def solve(contributors, projects_dict):
    """
    projects : {"name": "Logging", "required_skills":  [{"name": "c++", "level": 2}], "days" : 3, "best_before_day" : 3, "score" : 100}
    contributors : [{"name" : "Bob", "skills" : [{"name": "c++", "level": 2}]}]
    """
    print(contributors)
    current_day = 0

    assignments = []
    current_projects = []
    done_projects = set()
    busy_collaborators = set()
    while True:
        if not any_project_profitable(projects_dict, current_day):
            break

        for (project, start_day, team) in current_projects:
            if is_project_done(project, start_day, current_day, team):
                busy_collaborators = busy_collaborators.difference(team)
                

        projects = sort_projects(projects_dict.values())

        # optimisation for later
        # if is_project_unworthy(projects[0], current_day):
        #     break

        for project in projects:
            team = make_team(project, contributors, busy_collaborators)
            if team: 
                assignments += [(project, team)]
                current_projects += [(project, current_day, team)]
                busy_collaborators.update(team)
                del projects_dict[project["name"]]

        
        current_day += 1    
        
    return assignments


def sort_projects(projects):
    def get_project_sort_key(project):
        return (project["best_before"], - project["score"] / project["num_days"] / len(project["skills"]))
    return sorted(projects, key=get_project_sort_key)

def is_project_doable(project, contributors, current_day,  busy_collaborators, current_projects):
    pass


def make_team(project, contributors, busy_collaborators):
    skills = project['skills']
    cont = set(list(contributors.values())[0].keys()) - busy_collaborators
    team = []
    if len(cont) >= len(skills):
        for skill, value in skills:
            for collab in cont:
                if contributors[skill][collab] > value and collab not in team:
                    team.append(collab)
                if contributors[skill][collab] == value and collab not in team:
                    team.append(collab)
                    contributors[skill][collab] += 1
                    break
            else:
                return 0
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


def make_output_file(assignments, output_suffix):
    with open(f'output-{output_suffix}.txt', 'w') as f:
        f.write(f"{len(assignments)}\n")
        for a in assignments:
            f.write(f"{a[0]['name']}\n")
            f.write(f"{' '.join(a[1])}\n")
