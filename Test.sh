#! /bin/bash
rm -rf /var/lib/mkt/Res/Data/BaseDB
mkdir -p /var/lib/mkt/Res/Data/BaseDB
cp -r . /var/lib/mkt/Res/Data/BaseDB
python3 /var/lib/mkt/Res/Data/BaseDB/Build.py