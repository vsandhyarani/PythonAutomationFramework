print("ENVIRONMENT FILE LOADED")

import allure
from allure_commons.types import AttachmentType


def after_step(context, step):
    if step.status == "failed":
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=f"Failed Step - {step.name}",
            attachment_type=AttachmentType.PNG
        )