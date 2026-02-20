# Settings Configuration

class Settings:
    def __init__(self):
        self.database_url = "sqlite:///./test.db"
        self.api_key = "your_api_key"
        self.debug_mode = True
        # Add other configuration settings as needed

settings = Settings()