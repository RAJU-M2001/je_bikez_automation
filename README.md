# JE BikeZ Playwright Automation

Python + Playwright framework for smoke and UI checks for the JE BikeZ website.

## Pages covered

- Authentication: login and signup
- Home
- Service
- Builds
- Sales
- About Us
- Contact
- Navigation

## Setup (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
Copy-Item .env.example .env
```

Edit `.env` and choose the target environment. `prod` currently points to
`https://je-bikez-frontend.onrender.com`. Set `BASE_URL_STAGE` only after a
real staging URL exists.

## Run tests

From the repository root:

```powershell
python -m web_automation.main
```

Run all tests directly:

```powershell
python -m pytest web_automation/tests -v
```

Run one test module:

```powershell
python -m pytest web_automation/tests/test_authentication.py -v
```

Reports are written under `web_automation/reports/<environment>/`.

## Important notes

- No `pytest.ini`, `conftest.py`, `session.py`, or `test_data/` is used.
- Each test creates and closes its own browser/page through `core/browser.py`.
- The first version uses conservative smoke checks and common accessible selectors.
  Check the actual website labels/DOM and adjust the locator files if the UI differs.
- Production tests should be read-only. Login/signup form submission, service bookings,
  contact submissions, and admin changes can create data. Keep such tests pointed at a
  dedicated test environment or use dedicated test accounts.
- Never commit real credentials. Add secrets to GitHub Actions repository secrets if needed.
