#!/usr/bin/env python3
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
class Bicycle_model():
   
        
       
    def __init__(self,t,v,lr,ll):
        self.t=t
        self.velocity=v
        self.pub= rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
        self.sub=rospy.Subscriber("/turtle1/pose",Pose, self.pose_callback)
        self.x=0
        self.y=0
        self.theta=0
        self.steeringangle=0
        self.lr=lr
        self.ll=ll
        self.beta=0

        #rospy.timer(rospy.duration)

    def pose_callback(self,pose):
        cmd= Twist()
        
        self.beta= math.atan(self.lr*math.tan(self.steeringangle))/(self.lr+self.ll)
        
        self.x_dot=self.velocity*math.cos(self.beta+self.theta)
        cmd.linear.x=self.x_dot
        self.x=pose.x + self.t*self.x_dot

        self.y_dot=self.velocity*math.sin(self.beta+self.theta)
        cmd.linear.y=self.y_dot
        self.y = pose.y +self.t* self.y_dot

        self.theta_dot=self.velocity*math.tan(self.steeringangle)*math.cos(self.beta)/self.lr+self.ll
        cmd.angular.z=self.theta_dot
        self.theta=pose.theta+ self.t*self.theta_dot

        

        self.pub.publish(cmd)





if __name__=='__main__':
        try:
        
                rospy.init_node('my_bicycle_model')
                t=float(input("delta t: "))
                steering_angle=float(input("steering angle: "))
                velocity= float(input("velocity: "))
                #Lr= float(input("Lr: "))
               # Ll= float(input("Ll: "))
                Ll= rospy.get_param('/oop2_bicycle_model/Ll')
                Lr= rospy.get_param('/oop2_bicycle_model/Lr')
                Bicycle_model(t,velocity,Lr,Ll)
                
               
                
                rospy.loginfo("publisher node 1 has been started")
                rospy.spin()

        except rospy.ROSInterruptException:
            rospy.loginfo("node terminated")
    