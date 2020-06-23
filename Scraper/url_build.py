import sys


# Return list of URLS 
def build_url():
    # Check if search terms are provided as parameters
    if len(sys.argv) < 3:
        print(":Missing Mandatory Parameters:\n")
        print("PARAMS: \n")
        print("\t(mandatory) search-terms :: String of Space separated search terms enclosed in \"\". e.g. search-terms=\"Python Django\" \n")
        print("\t(mandatory) location :: One word location for job search. e.g. location=Delhi \n")
        print("\t(optional) depth :: Number of pages to search (default 14). e.g. depth=5 \n")
        raise SyntaxError


    print("Please Wait...")
    
    URL_DOMAIN = "https://www.naukri.com/"
    URL_PAGES = ""
    URL_TERMS = "?qp="
    URL_LOC = "&ql="


    LOCATION=""
    SEARCH_TERMS = []
    URLS = []
    DEPTH = 15



    # Extract command line keyword arguments and store it in variables
    for arg in sys.argv:
        k = arg.split("=")
        if k[0].lower() == "location":
            LOCATION= k[1].lower()+"%2C+&qf[]="
        if k[0].lower() == "search-terms":
            SEARCH_TERMS = k[1].split()
        if k[0].lower() == "depth":
            DEPTH = int(k[1])
        
    # Build fractions of the URL
    URL_PAGES =  "-".join(SEARCH_TERMS)+"-jobs-in-"+LOCATION
    URL_LOC += LOCATION
    URL_TERMS += ("+%2C+".join(SEARCH_TERMS)) 

    URLS.append( URL_DOMAIN+"/"+URL_PAGES+URL_TERMS+URL_LOC+"&qk[]=1&qs=f")
    # qk : 1 = Company posted, 2 = Consultancy Posted, 0 = All
    # qs : f = sort by date posted, r = sort by relevance
    for i in range(2,DEPTH):
            URLS.append(URL_DOMAIN+"/"+URL_PAGES+f'-{i}'+URL_TERMS+URL_LOC+"&qk[]=1&qs=f")

    return URLS

