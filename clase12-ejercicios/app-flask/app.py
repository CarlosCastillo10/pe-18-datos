"""
tomado de: https://gist.github.com/leplatrem/1277655
"""
import simplejson
from flask import Flask, g, request
from couchdb.design import ViewDefinition
import flaskext.couchdb


app = Flask(__name__)

"""
CouchDB permanent view
"""
docs_by_author = ViewDefinition('docs', 'byauthor', 
                                'function(doc) { emit(doc.anio_mad, doc);}')

"""
Retrieve docs
"""
@app.route("/<author_id>/docs")
def docs(author_id):
    docs = []
    print "--------------------"
    # print docs_by_author(g.couch)
    # for row in docs_by_author(g.couch)[author_id]:
    for row in docs_by_author(g.couch):
	print row.value['anio_mad'], author_id, row.value['anio_mad'] == author_id
	print row.value['anio_mad'].__class__, author_id.__class__
	try:
	    author_id = int(author_id)
		
	    if row.value['anio_mad'] == author_id:        
	        docs.append(row.value)
                print row.value
	except:
	    pass
    return simplejson.dumps(docs)


"""
Flask main
"""
if __name__ == "__main__":
    app.config.update(
        DEBUG = True,
        COUCHDB_SERVER = 'http://admin:11112222@localhost:5984/',
        COUCHDB_DATABASE = 'nacimientos'
    )
    manager = flaskext.couchdb.CouchDBManager()
    manager.setup(app)
    manager.add_viewdef(docs_by_author)  # Install the view
    manager.sync(app)
    app.run(host='0.0.0.0', port=5000)
