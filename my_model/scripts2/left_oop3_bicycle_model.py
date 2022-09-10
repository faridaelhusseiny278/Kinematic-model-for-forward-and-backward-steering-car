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



    def pose_callback(self,pose):
        
        cmd= Twist()
        
        self.beta= math.atan(self.ll*math.tan(self.steeringangle))/(self.lr+self.ll)

        self.x_dot=self.velocity*math.cos(self.beta+pose.theta)
        self.x=pose.x + self.t*self.x_dot

        self.y_dot=self.velocity*math.sin(self.beta+pose.theta)
        #cmd.linear.y=self.y_dot
        cmd.linear.x= self.velocity
        self.y = pose.y +self.t* self.y_dot
 
        self.theta_dot=self.velocity*math.cos(self.beta)*math.tan(steering_angle)/self.lr+self.ll
        cmd.angular.z=self.theta_dot
        self.theta=pose.theta+ self.t*self.theta_dot

        

        self.pub.publish(cmd)





if __name__=='__main__':
        try:
                
                rospy.init_node('left_oop3_my_bicycle_model')
                t=float(input("delta t: "))
                steering_angle=float(input("steering angle: "))
                velocity= float(input("velocity: "))
                Lr=float(input("Lr: "))
                Ll=float(input("Ll:"))
                Bicycle_model(t,velocity,Lr,Ll)
                #keda hadtar a3mel 2 yaml files?
                # Lr=rospy.get_param('/turtle_project/lr')
                # Ll=rospy.get_param('/turtle_project/ll')
                
                rospy.loginfo("publisher node 1 has been started")
                rospy.spin()

        except rospy.ROSInterruptException:
            rospy.loginfo("node terminated")
    