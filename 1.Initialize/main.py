from fastapi import FastAPI

app = FastAPI() # khoi tao 1 instance(vi du)

@app.get('/') # giup cho fastapi hieu phia duoi se la ham thuc thi(handler)
async def root():
    return "Hello VN"
