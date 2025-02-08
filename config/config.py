import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

URL = "https://brainlox.com/courses/category/technical"
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
