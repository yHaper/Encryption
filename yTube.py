from pytube import YouTube
from pytube.cli import on_progress
import os
import time
os.system("clear")

nomi = input("\033[1;31mDigite seu nome: \033[m")
os.system("clear")

cu = 0
while cu <1:
	print("\033[1;31mＹＴ  Ｄｏｗｎｌｏａｄ\033[m MP4\n\033[0;31m   ᵇʸ ʸᴴᵃᵖᵉʳ\n\033[m")
	print("\033[0;31mOque voce deseja, {} ?\033[m" .format(nomi))
	print("\033[31m[1] \033[mBaixar videos\n\033[0;31m[2] \033[mBaixar audios\n\033[0;31m[3]\033[m Sair")
	cobra = input("\n\033[0;31m~ \033[m")
	
	
	if cobra == '2':
		os.system("clear")
		
		print("\033[1;31mＹＴ  Ｄｏｗｎｌｏａｄ\033[m MP4\n\033[0;31m   ᵇʸ ʸᴴᵃᵖᵉʳ\n\033[m")
		
		link = input("\033[1;31mLink do audio que deseja baixar: \033[m")
		
		yt = YouTube(link, on_progress_callback = on_progress)
		
		os.system("clear")
		print("\033[0;32mBaixando... /\033[m")
		print("Titulo = ", yt.title)
		time.sleep(0.3)
		os.system("clear")
		
		print("\033[0;32mBaixando... -\033[m")
		print("Titulo = ", yt.title)
		time.sleep(0.3)
		os.system("clear")
		
		print("\033[0;32mBaixando... \  \033[m")
		print("Titulo = ", yt.title)
		time.sleep(0.3)
		os.system("clear")
		
		ys = yt.streams.get_audio_only()
		
		out_file = ys.download()
		base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file)
		
		
		os.system("clear")
		print("\033[1;32mPronto!\033[m")
		break
		
	if cobra == '1':
		os.system("clear")
		
		print("\033[1;31mＹＴ  Ｄｏｗｎｌｏａｄ\033[m MP4\n\033[0;31m   ᵇʸ ʸᴴᵃᵖᵉʳ\n\033[m")
		
		link = input("\033[1;31mLink do video que deseja baixar: \033[m")
		
		yt = YouTube(link, on_progress_callback = on_progress)
		
		os.system("clear")
		print("\033[0;32mBaixando... /\033[m")
		print("Titulo = ", yt.title)
		time.sleep(0.3)
		os.system("clear")
		
		print("\033[0;32mBaixando... -\033[m")
		print("Titulo = ", yt.title)
		time.sleep(0.3)
		os.system("clear")
		
		print("\033[0;32mBaixando... \  \033[m")
		print("Titulo = ", yt.title)
		time.sleep(0.3)
		os.system("clear")
		
		ys = yt.streams.get_highest_resolution()
		
		ys.download()
		
		os.system("clear")
		print("\033[1;32mPronto!\033[m")
		break
	break