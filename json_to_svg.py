import json
from utils import st_dist
import os
from svgwrite import Drawing


def file_to_vector_arrays(fileName):
    print('reading file into vector arrays')
    stroke_array = []
    with open(f"assets/{fileName}", "r") as file:
        stroke_array = [line.strip() for line in file]
        stroke_array = stroke_array[0]
        stroke_array = json.loads(stroke_array)
    return stroke_array


def strokes_to_drawing(type, i, strokes, stroke_width=5):
    print('converting stroke arrays to drawing objects')
    # Create an SVG drawing
    drawing = Drawing(f"assets/svg_output/{type}/{i}.svg", profile='tiny')
    # get points from strokes
    for stroke in strokes:
        points = []
        # iterate over points
        for i in range(len(stroke[0])):
            points.append((stroke[0][i], stroke[1][i]))
        # attach points to drawing
        drawing.add(
            drawing.polyline(
                points=points,
                fill="none",
                stroke="black",
                stroke_width=stroke_width
            )
        )
    return drawing


def vector_arrays_to_drawings(n, type, vectors, stroke_dist):
    print('converting arrays to drawing objects')
    # Create the output folder if it doesn't exist
    os.makedirs(f"assets/svg_output/{type}", exist_ok=True)
    drawings = []
    # limit to n outputs
    for i in range(n):
        drawings.append(strokes_to_drawing(
            type, i, vectors[i], stroke_width=stroke_dist[i]
        ))
    return drawings


def nd_to_json(names):
    for name in names:
        drawings = []
        with open(f"assets/{name}.ndjson", "r") as file:
            vectors = file.read().replace('\n', '')
            vectors = json.loads(vectors)
            for vector in vectors:
                drawings.append(vector['drawing'])
        with open(f"assets/{name}.json", "w") as file:
            file.write(json.dumps(drawings))


def main():
    jsons = ['anvil', 'baseball bat', 'bathtub', 'bee', 'bird', 'arm']
    stroke_dist = st_dist(500, min=1, max=20, dec=1)
    for json in jsons:
        # read vectors
        vector_arrays = file_to_vector_arrays(f'{json}.json')
        # save them to svg
        drawings = vector_arrays_to_drawings(
            500, json, vector_arrays, stroke_dist)
        for drawing in drawings:
            drawing.save()


if __name__ == "__main__":
    main()
