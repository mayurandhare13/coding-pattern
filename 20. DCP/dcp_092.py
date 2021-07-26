def coursesToTake(coursesToprereqs: dict):
    # Copy list values into a set for faster removal.
    # Course -> Prerequisites
    coursesToprereqs = { c: set(p) for c, p in coursesToprereqs.items() }

    todo = [c for c, p in coursesToprereqs.items() if not p]

    # Prerequisite -> Courses
    prereqsToCourses = {}
    for course, prereqs in coursesToprereqs.items():
        for prereq in prereqs:
            if prereq not in prereqsToCourses:
                prereqsToCourses[prereq] = []
            
            prereqsToCourses[prereq].append(course)
    
    result = []

    while todo:
        prereq = todo.pop()
        result.append(prereq)

        for c in prereqsToCourses.get(prereq, []):
            coursesToprereqs[c].remove(prereq)
            if not coursesToprereqs[c]:
                todo.append(c)
    

    # circulat dependency
    if len(result) != len(coursesToprereqs):
        return None
    
    return result


if __name__ == '__main__':
    assert coursesToTake (
        {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
    ) == ['CSC100', 'CSC200', 'CSC300']