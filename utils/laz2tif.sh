#!/bin/bash
cd ../data
for i in *.laz ; do
    echo "las2las $i"
    las2las -i "$i" -o "$(basename "${i/.laz}")".las
    sleep 60
done

for i in *.las ; do
    echo "whitebox $i"
    whitebox_tools -r lidar_idw_interpolation -i "$i" -o "$(basename "${i/.las}")".tif --parameter elevation --resolution 0.5 --weight 1.0 --radius 1.5
done
