from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = (3)
# Jouw python instructies zet je vanaf hier:
for a in range(1,5,+1):
    for x in range(a):
        robotArm.grab()
    for x in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(5):
        robotArm.moveLeft()
    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()