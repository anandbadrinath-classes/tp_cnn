# Exercice 3 (tp_cnn/exo3.py)
# Implémenter la classe Luggage Tracker qui permettra de déterminer si un baggage a été abandonné
import cv2

class LuggageItem:

    def __init__(self, luggage_id):
        self.luggage_id = luggage_id
        self.is_unattended = False
        self.frames_alone = 0
        self.is_alert = False


class LuggageTracker:

    def __init__(self, unattended_frame_threshold=150, unattended_distance_threshold=200):
        self.tracked_luggage = {}
        self.unattended_frame_threshold = unattended_frame_threshold
        self.unattended_distance_threshold = unattended_distance_threshold

    # Exercice 3.1 Implémenter la méthode add new luggage qui prend en entrée les résultats du tracking et ajoute
    # tous les nouveaux baggages dans self.tracked_luggage
    def add_new_luggage(self, tracked_objects):
        pass


    # Exercice 3.2 Implémenter la méthode _calc_distance qui prend en entrée 2 bounding box et retourne la distance
    # entre leurs centres.
    def _calc_distance(self, box1, box2):
        return 0

    # Exercice 3.3 Implémenter la méthode self.update_current_luggage qui prend en entrée les résultats du tracking.
    # Et met à jour self.tracked_luggage de la manière suivante:
    # Pour chaque baggage:
    # - si la distance entre le baggage et la personne la plus proche est supérieure à
    #   self.unattended_frame_threshold alors le baggage est considéré comme abandonné (passer is_unattended à True)
    # - sinon le baggage est considéré comme non-abandonné (passer is_unattended à False et remettre frames_alone à 0)
    # Ensuite, pour chaque baggage abandonné incrémenter sa propriété frames_alone de 1
    # Enfin, si un baggage a été abandonné pendant plus de self.unattended_frame_threshold, il faut lever l'alerte
    #   (passer is_alert à True)
    def update_current_luggage(self, tracked_objects):
        pass

    def update(self, tracked_objects):
        self.add_new_luggage(tracked_objects)
        self.update_current_luggage(tracked_objects)
        return self.tracked_luggage

    # Exercice 3.4 Implémenter la méthode self.draw_alert qui prend en entrée une image (frame) et dessine un rectangle
    # rouge par dessus les baggages en alerte.
    def draw_alert(self, frame):
        pass

    # BONUS: Améliorer la méthode update_current luggage en faisant en sorte qu'un baggage ne puisse être asoocié qu'a
    # une seule personne. Le baggage est alors considéré comme abandonné à partir du moment où la personne associée
    # est à une distance supérieure à (self.unattended_distance_threshold) du baggage.
