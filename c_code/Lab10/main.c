// main.c
#include <stdio.h>
#include "quad.h"

int main() {
    quadrilateral quad;

    // Input the coordinates of the quadrilateral
    printf("Enter the coordinates of the quadrilateral in order (x1 y1 x2 y2 x3 y3 x4 y4):\n");
    scanf("%lf %lf %lf %lf %lf %lf %lf %lf",
          &quad.node1.x, &quad.node1.y, 
          &quad.node2.x, &quad.node2.y, 
          &quad.node3.x, &quad.node3.y, 
          &quad.node4.x, &quad.node4.y);

    // Calculate the perimeter and area
    quad.perimeter = calculatePerimeter(quad);
    quad.area = calculateArea(quad);

    // Display the results
    printf("Perimeter of the quadrilateral: %.2f\n", quad.perimeter);
    printf("Area of the quadrilateral: %.2f\n", quad.area);

    return 0;
}
