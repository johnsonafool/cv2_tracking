print('hi')

from deep_sort_realtime.deepsort_tracker import DeepSort

tracker = DeepSort(max_age=30, nn_budget=70, override_track_class=None)
bbs = object_detector.detect(frame)
tracks = tracker.update_tracks(bbs, frame=frame)
for track in tracks:
   track_id = track.track_id
   ltrb = track.to_ltrb()
