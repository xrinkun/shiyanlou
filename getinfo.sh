#!/bin/bash
df -h | awk 'NR==2{b=$5;if($5<"85%"){a="is OK"}else{a="need notice"}{printf "Disk-Root:\t%s",a;printf ",use: %s\n",b}}'
free | awk 'NR==2{d=$3/$2;if(d < 0.9){c="is OK"}else{c="need notice"}{printf "Memory:         %s",c;printf ",use: %.2f%%\n",d*100}}'
uptime | awk '{print $10}' | sed 's/,//' | awk '{if($0<0.7){e="is OK"}else{e="nedd notice"};{printf "Loadaverage:\t%s,use: %.2f",e,$0}}'
