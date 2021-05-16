from teacher import Teacher
import pytest


# Fixture will run the function and returns this value as variable, this allows us to change the value if needed,
# Fixtures can be called as variables
@pytest.fixture()
def valid_person_name():
    return 'james'

@pytest.fixture()
def invalid_person_name():
    # yield will return(without exiting function) and run the code after that
    yield ''
    print("Clear the environment")


class TestCreateDirector:

    # THis will skip, and not show just pass in terminal (otherwise you will see it as passed test, but without function)
    @pytest.mark.skip(reason="Still not implemented")
    def test_create_director_with_empty_position(self):
        pass

class TestCreateTeacher:
    def test_create_teacher_with_optinal_args(self,valid_person_name):
        # input
        name = 'james'
        years_exp  = 2
        master_degree = True
        topics = ['Python','java']
        # process
        teacher = Teacher(valid_person_name, years_exp,master_degree=master_degree, topics = topics)

        # assert
        assert isinstance(teacher, Teacher)
        assert teacher.name == 'james'
        assert teacher.years_exp == 2
        assert teacher.has_master_degree is True
        assert teacher.topics == ['Python','java']
        assert teacher.amount_topics == 2

    def test_teacher_instantianing_sucess(self,valid_person_name):
        # input
        years_exp = 5

        # process
        teacher = Teacher(valid_person_name,years_exp)

        # assert
        assert isinstance(teacher,Teacher)
        assert teacher.name == 'james'
        assert teacher.years_exp == 5

