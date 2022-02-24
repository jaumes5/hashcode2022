from utils import read_input


def input_parser(file_path):
    files = read_input(f"files/{file_path}")[0].split("\n")
    number_of_people, number_of_projects = (int(i) for i in files.pop(0).split(" "))
    skills_dict = {}
    people = set()
    for _ in range(number_of_people):
        person, skills = files.pop(0).split(" ")
        people.add(person)
        for _ in range(int(skills)):
            skill, level = files.pop(0).split(" ")
            if skill in skills_dict:
                skills_dict[skill][person] = int(level)
            if skill not in skills_dict:
                skills_dict[skill] = {person: int(level)}
    for person in people:
        for skill_name in skills_dict:
            if person not in skills_dict[skill_name]:
                skills_dict[skill_name][person] = 0
    project_dict = {}
    for _ in range(number_of_projects):
        project, num_days, score, best_before, number_roles = (
            i if pos == 0 else int(i) for pos, i in enumerate(files.pop(0).split(" "))
        )
        for _ in range(int(number_roles)):
            skill, level = files.pop(0).split(" ")
            if project in project_dict:
                project_dict[project]["skills"].append((skill, int(level)))
            if project not in project_dict:
                project_dict[project] = {
                    "skills": [(skill, int(level))],
                    "num_days": num_days,
                    "score": score,
                    "best_before": best_before,
                    "number_roles": number_roles,
                    "name": project,
                }
    return skills_dict, project_dict


input_parser("a_an_example.in.txt")
