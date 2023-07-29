#!/usr/bin/env bash

find /home/carpi/Recordings/* -type d -ctime +10 | xargs rm -rf
find /home/carpi/Dashcam/Logs/* -type d -ctime +10 | xargs rm -rf