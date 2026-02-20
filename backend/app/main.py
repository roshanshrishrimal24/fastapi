from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.database import engine, Base
from app.config import get_settings
from app.routers import auth, users, products

# Create database tables
Base.metadata.create_all(bind=engine)

settings = get_settings()

# Initialize FastAPI app
app = FastAPI(
    title="FastAPI Application",
    description="Complete FastAPI with Frontend & Database Integration",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url, "http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "FastAPI is running!"}

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to FastAPI",
        "docs": "/docs",
        "redoc": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)