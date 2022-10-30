import pytest
from src.unique_email_leetcode import unique_email


@pytest.mark.parametrize(
    ('emails', 'expected'),
    (
        (["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"],2),
        ([],0),
        (["a@leetcode.com","b@leetcode.com","c@leetcode.com"],3),
        (["test.email+alex@leetcode.com", "test.email@leetcode.com"],1)
    )  
)
def test_unique_email_leetcode(emails, expected):
    assert unique_email(emails) == expected
