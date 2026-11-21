from jobtrack.models import Posting, JobRef

def test_new_posting_defaults():
    post = Posting("lever", "testCo", "123", "test title",
                   "https://www.testco.com")

    assert post.location is None
    assert post.status is "open"
    assert post.id is None
    assert post.saved_at is None
    assert post.checked_at is None
    assert post.closed_at is None


def test_jobref_equals():
    post = Posting("lever", "testCo", "123", "test title",
                       "https://www.testco.com")
    assert post.ref == JobRef("lever", "testCo", "123")

def test_jobref_hashable():
    ref1 = JobRef("lever", "testCo", "123")
    ref2 = JobRef("lever", "testCo", "123")

    assert len({ref1, ref2}) == 1