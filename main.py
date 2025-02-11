# main.py
import os
from dotenv import load_dotenv
import sys

# Add project root to sys.path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

load_dotenv()

from vitalik_ai import VitalikAI
import json
from rag.rag import VitalikKAG  # Import KAG
from observability.metrics import metrics

# Initialize components
vitalik_ai = VitalikAI()


def mock_data_collection():
    with open('data/raw_data.json', 'r') as f:
        raw_data = json.load(f)
    return raw_data

def mock_data_cleaning(raw_data):
    cleaned_data = []
    for item in raw_
        text = item['text'].lower().strip()  # Basic cleaning
        cleaned_data.append({'source': item['source'], 'date': item['date'], 'text': text})

    with open('data/cleaned_data.json', 'w') as f:
        json.dump(cleaned_data, f, indent=2)
    return cleaned_data

def mock_knowledge_graph_creation(cleaned_data):
    knowledge_graph = {
        "nodes": [
            {"id": "ethereum", "label": "Ethereum"},
            {"id": "layer2", "label": "Layer 2 Scaling"},
            {"id": "optimism", "label": "Optimism"},
            {"id": "zkrollups", "label": "ZK-rollups"},
            {"id": "decentralization", "label": "Decentralization"},
            {"id": "account_abstraction", "label": "Account Abstraction"}
        ],
        "edges": [
            {"source": "ethereum", "target": "layer2", "relation": "uses"},
            {"source": "layer2", "target": "optimism", "relation": "is_a"},
            {"source": "layer2", "target": "zkrollups", "relation": "is_a"},
            {"source": "ethereum", "target": "decentralization", "relation": "promotes"},
            {"source": "ethereum", "target": "account_abstraction", "relation": "benefits"}
        ]
    }
    with open('knowledge_graph/vitalik_graph.json', 'w') as f:
        json.dump(knowledge_graph, f, indent=2)
    return knowledge_graph

# Data initialization (run once)
raw_data = mock_data_collection()
cleaned_data = mock_data_cleaning(raw_data)
knowledge_graph = mock_knowledge_graph_creation(cleaned_data)  # KG created once at server start

# Initialize KAG with the created knowledge graph
kag = VitalikKAG(knowledge_graph=knowledge_graph)

#Removed Flask server endpoints

if __name__ == '__main__':
    #Example use of KAG and metrics
    query = "Tell me about Layer 2"
    context = kag.retrieve_context(query)
    tweet = kag.generate_tweet_response(query, context)
    metrics.increment_query_count()
    print(f"Example KAG query: {query}\nGenerated Tweet: {tweet}\nContext: {context}")
    print(f"Current Query Count: {metrics.get_query_count()}")
