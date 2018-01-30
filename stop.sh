#! /biin/sh
ps aux|grep IPProxy.py|awk '{print $2}'|xargs kill -9
