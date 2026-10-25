from web_automation.config.config import TEST_ENVIRONMENT, get_base_url

SUPPORTED_ENVIRONMENTS = ("local", "stage", "prod")

def select_environment(environment: str | None = None) -> dict[str, str]:
    selected = (environment or TEST_ENVIRONMENT).strip().lower()
    if selected not in SUPPORTED_ENVIRONMENTS:
        raise ValueError(
            f"Invalid environment '{selected}'. Choose one of "
            f"{', '.join(SUPPORTED_ENVIRONMENTS)}."
        )
    return {"name": selected, "base_url": get_base_url(selected)}
