from pytest import fixture
@fixture(scope="session")
def fix_session():
    print("running Setup SESSION scope")
    yield
    print("running teardown SESSION scope")
@fixture(scope="module")
def fix_mod():
    print("running Setup MODULE scope")
    yield
    print("running Teardown MODULE scope")
@fixture(scope="class")
def fix_class():
    print("running Setup CLASS scope")
    yield
    print("running Teardown CLASS scope")
@fixture()
def fix_func():
    print("running Setup FUNCTION scope")
    yield
    print("running TEARDOWN CLASS scope")
