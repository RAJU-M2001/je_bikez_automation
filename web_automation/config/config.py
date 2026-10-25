
"""
JE BikeZ automation configuration.
"""

from pathlib import Path
import os

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def _as_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


TEST_ENVIRONMENT = os.getenv("TEST_ENVIRONMENT", "prod").strip().lower()
BROWSER = os.getenv("BROWSER", "chromium").strip().lower()

# Visible browser by default.
HEADLESS = _as_bool(os.getenv("HEADLESS"), False)

try:
    TIMEOUT = int(os.getenv("TIMEOUT", "15000"))
except ValueError as exc:
    raise ValueError(
        "TIMEOUT must be an integer number of milliseconds."
    ) from exc

BASE_URLS = {
    "local": os.getenv(
        "BASE_URL_LOCAL", "http://127.0.0.1:3000"
    ).strip(),
    "stage": os.getenv("BASE_URL_STAGE", "").strip(),
    "prod": os.getenv(
        "BASE_URL_PROD",
        "https://je-bikez-frontend.onrender.com",
    ).strip(),
}


def get_base_url(environment: str | None = None) -> str:
    """Return the base URL for the selected environment."""

    selected = (environment or TEST_ENVIRONMENT).strip().lower()

    if selected not in BASE_URLS:
        raise ValueError(
            f"Unsupported TEST_ENVIRONMENT '{selected}'. "
            f"Choose: {', '.join(BASE_URLS)}."
        )

    url = BASE_URLS[selected]

    if not url:
        raise ValueError(
            f"BASE_URL_{selected.upper()} is empty. "
            "Set it in your .env file."
        )

    return url.rstrip("/")
