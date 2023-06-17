import pyownet

owproxy = pyownet.protocol.proxy(host="localhost", port=4304)
ow_dir = owproxy.dir()
print(ow_dir)
val = owproxy.read(f"{ow_dir[0]}temperature")
print(val)

sensor = ow_dir[0]
temp = float(owproxy.read(sensor + "temperature"))
temp = "{0:.5f}".format(temp)
print(temp)

