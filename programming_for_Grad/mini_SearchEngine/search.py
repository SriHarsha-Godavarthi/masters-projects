#import string module
import string

def cleanToken(token):
    # clean the puntuations from start and end of each token
    punctuations_char=string.punctuation
    #strip will trim punctuations
    cleaned_token=token.strip(punctuations_char)
    # return the token after removing punctuations
    return cleaned_token

def buildInvertedIndex(docs):
    #build inverted index from word to url's mapping
    keyWords=[]
    # get the pages to process for inverted index
    urls=docs.keys()
    # create empty index
    inverted_index=dict()
    for url in urls:
        #get the tokens for each website(url)
        #loop individual tokens and create index's if not present
        #if token is already present in index then add url to the value of key
        tokens = docs[url]
        for token in tokens:
            #check if token is present in index
            if inverted_index.get(token)== None:
                #create new record for token's not in index
                inverted_index[token]=set([url])
            else:
                #update exsisting record
                inverted_index[token]=(inverted_index[token].union(set([url])))
            
        #return inverted index
    return inverted_index

def findQueryMatches(index, query):
    #To find search results from processed index
    search_result=set([])
    search_terms=index.keys()
    # split query into different tokens
    # get result for each token do operations based on query and then return final result
    for term in (query.split(" ")):
        # if term in search_terms:
            if not term.startswith("-"):
                #if query doesn't have any removing token the only append
                term_result=index[(cleanToken(term))]
                search_result=search_result.union(term_result)
            else:
                # if query want to exclude result's to certain token exclude using set difference
                term_result=index[(cleanToken(term))]
                search_result=search_result.difference(term_result)
    return search_result

def readDocs(dbfile):
    #open text file to read
    opened_file = open(dbfile, mode="r",encoding="utf8")
    #remove the converted characters spaces and tabs
    file_content=opened_file.read().replace("\xa0"," ").replace("\t"," ")
    #filter and remove empty keywords
    file_content=list(filter(lambda item: item !="",file_content.split("\n")))
    urls={}
    pageBody = ""
    url=""
    # read line by line and create mapping from url to keywords
    for line in file_content:
        if (line.startswith("https:") or line.startswith("http:")):
            #store url for the page
            if url=="":
             url=line
        elif line.__contains__("<endPageBody>"):
            #get keywords from page body of webpage
            tokens=[]
            # add tokens in pageBody to index with key as site url
            for token in (pageBody.lower().split(" ")):
                #process each token
                token=cleanToken(token)
                if token!="":
                     tokens.append(token)
            urls[url]= set(tokens)
            pageBody=""
            url=""
        elif line=="<pageBody>":
            #if page body starts don't add it to keywords
            continue
        else:
            # if pageBodyEnd is not found keep on adding data to pageBody
            pageBody+=line
        # returns the forward index
    return urls

    

def mySearchEngine(dbPath):
    # Read and process the database file
        #Take input
        query = input("Enter query sentence (RETURN/ENTER to quit): ")
        query=query.strip(" ").lower()
        if query!="":
            #create forward index
            mapping_urls=readDocs(dbPath)
            #create backward index from forward index
            invertedIndex=buildInvertedIndex(mapping_urls)
            # Perform the query and display the results
            matches = findQueryMatches(invertedIndex, query)
            # display search result
            print(f"Found {len(matches)} matching pages")
            print(matches)
        return query

        
if __name__ == "__main__":
    while (True):
        query=mySearchEngine("./data_base/sampleWebsiteData.txt")
        if query=="":
            break