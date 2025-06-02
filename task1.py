import paho.mqtt.client as mqtt
import time
import Adafruit_DHT

mqtt_broker = "broker.hivemq.com"
mqtt_port = 1883
mqtt_qos = 1
mqtt_client = mqtt.Client("iot-21103197d")
mqtt_client.connect(mqtt_broker, mqtt_port)
print("Connect to MQQT broker")


mqtt_topic = "iot/21103197d"
msg = "36.0"
mqtt_client.publish(mqtt_topic,msg,mqtt_qos)
mqtt_client.subscribe(mqtt_topic,mqtt_qos)
print("Publishing message",msg,"to topic",mqtt_topic)

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def mqtt_on_message(client,userdata,msg):
    d_msg = str(msg.payload.decode("utf-8"))
    print("Received message on topic %s: %s" %(msg.topic,d_msg))
mqtt_client.on_message = mqtt_on_message
mqtt_client.loop_start()
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR,DHT_PIN)
    mqtt_client.publish(mqtt_topic, temperature, mqtt_qos)
    print("Publishing message %s to topic %s" % (temperature,mqtt_topic))
    time.sleep(2)