from edu_group_test import test_edu_group
from edu_program_test import test_edu_program
from edu_suply_by_program import test_edu_suply

try:
    test_edu_group()
except:
    print("test_edu_group falled")

try:
    test_edu_program()
except:
    print("test_edu_program falled")

try:
    test_edu_suply()
except:
    print("test_edu_suply falled")