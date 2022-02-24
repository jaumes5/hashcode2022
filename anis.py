def solve(contributors, projects):
    """
    projects : {"name": "Logging", "required_skills":  [{"name": "c++", "level": 2}], "days" : 3, "best_before_day" : 3, "score" : 100}
    contributors : [{"name" : "Bob", "skills" : [{"name": "c++", "level": 2}]}]
    """
    current_day = 0

    assignments = []
    current_projects = []
    done_projects = set()
    busy_collaborators = set()
    while True:
        

        for (project, start_day, team) in current_projects:
            if is_project_done(project, start_day, current_day, team):
                done_projects.add(project)
                busy_collaborators = busy_collaborators.difference([t["name"] for t in team])

        projects = sort_projects(projects, done_projects)

        for (porject_name, project) in projects.items():
            if is_project_doable(project, contributors, current_day, busy_collaborators, current_projects):
                team = make_team(project, contributors, busy_collaborators)
                assignments += (project, team)
                current_projects.add((project, team))
                busy_collaborators.update([t["name"] for t in team])

        current_day += 1    
        
    return assignments


def sort_projects(projects):
    def get_project_sort_key(project):
        return (project["best_before_day"], - project["score"] / project["days"] / len(project["required_skills"]))
    return sorted(projects, key=get_project_sort_key)

def is_project_doable(project, contributors, current_day,  busy_collaborators, current_projects):
    pass


def make_team(project, contributors, busy_collaborators):
    pass

def is_project_done(project, start_day, current_day, team):
    pass