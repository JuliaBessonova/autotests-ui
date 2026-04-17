import pytest
import random

@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_reruns():
    assert random.choice([True, False]) == True