// quad_perimeter.c
#include <math.h>
#include "quad.h"

// Function to calculate the distance between two points
static double distance(point p1, point p2) {
    return sqrt((p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y));
}

// Function to calculate the perimeter of the quadrilateral
float calculatePerimeter(quadrilateral quad) {
    double d1 = distance(quad.node1, quad.node2);
    double d2 = distance(quad.node2, quad.node3);
    double d3 = distance(quad.node3, quad.node4);
    double d4 = distance(quad.node4, quad.node1);
    return (float)(d1 + d2 + d3 + d4);
}
