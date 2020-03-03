import cv2
import tensorflow as tf

from absl import app, flags, logging
from absl.flags import FLAGS

from yolov3_tf2.models import YoloV3
from yolov3_tf2.dataset import transform_images
from yolov3_tf2.utils import draw_outputs
from tp_cnn import exo1, exo2, exo3

flags.DEFINE_string('classes', './data/coco.names', 'path to classes file')
flags.DEFINE_string('weights', './checkpoints/yolov3.tf',
                    'path to weights file')
flags.DEFINE_boolean('tiny', False, 'yolov3 or yolov3-tiny')
flags.DEFINE_integer('size', 416, 'resize images to')
flags.DEFINE_string('video', './data/C0089.MP4',
                    'path to video file or number for webcam)')
flags.DEFINE_boolean('display_output', False, 'display results in window')
flags.DEFINE_boolean('write_output', True, 'write results to video')
flags.DEFINE_string('output', 'data/result.avi', 'path to output video')
flags.DEFINE_string('output_format', 'XVID', 'codec used in VideoWriter when saving video to file')
flags.DEFINE_integer('num_classes', 80, 'number of classes in the model')


def init_yolo():
    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
    yolo = YoloV3(classes=FLAGS.num_classes)
    yolo.load_weights(FLAGS.weights)
    print("Weights loaded")
    return yolo


def init_writer(cap):
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    codec = cv2.VideoWriter_fourcc(*FLAGS.output_format)
    out = cv2.VideoWriter(FLAGS.output, codec, fps, (width, height))
    return out


def convert_frame_to_tf(frame):
    frame_in = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_in = tf.expand_dims(frame_in, 0)
    frame_in = transform_images(frame_in, FLAGS.size)
    return frame_in


def main_loop(yolo, class_names, cap, writer, object_tracker, luggage_tracker):
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_in = convert_frame_to_tf(frame)

        boxes, scores, classes, nums = yolo.predict(frame_in)
        boxes, scores, classes, nums = boxes[0], scores[0], classes[0], nums[0]

        # Exercice 1 (tp_cnn/exo1.py)
        # Implémenter la fonction filter_detections, cette fonction prend en entrée les résultats de la détection par
        # YOLO et retourne uniquement ceux des classes "person" et "suitcase" dont le score est supérieur à 0.5
        f_boxes, f_scores, f_classes, f_nums = exo1.filter_detections(boxes, scores, classes, nums, class_names)

        # Exercice 2 (tp_cnn/exo2.py)
        # Implémenter la classe Object Tracker qui permettra d'assigner une identité temporelle aux objets détectés
        tracked_objects = object_tracker.update(f_boxes, f_classes, class_names)

        # Exercice 3 (tp_cnn/exo3.py)
        # Implémenter la classe Luggage Tracker qui permettra de déterminer si un baggage a été abandonné
        unattended_luggage = luggage_tracker.update(tracked_objects)

        if any([FLAGS.write_output, FLAGS.display_output]):
            if not tracked_objects:
                frame = draw_outputs(frame, (boxes, scores, classes, nums), class_names)
            else:
                object_tracker.draw_tracked_objects(frame)
            if unattended_luggage:
                luggage_tracker.draw_alert(frame)

        if FLAGS.write_output:
            writer.write(frame)

        if FLAGS.display_output:
            cv2.imshow("Result", frame)
            k = cv2.waitKey(1)
            if k % 256 == ord('q'):
                break


def main(_argv):
    yolo = init_yolo()
    class_names = [c.strip() for c in open(FLAGS.classes).readlines()]
    cap = cv2.VideoCapture(FLAGS.video)
    if FLAGS.write_output:
        writer = init_writer(cap)
    else:
        writer = None
    if FLAGS.display_output:
        cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
    object_tracker = exo2.ObjectTracker()
    luggage_tracker = exo3.LuggageTracker(150)
    main_loop(yolo, class_names, cap, writer, object_tracker, luggage_tracker)

    cap.release()
    if FLAGS.display_output:
        cv2.destroyAllWindows()
    if FLAGS.write_output:
        writer.release()


if __name__ == '__main__':
    app.run(main)
