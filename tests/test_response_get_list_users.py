import allure
from allure.constants import AttachmentType
from requests_toolbelt.utils import dump

from core.tools import get_list_users, OK


class TestResponseGetListUsers:

    @allure.feature("Вывод списка пользователей")
    def test_response_get_list_users(self, host, pages):
        """
        Нужно сделать matcher чтобы была только одна проверка
        """
        with allure.step("Шлем запрос"):
            r = get_list_users(host, pages)
            allure.attach("request", dump.dump_all(r), AttachmentType.TEXT)
        with allure.step("Проверяем статус ответа"):
            assert (r.status_code == OK)
        with allure.step("Проверяем правильная ли страница отобразилась"):
            assert (r.json()['page'] == pages)
