#!/bin/bash

echo Marking PhoneInformationTracer.py as executable...
chmod +x PhoneInformationTracer.py

echo Creating Symlink...
ln -s PhoneInformationTracer.py /sbin/phoneInformationTracer

echo Everything\'s set up! Run phoneInformationTracer to get started!