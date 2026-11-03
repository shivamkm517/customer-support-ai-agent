from fastapi import FastAPI

app = FastAPI(title="ShopEase AI Support")

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "ShopEase AI Support is running"
    }

