import json


def create_cube_order_dto(cube_order):
    cubes = []

    for cube in cube_order:
        cube_position = cube.get_target_zone_position()
        cube_position = [int(cube_position.x), int(cube_position.y)]
        cube_color = cube.get_color().value
        cubes.append({'cube position': cube_position,
                      'cube color': cube_color})

    return json.dumps({"cubes": cubes})
