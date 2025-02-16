from .base import *  # noqa: F401, F403

ALLOWED_HOSTS = ["admin-vd2.kro.kr"]

DEBUG = False

INTERNAL_IPS = []  # 프로덕션 환경에서는 빈 리스트로 설정

CSRF_TRUSTED_ORIGINS = ["https://admin-vd2.kro.kr"]

CORS_ALLOWED_ORIGINS = ["https://admin-vd2.kro.kr"]

# # 추가 보안 설정
# SECURE_SSL_REDIRECT = True  # HTTP를 HTTPS로 리다이렉트
# SESSION_COOKIE_SECURE = True  # HTTPS에서만 쿠키 전송
# CSRF_COOKIE_SECURE = True  # HTTPS에서만 CSRF 쿠키 전송
# SECURE_BROWSER_XSS_FILTER = True  # XSS 필터링 활성화
# SECURE_HSTS_SECONDS = 31536000  # HSTS 활성화 (1년)
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # HSTS 서브도메인 포함
# SECURE_HSTS_PRELOAD = True  # HSTS 프리로드 활성화
