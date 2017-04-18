import allure
from allure.constants import AttachmentType
from requests_toolbelt.utils import dump

from core.tools import get_user, OK


class TestResponseGetSingleUser:

    @allure.feature("Вывод пользователей")
    def test_response_get_single_user(self, host, user_ids):
        with allure.step("Шлем запрос"):
            r = get_user(host, user_ids)
            allure.attach(dump.dump_all(r), AttachmentType.TEXT)
        """
        написать matcher для одной проверки
        """
        with allure.step("Проверяем статус ответа"):
            assert (r.status_code == OK)
        with allure.step("Проверка id пользователя в ответе"):
            id_request = r.json()["data"]["id"]
            assert (id_request == user_ids)
