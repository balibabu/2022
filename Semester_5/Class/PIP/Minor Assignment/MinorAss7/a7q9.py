'''Consider the following three sets, namely vehicles, heavyVehicles, and lightVehicles:
Determine the output on executing the following statements:'''

vehicles = {'Bicycle', 'Scooter', 'Car', 'Bike', 'Truck', 'Bus', 'Rickshaw'}
heavyVehicles = {'Truck', 'Bus'}
lightVehicles = {'Rickshaw', 'Scooter', 'Bike', 'Bicycle'}

lytVehicles = vehicles - heavyVehicles
print(lytVehicles)
#
hvyVehicles = vehicles - lightVehicles
print(hvyVehicles)

averageWeightVehicles = lytVehicles & hvyVehicles
print(averageWeightVehicles)

transport = lightVehicles | heavyVehicles
print(transport)

transport.add('Car')
print(transport)

for i in vehicles:
    print(i)

print(len(vehicles))

print(min(vehicles))

print(set.union(vehicles, lightVehicles, heavyVehicles))