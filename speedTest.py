
import speedtest
import time

print("""  
                          _ _            _   
                         | | |          | |  
  ___ _ __   ___  ___  __| | |_ ___  ___| |_ 
 / __| '_ \ / _ \/ _ \/ _` | __/ _ \/ __| __|
 \__ \ |_) |  __/  __/ (_| | ||  __/\__ \ |_ 
 |___/ .__/ \___|\___|\__,_|\__\___||___/\__|
     | |                                     
     |_|                                     
           coded by cihanSrb                            
	""")

time.sleep(1)

print("Please wait...")

test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

download = download / 1048576
upload = upload / 1048576

print("\nDownload : {:.2f} mb/s. \nUpload : {:.2f} mb/s.".format(download,upload))


input("\nPress enter to exit.")

























