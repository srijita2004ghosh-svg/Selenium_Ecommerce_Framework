import pytest

from utilities.screenshot import ScreenshotUtil


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # Let the test execute first
    outcome = yield

    # Get the test result
    report = outcome.get_result()

    # We only need the actual test execution result.
    # Do not capture screenshots for setup or teardown failures.
    if report.when != "call":
        return

    # Check whether the test failed
    if report.failed:

        # Get the test class instance
        test_instance = getattr(
            item,
            "instance",
            None
        )

        # Make sure the test instance exists
        if test_instance is None:
            return

        # Make sure the WebDriver exists
        if not hasattr(test_instance, "driver"):
            return

        # Create a safe screenshot name
        test_name = (
            item.nodeid
            .replace("::", "_")
            .replace("/", "_")
            .replace("\\", "_")
            .replace(".py", "")
        )

        # Take screenshot while browser is still open
        try:

            screenshot_path = (
                ScreenshotUtil.take_screenshot(
                    test_instance.driver,
                    test_name
                )
            )

            print(
                f"\nScreenshot saved at: "
                f"{screenshot_path}"
            )

        except Exception as error:

            print(
                f"\nUnable to capture screenshot: "
                f"{error}"
            )