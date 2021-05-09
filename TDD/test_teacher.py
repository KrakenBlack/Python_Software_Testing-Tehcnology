from teacher import Teacher

def test_create_teacher_with_optinal_args():
    # input
    name = 'james'
    years_exp  = 2
    master_degree = True
    topics = ['Python','java']
    # process
    teacher = Teacher(name, years_exp,master_degree=master_degree, topics = topics)

    # assert
    assert isinstance(teacher, Teacher)
    assert teacher.name == 'james'
    assert teacher.years_exp == 2
    assert teacher.has_master_degree is True
    assert teacher.topics == ['Python','java']
    assert teacher.amount_topics == 2

def test_teacher_instantianing_sucess():
    # input
    name = 'Yoko'
    years_exp = 5

    # process
    teacher = Teacher(name,years_exp)

    # assert
    assert isinstance(teacher,Teacher)
    assert teacher.name == 'Yoko'
    assert teacher.years_exp == 5

