# from flask import Blueprint
# from core import db
# from core.apis import decorators
# from core.apis.responses import APIResponse
# from core.models.assignments import Assignment
# from core.models.teachers import Teacher

# from .schema import TeacherSchema
# principal_assignments_resources = Blueprint("principal_assignments_resources",__name__)

# @principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
# @decorators.authenticate_principal
# def list_assignments(p):
#     """Returns list of all the teachers"""
#     teacher_list = Teacher.get_all_teachers()
#     print(teacher_list)
#     teacher_list_dump = TeacherSchema().dump(teacher_list, many=True)
#     return APIResponse.respond(data=teacher_list_dump)