#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import time
from Helpers.kinematics import Kinematic
from spotmicroai.msg import LegCommand
from Parts.Leg import Leg
from enum import Enum


class Positions():
    Agachado=[-55,-100,20]
    Arriba=[-55,-190,20]
    SitFront=[-55,-260,20]
    SitBack=[-55,-160,20]
    Test=[0,0,0]

class movements:

    def __init__(self):
        self.k=Kinematic()
        self.posiciones=Positions()

        #Initialize publishers
        self.MoveLegs=rospy.Publisher('spotmicroai/MoveLegs', LegCommand,queue_size=10)

        #Initialize Ros node
        rospy.init_node('Movimiento', anonymous=True)

    def Move(self, Legs, Posicion):
        
        #Get angles
        angles=self.k.legIK(Posicion)     

        #Prepare data for the msg
        msg=LegCommand()
        msg.Theta1=angles[0]
        msg.Theta2=angles[1]
        msg.Theta3=angles[2]

        msg.Legs=Legs
        #publish the msg
        self.MoveLegs.publish(msg)

movimiento = movements()
Posiciones=Positions()
SIT=1
UP=0
DOWN=0
rospy.sleep(1)
if SIT:
    Legs=[0,0,1,1]
    movimiento.Move(Legs,Posiciones.SitBack)
    Legs=[1,1,0,0]
    movimiento.Move(Legs,Posiciones.SitFront)
if UP:
    Legs=[1,1,1,1]
    movimiento.Move(Legs,Posiciones.Arriba)
if DOWN:
    Legs=[1,1,1,1]
    movimiento.Move(Legs,Posiciones.Agachado)

rospy.sleep(3)
SIT=0
UP=0
DOWN=1
if SIT:
    Legs=[0,0,1,1]
    movimiento.Move(Legs,Posiciones.SitBack)
    Legs=[1,1,0,0]
    movimiento.Move(Legs,Posiciones.SitFront)
if UP:
    Legs=[1,1,1,1]
    movimiento.Move(Legs,Posiciones.Arriba)
if DOWN:
    Legs=[1,1,1,1]
    movimiento.Move(Legs,Posiciones.Agachado)

rospy.sleep(4)
SIT=0
UP=1
DOWN=0
if SIT:
    Legs=[0,0,1,1]
    movimiento.Move(Legs,Posiciones.SitBack)
    Legs=[1,1,0,0]
    movimiento.Move(Legs,Posiciones.SitFront)
if UP:
    Legs=[1,1,1,1]
    movimiento.Move(Legs,Posiciones.Arriba)
if DOWN:
    Legs=[1,1,1,1]
    movimiento.Move(Legs,Posiciones.Agachado)
