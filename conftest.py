import pytest


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import mobile_tests.assist.selene.patch_selector_strategy  # noqa
    import mobile_tests.assist.selene.patch_element_mobile_commands  # noqa
