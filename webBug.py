import urllib
import regex


#String -> String
def file_input(filepath):
    h = open (filepath,"r")
    g = h.readline()
    l = h.read()
    h.close()
    h = open (filepath,"w")
    h.truncate()
    h.write(l)
    h.flush()
    h.close()
    return g

def mapf(lines):
    ret = []
    for x in lines:
        ret.append(x+"\n")
    return ret
#String->[String]->Nothing
def file_output(filepath,lines):
    h = open (filepath,"a")
    h.writelines(mapf(lines))
    h.flush()
    h.close()
#String -> String
def getHtml(url):
    print url
    try:
        page = urllib.urlopen(url)
    except IOError:
        print "*****Invalid Http*****\n"
        return ""
    else:
        return page.read()

    
nextwebfile = "nextweb"
nextwebrule = []

#Tuple(String,String) -> [String]
def getNextWeb(content):
    global nextwebfile
    global nextwebrule
    if(nextwebrule == []):
        h = open (nextwebfile)
        nextwebruleScript = h.read()
        nextwebrule = regex.ruleScript(nextwebruleScript.split('\n'))
        h.close()
    return  regex.regApply(content,nextwebrule)
    


#String

historyfile = "history"

#[String]->[String]->[String]
def filter_(rule,source):
    for arule in rule:
        for target in source:
            if(target == arule):
                source.remove(target)

    return source

def monoize(source):
    filter_(source,source)

#String->Nothing
def historyRecord(history_):
    global historyfile
    h = open(historyfile,"r")
    r = h.read()
    h.close()
    h = open(historyfile,"w")
    h.write(r + "\n")
    h.write(history_+"\n")
    h.flush()
    h.close()

def startBug(startwebfile,function):
    h = open(historyfile)
    r = h.readlines()
    h.close()
    _startBug(startwebfile,function,r)

def rmret(url):
    x = url.split("\n")
    ret = ""
    for y in x:
        ret = ret + y
    return ret
    
#String->((String,String)->b)->[String]->Nothing
def _startBug(startwebfile,function,history):
    i = file_input (startwebfile)
    while(i):
        url =rmret(i)
        
        x = (url,getHtml(url))
        y = filter_(history,getNextWeb(x))
        print "nextweb:"
        print y
        function(x)
        historyRecord(url)
        
        history.append(url)
        print "history:"
        print history
        if(y != None):
            file_output (startwebfile,y)
        i  = file_input (startwebfile)
