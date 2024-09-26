// quad_area.c
#include <math.h>
#include "quad.h"

// Function to calculate the area using the Shoelace formula
float calculateArea(quadrilateral quad) {
    double area = 0.5 * fabs(
        quad.node1.x * quad.node2.y + quad.node2.x * quad.node3.y + 
        quad.node3.x * quad.node4.y + quad.node4.x * quad.node1.y
        - (quad.node1.y * quad.node2.x + quad.node2.y * quad.node3.x + 
           quad.node3.y * quad.node4.x + quad.node4.y * quad.node1.x)
    );
    return (float)area;
}
