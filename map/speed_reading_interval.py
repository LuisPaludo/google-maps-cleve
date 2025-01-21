from typing import List

class JamInfo:
    def __init__(self, start_polyline_point_index: int, end_polyline_point_index: int, speed: str):
        self.start_polyline_point_index = start_polyline_point_index
        self.end_polyline_point_index = end_polyline_point_index
        self.speed = speed

    def __repr__(self) -> str:
        return (f"JamInfo("
                f"start_polyline_point_index={self.start_polyline_point_index}, "
                f"end_polyline_point_index={self.end_polyline_point_index}, "
                f"speed='{self.speed}')")
    

def parse_speed_reading_intervals(data: List[dict]) -> List[JamInfo]:
    return [
        JamInfo(
            item['startPolylinePointIndex'],
            item['endPolylinePointIndex'],
            item['speed']
        ) for item in data
    ]