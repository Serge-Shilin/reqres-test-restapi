import pytest


def idfn(val):
    return "params: {0}".format(str(val))


@pytest.fixture(params=[("morpheus","leader"), ("shmorpheus", "shleader")], ids=idfn)
def users(request):
    return request.param


@pytest.fixture(params=["1","2","3"], ids=idfn)
def pages(request):
    return request.param


@pytest.fixture(params=[1,2,3,4], ids=idfn)
def user_ids(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption("--testing-stand", action="store", default="TEST", help="stand option: DEV or TEST")


@pytest.fixture()
def cmdopt(request):
    return request.config.getoption("--testing-stand")


@pytest.fixture()
def host(cmdopt):
    if cmdopt == "DEV":
        return 'https://reqres.in'
    elif cmdopt == "TEST":
        return 'localhost'
