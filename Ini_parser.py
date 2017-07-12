# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 15:28:23 2017

@author: moghb
"""

import configparser
config = configparser.ConfigParser()
config.read('C:\\Users\\moghb\\OneDrive\\Documents\\config.ini')
#config.filename = 'config.ini'
config.add_section('Spectrum general')
config.set('Spectrum general', 'spectrum, fragment monoisotopic mass error', '0.4')
config.set('Spectrum general', 'spectrum, fragment monoisotopic mass error units', 'Daltons')
config.set('Spectrum general', 'spectrum, parent monoisotopic mass error plus', '20')
config.set('Spectrum general', 'spectrum, parent monoisotopic mass error minus', '20')
config.set('Spectrum general', 'spectrum, parent monoisotopic mass error units', 'ppm')
config.set('Spectrum general', 'spectrum, parent monoisotopic mass isotope error', 'yes')

config.add_section('Spectrum conditioning')
config.set('Spectrum conditioning', 'spectrum, dynamic range', '100')
config.set('Spectrum conditioning','spectrum, total peaks',	'50')
config.set('Spectrum conditioning','spectrum, use noise suppression',	'no')
config.set('Spectrum conditioning','spectrum, maximum parent charge',	'4')
config.set('Spectrum conditioning','spectrum, minimum parent', 'm+h	500')
config.set('Spectrum conditioning','spectrum, minimum fragment mz',	'150')
config.set('Spectrum conditioning','spectrum, minimum peaks', '15')
config.set('Spectrum conditioning','spectrum, threads',	'6')

config.add_setion('Residue modification')
config.set('Residue modification', 'residue, modification mass', '57.021464@C')
config.set('Residue modification', 'residue, potential modification mass', '15.994915@M')

config.add_section('Protein general')
config.set('Protein general', 'protein, taxon', 'human')
config.set('Protein general', 'protein, cleavage site', '[RK]|{P}')
config.set('Protein general', 'protein, N-terminal residue modification mass', '0')
config.set('Protein general', 'protein, C-terminal residue modification mass', '0')

config.add_section('Scoring')
config.set('Scoring', 'scoring, minimum ion count', '4')
config.set('Scoring', 'scoring, maximum missed cleavage sites', '1')

config.add_section('model refinement paramters')
config.set('model refinement paramters', 'refine', 'yes')
config.set('model refinement paramters', 'refine, spectrum synthesis',	'yes')
config.set('model refinement paramters', 'refine, maximum valid expectation value', '0.1')
config.set('model refinement paramters', 'refine, potential N-terminus', 'modifications')
config.set('model refinement paramters', 'refine, potential C-terminus', 'modifications')
config.set('model refinement paramters', 'refine, unanticipated cleavage', 'yes')
config.set('model refinement paramters', 'refine, potential modification mass', '15.994915@M,0.9848@N,0.9848@Q')
config.set('model refinement paramters', 'refine, use potential modifications for full refinement', 'no')
config.set('model refinement paramters', 'refine, point mutations', 'no')

config.add_section('Output')
config.set('Output', 'output, path', 'output.xml')

config.add_section('Paths')
config.set('Paths', 'list path, taxonomy information', 'taxonomy.xml')
config.set('Paths', 'list path, default parameters', 'default_input.xml')
config.set('Paths', 'spectrum, path', 'input.xml')

config.add_section('Directory')
config.set('Directory', 'input directory path', 'C:\\Users\\moghb\\OneDrive\\Documents\\PXD002412')
config.set('Directory', 'output directory path', 'C:\\Users\\moghb\\OneDrive\\Documents\\Output')
config.set('Directory', 'tandem directory path', 'C:\\Users\\moghb\\Downloads\\tandem-win-17-02-01-4\\tandem-win-17-02-01-4\\tandem-win-17-02-01-4')

with open('C:\\Users\\moghb\OneDrive\\Documents\\config.ini', 'w') as configfile:    # save
    config.write(configfile)