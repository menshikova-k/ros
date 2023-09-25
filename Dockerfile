FROM ros:noetic

RUN apt-get update && ap-get install -y \ 
    


COPY . /catkin_ws/test

RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && \ 
    cd /catkin_ws && \
    catkin_make"
	
RUN echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc

CMD /bin/bash -c "source /catkin_ws/devel/setup.bash && \ 
    roslauch test my_nodes.launch



