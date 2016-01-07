#!/usr/bin/python

__author__ = 'RFSilva - WarDriving Portugal'
version = '0.1 beta'



import os,subprocess,time,argparse,sys
import bluetooth
import socket

from settings import *
from lang_en import *
from blue import *


def banner():
	print(bcolors.ROSA + """
 __      __             ________        .__      .__                 
/  \    /  \_____ ______\______ \_______|__|__  _|__| ____    ____   
\   \/\/   /\__  \\_  __ \    |  \_  __ \  \  \/ /  |/    \  / ___\  
 \        /  / __ \|  | \/    `   \  | \/  |\   /|  |   |  \/ /_/  > 
  \__/\  /  (____  /__| /_______  /__|  |__| \_/ |__|___|  /\___  /  
       \/        \/             \/                       \//_____/   
      __________              __                     .__             
      \______   \____________/  |_ __ __  _________  |  |            
       |     ___/  _ \_  __ \   __\  |  \/ ___\__  \ |  |            
       |    |  (  <_> )  | \/|  | |  |  / /_/  > __ \|  |__          
       |____|   \____/|__|   |__| |____/\___  (____  /____/          
                                       /_____/     \/                

                                       """)


# Arg Start 

def start_capture():

	try:

		print("""Setting up BlueTooth conection to GPS Device...\n
		#check_bt_inter();
		#select_bt_inter);
		#scan_bt_dev(); --> Feito
		#check_mac(); --> Feito
		#check_serv(); --> Feito
		#check_rfcomm_conn();
		#connect_to_bt_dev();
		\n""")

		print(bcolors.GREEN + "Lets check BT GPS device...\n\n")
		
		scan_bluetooth();
		mac_attack = raw_input(bcolors.BLUE + "MAC to check services -> ")
		check_mac(mac_attack);
		check_serv(mac_attack);
		channel = input(bcolors.BLUE + "Port / Channel -> ")
		
		liga_bluetooth(mac_attack,channel);


		time.sleep(1)




		print("""Setting up Wifi Interfaces...\n")

		#check_wifi_inter();
		#select_wifi_inter();
		\n""")

		time.sleep(1)



		print("""Killing Processes to run nice...

		#kismet_server
		#gpsd
		#dhclient
		#rfcomm
		\n""")

		time.sleep(1)


		print("""Initiating Apps...

		#start_terminator()
		#start_gpsd()
		#start_kismet() --file=own_file.config
		\n\n""")

		time.sleep(1)






	except Exception, e:
		print("Error starting Capture...")

		raise e





# Create a Dir in /tmp/$var 
def cria_dir(nome_dir):
	try:
		create_dir = subprocess.call(C_DIR + nome_dir, shell=True)
		print var_texts['1'] + nome_dir
	except Exception, e:
		print (error_texts['2'])
		raise e



# Arg Install

def install_apps(distro):
	if distro =="Ubuntu":
		print apps_texts['1']
		proc_term = subprocess.call(UBUNTU + INSTALL + APPS, shell=True)

	elif distro =="Fedora":
		print apps_texts['2']
		proc_term = subprocess.call(FEDORA + INSTALL + APPS , shell=True)

	elif distro == "Arch":
		print apps_texts['3']
		proc_term = subprocess.call(ARCH + INSTALL + APPS, shell=True)

	elif distro == "Raspas":
		print apps_texts['4']
		proc_term = subprocess.call(RASPAS + INSTALL + APPS , shell=True)

	elif distro == "Pwnpi":
		print apps_texts['5']
		proc_term = subprocess.call(PWNPI + INSTALL + APPS , shell=True)



# Arg Data Management --> Proxima Versao


def data_manag(distro):
	print("Data Management\n\n")
	try:
		print(data_texts['google'])
		#export_kml();
	except Exception, e:
		raise e

	try:
		print (data_texts['csv'])
		#export_csv();
	except Exception, e:
		raise e
	try:
		print (data_texts['pcap'])
		#export_pcap();
	except Exception, e:
		raise e

# Arg Config


def config(distro):
	print(bcolors.RED + var_texts['2'])

# Arg Advanced Config

def advanced_config(distro):
	print(bcolors.RED + var_texts['3'])


# Arg Update 

