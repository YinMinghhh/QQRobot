import uvicorn
from fastapi import FastAPI, Request

from sample.group_service import group_service

app = FastAPI()

@app.post("/")
async def root(request: Request):
    data = await request.json()  # 获取事件数据
    print(data)

    message_type = data.get('message_type')
    if message_type == 'group':
        group_service.serve(data)

if __name__ == "__main__":
    uvicorn.run(app, port=8080)
