import math


class QuerySearch:
    """ Searches similarity of query image vector with extracted vectors from database"""

    def __init__(self, queryFeature, features):

        self.features = features
        self.queryFeature = queryFeature

    def __cosine_similarity(self, queryVector, vector):
        # Computes cosine similarity between two vectors

        eps = 1e-10
        dot_product = sum(q*v for q, v in zip(queryVector, vector))

        queryMagnitude = math.sqrt(sum([val**2 for val in queryVector]))
        vectorMagnitude = math.sqrt(sum([val**2 for val in vector]))
        magnitude = (queryMagnitude*vectorMagnitude)+eps

        if not magnitude:
            return 0

        cosine_similarity = round(dot_product/magnitude, 5)
        return cosine_similarity

    def __chi2_distance(self, queryVector, vector):
        # Computes chi-square distance between two vectors

        eps = 1e-10
        dists = [((q - v) ** 2) / (q + v + eps)
                 for (q, v) in zip(queryVector, vector)]
        chi2_distance = 0.5 * sum(dists)
        chi2_distance = round(chi2_distance, 5)
        return chi2_distance

    def __SAD_distance(self, queryVector, vector):
        # Computes SAD distance between two vectors

        dists = [abs(q-v) for (q, v) in zip(queryVector, vector)]
        SAD_distance = sum(dists)
        return SAD_distance

    def performSearch(self):
        # Return similarity indices of queryVector and databse images

        searchSimilarityScores = []

        for image in self.features:
            queryVector = self.queryFeature
            vector = self.features[image]
            cosine_similarity = self.__chi2_distance(queryVector, vector)

            searchSimilarityScores.append((image, cosine_similarity))

        return searchSimilarityScores
