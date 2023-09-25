from std_msgs.msg import String
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
import uvicorn as uvicorn
import rospy
import uvicorn


app = FastAPI()
logger = rospy.Publisher("logger_topic", String, queue_size=10)
rospy.init_node('rest_to_ros_logger')

class LogItem(BaseModel):
    log: str
    
@app.post("/log")
async def log(req: LogItem):
    logger.publish(req.log)
    return {"message":"Log received"}
        
if __name__== '__main__':
    uvicorn.run(app, host="http://0.0.0.0", port=8003)
    

