import pysolr

# Configure connection to Apache solr
solr_homedepo = pysolr.Solr('http://localhost:8983/solr/homedepo')

def search_function(core, query, rows = 12 ):
    results = core.search(query, rows = rows)
    return results
