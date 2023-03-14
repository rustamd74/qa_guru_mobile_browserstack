import allure
from allure_commons.types import AttachmentType
#https://app-automate.browserstack.com/s3-upload/bs-video-logs-euw/s3.eu-west-1/2b7e5c4dd50ca1dc2a740c1fb0981ef8c8d91bfa/video-2b7e5c4dd50ca1dc2a740c1fb0981ef8c8d91bfa.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2XUQHUQMLGDEA5FL%2F20230314%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20230314T143707Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=08e3516a1336f110db26fc38e1e3267a55c6505f7521e0a77fb428c1cbd769b6


def add_video(browser):
    video_url = f"https://app-automate.browserstack.com/s3-upload/bs-video-logs-euw/s3.ap-west-1/" \
                f"{browser.driver.session_id}/video-{browser.driver.session_id}.mp4"
    html = (
        "<html><body><video width='100%' height='100%' controls autoplay><source src='"
        + video_url
        + "' type='video/mp4'></video></body></html>"
    )
    allure.attach(
        body=html,
        name="video_" + browser.driver.session_id,
        attachment_type=AttachmentType.HTML,
        extension=".html",
    )
