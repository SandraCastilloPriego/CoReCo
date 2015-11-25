#!/usr/bin/env python
"""
Author: M. Fahad Syed (fahad.syed@vtt.fi)
"""



import os
import sys
import subprocess
import operator
import traceback
import time
sys.path.append("..")
import ScriptsDir

import NGS_Util


class NGS_IPRScan:
    
    iprscanDir = ScriptsDir.IprscanDir
    iprscan    = iprscanDir + "iprscan -cli "
    converter  = "perl "  + iprscanDir + "converter.pl " 

    iprscan5    = iprscanDir + "interproscan.sh "
    
    def protein_iprscan_to_raw_output(self, inputFile, outputFile):
        
        try:

            call = self.iprscan + " -i "   + inputFile + " -o " + outputFile + " -format raw -goterms -iprlookup "

            NGS_Util.executeCall(call)

#            NGS_Util.executeThreadedCall(call)
                  
        except Exception:
            print traceback.print_exc()
            
    def protein_iprscan_to_xml_output(self, inputFile, outputFile):
        
        try:

            call = self.iprscan + " -i "   + inputFile + " -o " + outputFile + " -goterms -iprlookup "

            NGS_Util.executeCall(call)

#            NGS_Util.executeThreadedCall(call)
                  
        except Exception:
            print traceback.print_exc()
            
    
    def convert_raw_xml(self, inputFile, outputFile):
        
        try:
            
            call = self.converter + " -format xml -input " + inputFile + " -output " + outputFile
            
            NGS_Util.executeCall(call)
            
        except Exception:
            
            print traceback.print_exc()

    ############################################################################################################################################################
    
    
    def protein_iprscan5_to_xml_output(self, inputFile, outputFile):
        
        try:

            call = self.iprscan5 + " -i "   + inputFile + " -o " + outputFile + " -f XML -goterms -iprlookup "

            NGS_Util.executeCall(call)

                  
        except Exception:
            print traceback.print_exc()
            
    
    def convert_iprscan5_xml_raw(self, inputFile, outputFile):
        
        try:
            
            call = self.iprscan5 + " -mode convert -i " + inputFile + " -f RAW -o " + outputFile
            
            NGS_Util.executeCall(call)
            
        except Exception:
            
            print traceback.print_exc()

