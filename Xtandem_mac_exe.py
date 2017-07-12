# -*- coding: utf-8 -*-
"""
Mehrnoosh Oghbaie
07/06/2017
Running X-tandem from python for mac
"""
import subprocess
import os
from lxml import etree as et
import configparser

def parse_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def taxonomyMaker(species, fasta_files, bindir):
    bioml = et.Element("bioml")
    bioml.attrib["label"]="x! taxon-to-file matching list"
    taxon = et.SubElement(bioml, "taxon")
    taxon.attrib["label"]=species
    children = [
        et.Element('file', URL="../fasta/"+str(i),format="peptide")
        for i in fasta_files
        ]
    taxon.extend(children)
    tree = et.ElementTree(bioml)
    tree.write(bindir+"/taxonomy.xml", pretty_print=True, method="xml")
    
def inputXmlMaker(bindir,inputdir,outputdir,config,i):
    bioml = et.Element("bioml")
    for section in config.sections():
        for key in config[section]: 
            if section!= "Directory":
                et.SubElement(bioml,'note', type="input", label=key).text=config[section][key]
    tree = et.ElementTree(bioml)
    spectrum = tree.find("//note[@label='spectrum, path']")
    spectrum.text=inputdir+"/"+i
    output = tree.find("//note[@label='output, path']")
    output.text=outputdir+"/"+i.split(".", 1)[0]+".xml"
    tree.write(bindir+"/input.xml", pretty_print=True, method="xml")      

def XMLmod(inputdir):
        term_list=['.mzXML','.mzML','.mzData','.pkl','.mgf']
        input_files = [fn for fn in os.listdir(inputdir)
                      if any(fn.endswith(ext) for ext in term_list)]
        return input_files
 
def xtandem_exe():
    config= parse_config()
    config.read('../config.ini')
    inputdir = config.get('Directory', 'input directory path')
    outputdir = config.get('Directory', 'output directory path')
    tandemdir = config.get('Directory', 'tandem directory path')
    species = config.get('Protein general', 'protein, taxon')
    # Search for .fasta file in input folder (consider that input folder )
    fasta_file = list(filter(lambda fname: '.fasta' in fname, os.listdir(inputdir)))[0]
    # Building .fasta file original directory
    fasta_file_dir=inputdir+"/"+fasta_file
    # Building X-tandem bin directory
    bindir = tandemdir+"/bin"
    # Building X-tandem fasta directory
    fastadir = tandemdir+"/fasta"
    # Change the directory to bin X-tandem
    os.chdir(bindir)
    # Running fasta_pro on .fasta file
    subprocess.call("fasta_pro "+fasta_file_dir, shell=True)
    # Saving .fasta files in list
    fasta_files = list(filter(lambda fname: '.fasta' in fname, os.listdir(inputdir)))
    # Moving all the fasta files to fasta directory
    subprocess.call("move "+ inputdir+"\*.fasta* "+ fastadir, shell=True)
    # Create taxonomy.xml file
    taxonomyMaker(species, fasta_files, bindir)
    # Getting the list of input files
    input_files = XMLmod(inputdir)
    for i in input_files:
        #Building input.xml file
        inputXmlMaker(bindir,inputdir,outputdir,config,i)
        # Running the input.xml file
        subprocess.call(["tandem", "input.xml"])

xtandem_exe()


