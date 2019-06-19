def pathToFile(site):
    if isFile(site):
        return site
    bs = getBaseUrl(site)
    ext = "index.html"    
    if isPHPIndex(site):        
    ext = "index.php"   
 return "%s/%s" % (bs,ext)