def distro_update(distro):

	if distro =="Ubuntu":
		print (update_texts['ubuntu'])
		os.system(UBUNTU + UPDATE)
	elif distro =="Fedora":
		print (update_texts['fedora'])
		os.system(FEDORA + UPDATE)
		return credits();
	elif distro == "Arch":
		print(update_texts['arch'])
		os.system(ARCH + UPDATE)
	elif distro =="Raspas":
		print(update_texts['raspas'])
		os.system(RASPAS + UPDATE)
	elif distro == "PWNPI":
		print(update_texts['pwnpi'])
		os.system(PWNPI + UPDATE)
	else:
		print(update_texts['error'])



# Arg Credits

def show_credits():
	for creds in credits_texts:
		print(credits_texts[creds])






class sniff_frequencies(object):
	"""docstring for sniff_frequencies"""
	do_clean= subprocess.call("clear", shell=True)
	print banner()





	parser = argparse.ArgumentParser(
		prog='WarDriving',
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description=(bcolors.BLUE + '''
        Portuguese WarDriving Community             
         '''),
		prefix_chars='--')
	parser.add_argument('--start',action="store_true",
		help=bcolors.GREEN + args_texts['start'] + bcolors.RED + ' 75%% Done')

	parser.add_argument('--data_management',action="store_true",
		help=bcolors.GREEN + args_texts['data'] + bcolors.RED +' next version')

	parser.add_argument('--install',action="store_true",
	    help=bcolors.GREEN + args_texts['install'] + bcolors.RED + ' 90%% Done')

	parser.add_argument('--config',action="store_true",
		help=bcolors.GREEN + args_texts['config'] + bcolors.RED + 'next version')

	parser.add_argument('--advanced',action="store_true",
		help=bcolors.GREEN + args_texts['advanced'] + bcolors.RED + ' next version')

	parser.add_argument('--update',action="store_true",
	    help=bcolors.GREEN + args_texts['update'] + bcolors.RED + ' 90%% Done')

	parser.add_argument('--credits',action="store_true",
		help=bcolors.GREEN + args_texts['credits']  + bcolors.RED + ' 100%% Done')


	args = parser.parse_args()


	if args.start:
		try:
			start_capture();
		except Exception, e:
			raise e
			print(bcolors.RED + error_texts['3'])

	elif args.update:
		try:
			if not os.geteuid()==0:
    					sys.exit(apps_texts['4'])
	    		else:
   						distro = raw_input(bcolors.BLUE + apps_texts['2'] + bcolors.RED + apps_texts['3'])
   						distro_update(distro);
		except KeyboardInterrupt:
			raise e
        		print(end_app['1'] + bcolors.GREEN + end_app['2'] + bcolors.BRANCO + EMAIL + bcolors.RED + end_app['3'])
	elif args.config:
		try:
			distro = raw_input(bcolors.BLUE + apps_texts['2'] + bcolors.RED + apps_texts['3'])

			config(distro);
		except KeyboardInterrupt:
        		print(end_app['1'] + bcolors.GREEN + end_app['2'] + bcolors.BRANCO + EMAIL + bcolors.RED + end_app['3'])

	elif args.data_management:
		try:
			distro = raw_input(bcolors.BLUE + apps_texts['2'] + bcolors.RED + apps_texts['3'])

			data_manag(distro);
		except KeyboardInterrupt:
        		print(end_app['1'] + bcolors.GREEN + end_app['2'] + bcolors.BRANCO + EMAIL + bcolors.RED + end_app['3'])

	elif args.credits:
		try:
			show_credits();
		except KeyboardInterrupt:
        		print(end_app['6'] + bcolors.GREEN + end_app['2'] + bcolors.BRANCO + EMAIL + bcolors.RED + end_app['3'])

	elif args.install:
		try:
			distro = raw_input(bcolors.BLUE + apps_texts['2'] + bcolors.RED + apps_texts['3'])
			install_apps(distro);
		except KeyboardInterrupt:
        		print(end_app['1'] + bcolors.GREEN + end_app['2'] + bcolors.BRANCO + EMAIL + bcolors.RED + end_app['3'])

	elif args.advanced:
		try:
			distro = raw_input(bcolors.BLUE + apps_texts['2'] + bcolors.RED + apps_texts['3'])
			advanced_config(distro);
		except KeyboardInterrupt:
        		print(end_app['1'] + bcolors.GREEN + end_app['2'] + bcolors.BRANCO + EMAIL + bcolors.RED + end_app['3'])

	else:
		print(bcolors.RED + args_texts['help'])



	def __init__(self, arg):
		super(sniff_frequencies, self).__init__()
		self.arg = arg
		print("Smell the air")
		

