#Euro Truck Simulator 2 Telemetry Python Client

This is a simple python-2.7 client for the ETS2-Telemetry plugin. If you want use the python client, please follow the install steps for the c# Client. This script is Alpha version.

##Example for engineRpm
```python
e = ets2sdkclient()
e.update()
print e.engineRpm
```

##Exampke for print all values
```python
e = ets2sdkclient()
e.update()
e.printall()
```