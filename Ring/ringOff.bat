rshell -p COM3 --buffer-size 512
repl
from machine import Pin
out = Pin(0,Pin.OUT)
out.off()