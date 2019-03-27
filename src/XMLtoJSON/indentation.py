"""
indentation

To indentation json documents

@author Adonis & Tom
"""
import json

your_json = '{"IMG_20180413_102955.jpg": {"filename": "IMG_20180413_102955.jpg", "regions": {"0": {"region_attributes": {"damage": "damage"}, "shape_attributes": {"all_points_x": [1435, 1493, 1551, 1551, 1551, 1493, 1435, 1435, 1435], "all_points_y": [1366, 1366, 1366, 1420, 1475, 1475, 1475, 1420, 1366]}, "name": "polygon"}}, "size": 2491619}, "IMG_20180413_103358.jpg": {"filename": "IMG_20180413_103358.jpg", "regions": {"0": {"region_attributes": {"damage": "damage"}, "shape_attributes": {"all_points_x": [1248, 1283, 1319, 1319, 1319, 1283, 1248, 1248, 1248], "all_points_y": [2004, 2004, 2004, 2041, 2079, 2079, 2079, 2041, 2004]}, "name": "polygon"}}, "size": 1746576}, "IMG_20180413_103507.jpg": {"filename": "IMG_20180413_103507.jpg", "regions": {"0": {"region_attributes": {"damage": "damage"}, "shape_attributes": {"all_points_x": [3082, 3113, 3144, 3144, 3144, 3113, 3082, 3082, 3082], "all_points_y": [1025, 1025, 1025, 1052, 1079, 1079, 1079, 1052, 1025]}, "name": "polygon"}}, "size": 1777318}, "IMG_20180413_103401.jpg": {"filename": "IMG_20180413_103401.jpg", "regions": {"0": {"region_attributes": {"damage": "damage"}, "shape_attributes": {"all_points_x": [2197, 2242, 2288, 2288, 2288, 2242, 2197, 2197, 2197], "all_points_y": [2269, 2269, 2269, 2306, 2344, 2344, 2344, 2306, 2269]}, "name": "polygon"}}, "size": 1905208}, "IMG_20180413_103404.jpg": {"filename": "IMG_20180413_103404.jpg", "regions": {"0": {"region_attributes": {"damage": "damage"}, "shape_attributes": {"all_points_x": [3363, 3392, 3422, 3422, 3422, 3392, 3363, 3363, 3363], "all_points_y": [1275, 1275, 1275, 1303, 1332, 1332, 1332, 1303, 1275]}, "name": "polygon"}}, "size": 1730852}, "IMG_20180413_103354.jpg": {"filename": "IMG_20180413_103354.jpg", "regions": {"0": {"region_attributes": {"damage": "damage"}, "shape_attributes": {"all_points_x": [1502, 1531, 1561, 1561, 1561, 1531, 1502, 1502, 1502], "all_points_y": [1454, 1454, 1454, 1487, 1521, 1521, 1521, 1487, 1454]}, "name": "polygon"}}, "size": 1741984}, "IMG_20180413_103206.jpg": {"filename": "IMG_20180413_103206.jpg", "regions": {"0": {"region_attributes": {"damage": "damage"}, "shape_attributes": {"all_points_x": [1377, 1446, 1515, 1515, 1515, 1446, 1377, 1377, 1377], "all_points_y": [2225, 2225, 2225, 2316, 2408, 2408, 2408, 2316, 2225]}, "name": "polygon"}}, "size": 1660801}}'
parsed = json.loads(your_json)

print(json.dumps(parsed, indent=4, sort_keys=True))

   