from pyswip import Prolog

class Recommender():
    def __init__(self):
        self.knowledge_base = Prolog()
        self.create_rules()

    def create_rules(self):
        """
        Insert rules into knowledge base
        """
        # If time available is less than an hour
        self.knowledge_base.assertz("recommend(0, _, sensitive, small, '30_30_sensitive')")
        self.knowledge_base.assertz("recommend(0, _, sensitive, medium, '30_30_sensitive')")
        self.knowledge_base.assertz("recommend(0, _, sensitive, large, '45_30_sensitive')")
        self.knowledge_base.assertz("recommend(0, _, normal, small, '30_40_normal')")
        self.knowledge_base.assertz("recommend(0, _, normal, medium, '30_40_normal')")
        self.knowledge_base.assertz("recommend(0, _, normal, large, '45_40_normal')")
        self.knowledge_base.assertz("recommend(0, _, heavy, small, '30_60_heavy')")
        self.knowledge_base.assertz("recommend(0, _, heavy, medium, '30_60_heavy')")
        self.knowledge_base.assertz("recommend(0, _, heavy, large, '45_60_heavy')")
        # If time available is less than two hours
        self.knowledge_base.assertz("recommend(1, _, sensitive, small, '60_30_sensitive')")
        self.knowledge_base.assertz("recommend(1, _, sensitive, medium, '60_30_sensitive')")
        self.knowledge_base.assertz("recommend(1, _, sensitive, large, '90_30_sensitive')")
        self.knowledge_base.assertz("recommend(1, _, normal, small, '60_40_normal')")
        self.knowledge_base.assertz("recommend(1, _, normal, medium, '60_40_normal')")
        self.knowledge_base.assertz("recommend(1, _, normal, large, '90_40_normal')")
        self.knowledge_base.assertz("recommend(1, _, heavy, small, '60_60_heavy')")
        self.knowledge_base.assertz("recommend(1, _, heavy, medium, '60_60_heavy')")
        self.knowledge_base.assertz("recommend(1, _, heavy, large, '90_60_heavy')")
        # If time available is three or more hours
        self.knowledge_base.assertz("recommend(2, _, sensitive, small, '120_30_sensitive')")
        self.knowledge_base.assertz("recommend(2, _, sensitive, medium, '120_30_sensitive')")
        self.knowledge_base.assertz("recommend(2, _, sensitive, large, '180_30_sensitive')")
        self.knowledge_base.assertz("recommend(2, _, normal, small, '120_40_normal')")
        self.knowledge_base.assertz("recommend(2, _, normal, medium, '120_40_normal')")
        self.knowledge_base.assertz("recommend(2, _, normal, large, '180_40_normal')")
        self.knowledge_base.assertz("recommend(2, _, heavy, small, '120_60_heavy')")
        self.knowledge_base.assertz("recommend(2, _, heavy, medium, '120_60_heavy')")
        self.knowledge_base.assertz("recommend(2, _, heavy, large, '180_60_heavy')")

    def recommend(self, query):
        """
        Returns a recommendation based on the rules of the knowledge base, when presented with an appropriate query
        """
        for recommendation in self.knowledge_base.query(query):
            return recommendation['Recommendation'].split('_')