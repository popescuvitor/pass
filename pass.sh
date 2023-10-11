#!/bin/bash
curl -X POST -H "Content-Type: application/json" -d @/home/tqi_vbraco/pass.json http://127.0.0.1:8080/pass
xdotool key --clearmodifiers "ctrl+v"

