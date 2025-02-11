from flask import Flask, render_template, request
import sys
import os
import json

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from rag.rag import VitalikKAG
from observability.metrics import metrics

app = Flask(__name__)

# Load the knowledge graph
with open(os.path.join(project_root, 'knowledge_graph/vitalik_graph.json'), 'r') as f:
    knowledge_graph = json.load(f)

# Initialize KAG with the loaded knowledge graph
print(f"KG {knowledge_graph}")
kag = VitalikKAG(knowledge_graph=knowledge_graph)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        print(f"Query {query}")
        context = kag.retrieve_context(query)
        print(f"Context {context}")
        response = kag.generate_tweet_response(query, context) # Corrected method name
        metrics.increment_query_count()  # Update query count
        return render_template('index.html', query=query, response=response, context=context)
    else:
        return render_template('index.html', query='', response='', context={})

@app.route('/observability')
def observability():
    query_count = metrics.get_query_count()
    return render_template('observability.html', query_count=query_count)

import os

if __name__ == '__main__':
    port = int(os.getenv("FLASK_RUN_PORT", 8080))  # Use env var or default to 8080
    app.run(host="0.0.0.0", port=port, debug=True)
