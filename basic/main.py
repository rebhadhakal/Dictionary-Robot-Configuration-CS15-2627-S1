robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}
#name and model
print("NAME AND MODEL")
print(robot["name"])
print(robot["model"])
#battery to 100
print("BATTERY PERCENTAGE")
robot["battery"]=100
print(robot["battery"])
#robot colour
print("ROBOT COLOUR")
robot["colour"]="glaucous"
print(robot["colour"])
#removal of the mode thing
robot.pop("mode")
#number of items
print("NUMBER OF ITEMS")
print(len(robot))
#organized items and things
print("KEY")
for key, value in robot.items():
    print(key,"-",value)