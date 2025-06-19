from services.common.demo import DEMO_USERS
try:
    from services.ledger.main import DEMO_MODE, list_loans
except Exception:  # pragma: no cover - fastapi not installed
    DEMO_MODE = False
    list_loans = lambda: []


def test_demo_users():
    assert "alice@example.com" in DEMO_USERS


def test_list_loans_demo_mode():
    if DEMO_MODE:
        loans = list_loans()
        assert len(loans) == 3
