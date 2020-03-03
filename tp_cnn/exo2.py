# Exercice 2 (tp_cnn/exo2.py)
# Implémenter la classe Object Tracker qui permettra d'assigner une identité temporelle aux objets détectés
import cv2

class TrackedObject:
    max_id = 0

    @classmethod
    def new_id(cls):
        new_id = cls.max_id
        cls.max_id += 1
        return new_id

    def __init__(self, box, class_label, object_id=None):
        self.box = box
        self.class_label = class_label
        self.untracked_frames = 0
        if id is None:
            self.object_id = TrackedObject.new_id()
        else:
            self.object_id = object_id


class ObjectTracker:

    def __init__(self, iou_threshold=0.3, max_untracked_frames=10):
        self._tracked_objects = {}
        self.iou_threshold = iou_threshold
        self.max_untracked_frames = max_untracked_frames

    # Exercice 2.1
    # Implémenter la méthode _calc_iou qui prend en entrée 2 bounding box et retourne leur IOU (float)
    # IOU (Intersection Over Union): Le rapport entre l'aire de l'intersection et l'aire de l'union de deux rectangles
    def _calc_iou(self, box1, box2):
        # Ecrivez votre code ici, n'oubliez pas de remplacer le return 0 par le votre
        return 0

    # Exercice 2.2
    # Implémenter la méthode find_best_matches qui prend en entrée une liste de bounding box et la liste des classes
    # associées et calcule l'iou entre chacun des objets trackés et les nouvelles bounding box. Puis retourne les
    # associations objet tracké/bounding box les plus pertinentes sous la forme d'une liste de tuples et la liste des
    # bounding box qui n'ont pas été associées à un objet tracké.
    # détections, et trouve les paires (objet tracké, objet détecté) qui correspondent le mieux.
    # Un objet détecté est associé à un objet tracké si et seulement si:
    # 1. Ils ont tous les deux la même classe
    # 2. L'IOU entre la bounding box et l'objet tracké est supérieur à celui entre l'objet tracké et une autre
    # bounding box de la même classe
    # 3. L'IOU entre l'objet tracké et la bounding box est supérieur à self.iou_threshold
    def _find_best_matches(self, boxes, classes, class_names):
        return [], []

    # Exercice 2.3
    # Implémenter la méthode _make_new_tracked_object qui prend en entrée la liste des bounding box non associées
    # et crée un nouveau TrackedObject pour chacune. La définition de la classe TrackedObject se trouve en haut de ce
    # fichier. Le nouveau TrackedObject doit ensuite être stocké dans self.tracked_objects (self.tracked_objects est
    # défini comme un dictionnaire, mais vous pouvez utiliser la structure de données que vous souhaitez pour stocker
    # les objets trackés).
    def _make_new_tracked_objects(self, unmatched_boxes):
        pass

    # Exercice 2.4
    # Implémenter la méthode _update_tracked_objects qui prend en entrée la liste des associations les plus pertinentes
    # et met à jour self.tracked_objects qui stocke les objets trackés:
    #
    # Objets trackés existants: Pour les objects trackés déja présents dans le dictionnaire self.tracked_objects, mettre
    #                           à jour les propriétés suivantes:
    #                               - box: Si l'objet tracké est associé à une bounding box il faut remplacer la
    #                                      bounding box actuelle par la nouvelle
    #                               - untracked_frames: Si l'objet tracké est associé à une bounding box
    #                                                   untracked_frames passe à 0 sinon untracked_frames est
    #                                                   incrémenté de 1
    #                           Si un objet tracké a une valeur de untracked_frames supérieure à
    #                           self.max_untracked_frames il doit être supprimé du dictionnaire
    def _update_tracked_objects(self, best_matches):
        pass

    def update(self, boxes, classes, class_names):
        best_matches, unmatched_boxes = self._find_best_matches(boxes, classes, class_names)
        self._make_new_tracked_objects(unmatched_boxes)
        self._update_tracked_objects(best_matches)
        return self._tracked_objects

    # Exercice 2.5
    # Implémenter la méthode draw_tracked_objects qui prend en entrée une image frame et dessine dessus les bounding
    # box des objets trackés contenus dans self.tracked_objects et leur identifiant object_id.
    # utiliser les méthodes cv2.rectangle et cv2.putText
    def draw_tracked_objects(self, frame):
        pass
