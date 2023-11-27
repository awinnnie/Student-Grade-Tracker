def cleanupData(data):
    cleanedData = [];
    uniqueStudents = [];
    for student in data:
        if (student.get('id') in uniqueStudents):
            continue;
        else:
            if (student.get('name') != None and student.get('surname') != None):
                uniqueStudents.append(student.get('id'));
                cleanedData.append(student);
    return cleanedData;

