import rospy
from std_msgs.msg import String
from pydantic import BaseModel
import json
from typing import Any
import requests

LOGGER_URL = "http://0.0.0.0:8003/log"
app = FastAPI()
rospy.init_node("listener_node")

class LogItem(BaseModel):
   data: str
   
@app.post("/info")
async def process(req: LogItem):
    new_data = json.dumps({"log":req.data})
    requests.post(LOGGER_URL, new_data)
    return {"message":"Data sent"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8001)
