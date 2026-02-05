import os
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from /backend/.env 
load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = "agentic_architect"

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect_to_storage(cls):
        """Establish MongoDB connection."""
        cls.client = AsyncIOMotorClient(MONGODB_URL)
        cls.db = cls.client[DATABASE_NAME]
        print(f"Connected to MongoDB: {DATABASE_NAME}")

    @classmethod
    async def close_storage(cls):
        """Close MongoDB connection."""
        cls.client.close()

async def save_roadmap(user_id: str, github_username: str, roadmap_data: dict):
    """
    Saves a generated roadmap to the 'roadmaps' collection.
    """
    roadmap_entry = {
        "user_id": user_id,
        "github_username": github_username,
        "roadmap": roadmap_data,
        "created_at": datetime.utcnow(),
        "status": "completed"
    }
    
    result = await MongoDB.db.roadmaps.insert_one(roadmap_entry)
    return str(result.inserted_id)

async def get_user_roadmaps(user_id: str):
    """
    Retrieves all roadmaps for a specific user.
    """
    cursor = MongoDB.db.roadmaps.find({"user_id": user_id})
    roadmaps = await cursor.to_list(length=100)
    
    # Convert MongoDB _id to string for JSON serialization
    for roadmap in roadmaps:
        roadmap["_id"] = str(roadmap["_id"])
        
    return roadmaps