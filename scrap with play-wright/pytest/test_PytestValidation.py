#Fixture
import pytest

@pytest.fixture(scope="module")
def preWork():
    print("I setup module instance")
    return 'fail'

@pytest.fixture(scope="function")
def secondWork():
    print("I setup browser instance")
    yield #pause
    print('tear down validation')

def test_instialCheck(preWork, secondWork):
    print('this is the first test')
    assert preWork == 'fail'

@pytest.mark.skip
def test_secondCheck(preSetupWork, secondWork):
    print("Running the second text")