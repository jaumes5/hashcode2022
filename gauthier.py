def make_team(project, contributors, busy_collaborators):
    skills = project['skills']
    cont=set(contributors.values()[0].keys())-busy_collaborators
    team = []
    if len(cont) >= len(skill):
        for skill, value in skills:
            for collab in cont:
                if contributors[skill][collab]>= value:
                    team.append(collab)
                    break
            else:
                return 0
        return team
    return 0