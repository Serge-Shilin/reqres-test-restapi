import allure
from allure.constants import AttachmentType
from core.tools import post_create_user_request, CREATED
from requests_toolbelt.utils import dump


class TestResponsePostCreateUser:

    @allure.feature("Создание пользователя")
    def test_response_post_create_user(self, host, users):
        (name, job) = users
        """
        Нужно сделать matcher чтобы была только одна проверка
        """
        with allure.step("Шлем запрос"):
            r = post_create_user_request(host, name, job)
            allure.attach("request", dump.dump_all(r), AttachmentType.TEXT)
        with allure.step("Проверяем статус ответа"):
            assert (r.status_code == CREATED)
        with allure.step("Проверяем имя пользователя в ответе"):
            assert (r.json()['name'] == name)
        with allure.step("Проверяем род занятий в ответе"):
            assert (r.json()['job'] == job)
        with allure.step("Проверяем, что в ответе есть id нового пользователя"):
            assert (r.json()['id'] is not None)