#Arat:
import dbg

#Altına ekle:
import os

#Arat:
__builtins__.pack_open = pack_open = pack_file

#Üzerine ekle:
if not os.path.isfile("locale.cfg"):
	localeConfig = open("locale.cfg", "w")
	localeConfig.write("10012 1254 tr")
	localeConfig.close()