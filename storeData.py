#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Autor: Franc Rodriguez

# Eina per guardar el consum energètic mensual d'un  SONOFF POWR2 en una BBDD MySQL

import mysql.connector
from mysql.connector import Error
import paho.mqtt.client as mqtt
from datetime import datetime

def on_connect(client, userdata, flags, rc):
  client.subscribe("SONOFF-POWR2/energy")

def on_message(client, userdata, msg):
    data = datetime.today().strftime('%Y-%m-%d')
    connection = mysql.connector.connect(host='server',
                                         database='database',
                                         user='user',
                                         password='password')
    cursor = connection.cursor()
    totalConsum = msg.payload.decode()
    sql = "INSERT INTO pantalles (Data, Consum) VALUES (%s, %s)"
    valors = (data, totalConsum)
    cursor.execute(sql, valors)
    connection.commit()
    client.disconnect()

client = mqtt.Client()
client.connect("192.168.1.218",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
