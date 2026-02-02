"""설정: 환경변수 기반."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """앱 설정."""

    openai_api_key: str = ""
    # 벡터스토어: "memory" | "chroma"
    vector_store_backend: str = "memory"
    # Framer 등 외부 도메인 허용 (쉼표 구분, 예: https://yoursite.framer.website)
    extra_cors_origins: str = ""
    # Hugging Face Space 등: 생성 파일을 output/temp 에 저장하고 max_age 분 후 삭제
    use_temp_for_output: bool = False
    temp_output_max_age_minutes: int = 5

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
