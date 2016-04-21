import re


websitep = re.compile(r'(.*):::(.*)')
procedurep = re.compile(r'(.*)>>>>(.*)')

#[String] -> [(String,[Pattern])]
def ruleScript(sources):
    ret = []
    for x in sources:
        g = websitep.match(x)
        ga = g.group(1)
        gx = g.group(2)
        px = procedurep.match(gx)
        retp = []
        while(px != None):
            retp.append(re.compile(px.group(1)))
            gx = px.group(2)
            px = procedurep.match(gx)
        retp.append(re.compile(gx))
        ret.append((ga,retp))
    return ret
        

#String->Pattern->[String]
def reg_search_all(source,pattern):
    
    ret = []
    x = 0
    while x < len(source):
        k = pattern.match(source[x:])
        if(k!=None):
            ret.append(k.group())
        x = x + 1
    return ret

#[String]->String
def beam(stringlist):
    ret = ""
    for x in stringlist:
        ret = ret + x + '\n'
    return ret
        

#(String,String) -> [(String,[Pattern])] -> [String]
def regApply(target,rule):
    website = target[0]
    webcontexts = target[1].split('\n')
    for x in rule:
        if (x[0] == "default") or (re.search(x[0],website) != None) :
            patternlists = x[1]
            for p in patternlists:
                pa = reg_search_all(beam(webcontexts),p)
                webcontexts = pa

            break
    
    return webcontexts
            
