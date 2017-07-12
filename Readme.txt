You have to do as follow:

1. Save the "Xtandem_exe.py" and "config.ini" file wherever you want.
2. Make an input directory and move all the raw_files and fasta file there.
3. Make an output directory.
4. Open the "config.ini" and fill following fields in Directory section:
	1. input directory path #the complete path to input folder( including all the .mzXML and .fasta files)
	2. output directory path 
	3. tandem directory path 

5. Open the following link and set all the required variables based on your eperiment design, and click on the view method at the end of the page. A new window will be opened with all the parameters' value that are required. fill parameters in config.ini with those values.
6. Open cmd in windows or terminal in mac.
7. Change your directory with cd command to the place you save the "Xtandem_exe.py" file
8. Make sure you have a python version > 3.5 & tandem software installed
9. Type "python Xtandem_win_exe.py" for windows OS and "python Xtandem_mac_exe.py"

#every file took around 10 minutes on my laptop. So be careful about the time and don't add too many mzXML files in input folder and run the python script on a workstation.