from api_commons.common import ApiResponse
from django.http import HttpRequest
from jba_api.common import JbAccessController, dto_inject
from jba_api.person.dto import PersonInDto, PersonOutDto
from jba_core.service import PersonService
from jba_api import permissions


class PersonController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest):
        personnel = PersonService.get_all()
        person_dtos = list([PersonOutDto.from_person(p) for p in personnel])
        return ApiResponse.success(person_dtos)

    @dto_inject(PersonInDto)
    def post(self, request: HttpRequest, dto: PersonInDto):
        person = PersonService.create(dto.name)
        return ApiResponse.success(PersonOutDto.from_person(person))


class PersonRUDController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest, id: int):
        id = self.parse_int_pk(id)
        person = PersonService.get(id)
        return ApiResponse.success(PersonOutDto.from_person(person))

    @dto_inject(PersonInDto)
    def put(self, request: HttpRequest, id: int, dto: PersonInDto):
        id = self.parse_int_pk(id)
        person = PersonService.update(id, dto.name)
        return ApiResponse.success(PersonOutDto.from_person(person))

    def delete(self, request: HttpRequest, id: int):
        id = self.parse_int_pk(id)
        PersonService.delete(id)
        return ApiResponse.success()