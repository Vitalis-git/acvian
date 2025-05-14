from fastapi import FastAPI
from supabase import create_client, Client
import os

app = FastAPI()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

@app.get("/users")
def get_users():
    result = supabase.table("users").select("*").execute()
    return result.data
