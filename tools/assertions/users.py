import allure

from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal
from tools.logger import get_logger

logger = get_logger("USERS_ASSERTIONS")


@allure.step("Check create user response")
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    assert_equal(response.user.email,request.email, 'email')
    assert_equal(response.user.last_name,request.last_name, 'last_name')
    assert_equal(response.user.first_name,request.first_name, 'first_name')
    assert_equal(response.user.middle_name,request.middle_name, 'middle_name')

    logger.info("Check create user response")

@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет корректность данных пользователя.

    :param actual: Объект пользователя, полученный из ответа API.
    :param expected: Ожидаемый объект пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check user")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")

@allure.step("Check get user response")
def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Проверяет, что данные созданного юзера соответствуют данным полученного юзера

    :param get_user_response: Полученные данные юзера
    :param create_user_response: Данные ответа на создание пользователя
    :return:
    """
    logger.info("Check get user response")
    assert_user(get_user_response.user, create_user_response.user)
