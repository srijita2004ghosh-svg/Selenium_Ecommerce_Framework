import os
from datetime import datetime


class ScreenshotUtil:

    @staticmethod
    def take_screenshot(driver, test_name):

        # Find project root
        project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        # Screenshot folder
        screenshot_dir = os.path.join(
            project_root,
            "screenshots"
        )

        # Create folder if it does not exist
        os.makedirs(
            screenshot_dir,
            exist_ok=True
        )

        # Create timestamp
        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        # Create screenshot filename
        filename = f"{test_name}_{timestamp}.png"

        screenshot_path = os.path.join(
            screenshot_dir,
            filename
        )

        # Capture screenshot
        driver.save_screenshot(
            screenshot_path
        )

        return screenshot_path