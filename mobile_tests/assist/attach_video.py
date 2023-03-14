import allure
from allure_commons.types import AttachmentType
#https://app-automate.browserstack.com/s3-upload/bs-video-logs-aps/s3.ap-south-1/3ee8cbec3d2798524f281aa857b8c9ffa67a574e/video-3ee8cbec3d2798524f281aa857b8c9ffa67a574e.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2XUQHUQMLGDEA5FL%2F20230314%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20230314T122808Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=70411931406b663fcfc52f482ce0185671656dd8a88ab81492f50fad0d46a86d

def add_video(browser):
    video_url = f"https://app-automate.browserstack.com/s3-upload/bs-video-logs-aps/s3.ap-south-1/" \
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
