from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

#SECRET_KEY = os.getenv("EMAIL")
#DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")