.DEFAULT_GOAL := build


build: java card
	python3 terminal_src/main.py

java:
	javac -source 1.2 -target 1.1 -g -cp /home/amarante/IdeaProjects/jsmr/sdks/jc211_kit/bin/api.jar src/main/java/main/Main.java
	java -classpath sdks/jc211_kit/bin/converter.jar:. com.sun.javacard.converter.Converter -verbose -exportpath sdks/jc211_kit/api_export_files:main -classdir . -applet 0xa0:0x0:0x0:0x0:0x62:0x3:0x1:0xc:0x6:0x1:0x2 Main src/main/java/main  0x0a:0x0:0x0:0x0:0x62:0x3:0x1:0xc:0x6:0x1 1.0

card:
	gpshell scripts/deleteApplet	
	gpshell scripts/uploadApplet

