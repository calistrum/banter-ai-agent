import json
import os
import openai

class VitalikKAG:
    def __init__(self, knowledge_graph=None, knowledge_graph_path="knowledge_graph/vitalik_graph.json"):
        if knowledge_graph:
            self.knowledge_graph = knowledge_graph
        else:
            with open(knowledge_graph_path, 'r') as f:
                self.knowledge_graph = json.load(f)
        openai.api_key = os.getenv("OPENAI_API_KEY")  # Retrieve API key securely

    def retrieve_context(self, query):
        # Find nodes related to keywords in the query
        relevant_nodes = []
        query_words = query.lower().split()  # Split query into words

        for node in self.knowledge_graph['nodes']:
            node_words = node['label'].lower().split()  # Split node label
            for word in node_words:
                if word in query_words:
                    relevant_nodes.append(node)
                    break  # Avoid adding the same node multiple times

        # Add connected nodes
        for edge in self.knowledge_graph['edges']:
            if edge['source'] in [n['id'] for n in relevant_nodes]:
                target_node = next((node for node in self.knowledge_graph['nodes'] if node['id'] == edge['target']), None)
                if target_node and target_node not in relevant_nodes:
                    relevant_nodes.append(target_node)
            if edge['target'] in [n['id'] for n in relevant_nodes]:
                source_node = next((node for node in self.knowledge_graph['nodes'] if node['id'] == edge['source']), None)
                if source_node and source_node not in relevant_nodes:
                    relevant_nodes.append(source_node)

        # Return connected nodes and edges as context
        context = {"nodes": relevant_nodes, "edges": []}
        edges = []
        for edge in self.knowledge_graph['edges']:
            if edge['source'] in [n['id'] for n in relevant_nodes] or \
                    edge['target'] in [n['id'] for n in relevant_nodes]:
                if edge not in edges:  # avoid duplicates
                    edges.append(edge)
        context['edges'] = edges
        return context

    def generate_tweet_response(self, query, context):
        # Use OpenAI Chat API to generate a tweet-length response
        try:
            context_str = json.dumps(context)  # Convert context to a string

            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are Vitalik Buterin. Given the following information extracted from a knowledge graph: {context_str}, generate a tweet-length response (140 characters max) to the query: {query}."},
                    {"role": "user", "content": query}
                ],
                max_tokens=100,  # Reduced max tokens to ensure tweet length.  Experiment with this!
                temperature=0.7,
                n=1,
                stop=None
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error generating response: {e}"

# Example usage (for testing rag.py independently)
if __name__ == '__main__':
    # Create a sample knowledge graph (replace with your actual graph)
    sample_knowledge_graph = {
        "nodes": [{"id": "node1", "label": "Example Node 1"}],
        "edges": []
    }
    kag = VitalikKAG(knowledge_graph=sample_knowledge_graph)
    queries = [
        "Tell me about Example Node 1 in 140 chars",
        "What is Layer 2?",
        "Explain ZK-rollups",
        "Ethereum and decentralization",
        "Account Abstraction benefits"
    ]
    for query in queries:
        context = kag.retrieve_context(query)
        response = kag.generate_tweet_response(query, context)
        print(f"Query: {query}")
        print(f"Context: {context}")
        print(f"Response: {response}")
        print("-" * 20)
