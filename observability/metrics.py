class Metrics:
    def __init__(self):
        self.query_count = 0

    def increment_query_count(self):
        self.query_count += 1

    def get_query_count(self):
        return self.query_count

metrics = Metrics() #Singleton instance