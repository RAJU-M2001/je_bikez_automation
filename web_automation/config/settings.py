from pathlib import Path
from web_automation.config.config import PROJECT_ROOT, TEST_ENVIRONMENT, TIMEOUT

WEB_AUTOMATION_ROOT = PROJECT_ROOT / "web_automation"
REPORTS_ROOT = WEB_AUTOMATION_ROOT / "reports"
REPORT_DIR = REPORTS_ROOT / TEST_ENVIRONMENT
DEFAULT_REPORT = REPORT_DIR / "pytest_report.html"

def ensure_report_dir() -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    return REPORT_DIR
