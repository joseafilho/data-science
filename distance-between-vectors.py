"""
author: José Araújo
enterprise: FireCloud Services - fireclouds.com.br
email: joseafilho@gmail.com, josearaujo@fireclouds.com.br
create in: 28-08-2021
last update: 28-08-2021
"""

import math

vector_x = [0, 1, 2, 1, 0]
vector_z = [0, 1, 2, 1, 1]
vector_y = [0, 0, 1, 0, 0]

# calculate distance quadratic
# =ABS(A2-B2)+ABS(A3-B3)+ABS(A4-B4)+ABS(A5-B5)+ABS(A6-B6)
def calculate_distance_quadratic(vector1, vector2):
    distance = 0
    pos = 0
    length_vectors = len(vector1)

    while pos < length_vectors:
        distance += abs(vector1[pos] - vector2[pos])
        pos += 1
    
    return distance

# calculate distance euclidean
# =RAIZ((A2-B2)^2+(A3-B3)^2+(A4-B4)^2+(A5-B5)^2+(A6-B6)^2)
def calculate_distance_euclidean(vector1, vector2):
    distance = 0
    pos = 0
    length_vectors = len(vector1)

    while pos < length_vectors:
        distance += (vector1[pos] - vector2[pos]) ** 2
        pos += 1
    
    return round(math.sqrt(distance), 2)

distance_quadratic_between_vx_vz = calculate_distance_quadratic(vector_x, vector_z)
distance_quadratic_between_vx_vy = calculate_distance_quadratic(vector_x, vector_y)
distance_quadratic_between_vz_vy = calculate_distance_quadratic(vector_z, vector_y)

print('distance quadratic between vectorX and vectorZ: {}'.format(distance_quadratic_between_vx_vz))
print('distance quadratic between vectorX and vectorY: {}'.format(distance_quadratic_between_vx_vy))
print('distance quadratic between vectorZ and vectorY: {}'.format(distance_quadratic_between_vz_vy))

distance_euclidean_between_vx_vz = calculate_distance_euclidean(vector_x, vector_z)
distance_euclidean_between_vx_vy = calculate_distance_euclidean(vector_x, vector_y)
distance_euclidean_between_vz_vy = calculate_distance_euclidean(vector_z, vector_y)
print('distance euclidean between vectorX and vectorZ: {}'.format(distance_euclidean_between_vx_vz))
print('distance euclidean between vectorX and vectorY: {}'.format(distance_euclidean_between_vx_vy))
print('distance euclidean between vectorZ and vectorY: {}'.format(distance_euclidean_between_vz_vy))