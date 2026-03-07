def skill_set(jd):

    try:
        fr = open("13. ErrorHandling\\skill_set.txt")
    

        skills = [line.strip() for line in fr if line.strip()]

    except Exception as e:
        print(e)
        return ""
    """
    if line.strip()
    -> Only keep the line if it has text.
    """
    # Read every line in the file, remove spaces/newlines, ignore empty lines, and store the remaining text in a list called skills.

    result = " "

    for skill in skills:

        if skill in jd:

            result += skill + " "

    return result

print(skill_set("Python SQL Project Planning, Time Management is a programming language"))

