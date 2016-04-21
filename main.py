from webBug import *
from regex import *

startwebfile = "queue"
rulefile = "rule"
outputfile = "output"
#nextwebfile = "nextweb"


#nextwebrule = []
rule = []

#webBug.startBug(startwebfile,targetf)


#(String,String)->Nothing
def targetf(content):
    global rule
    global rulefile
    if (rule == []):
        h = open (rulefile)
        ruleS = h.read()
        h.close()
        rule = ruleScript(ruleS.split('\n'))
    output_ =beam(regApply(content,rule))
    h = open(outputfile,"r+")
    h.write(output_)
    h.close()

startBug(startwebfile,targetf)
    
