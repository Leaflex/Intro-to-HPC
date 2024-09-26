#ifndef __QUAD_H__
#define __QUAD_H__

typedef struct {
    double x, y;
} point;

typedef struct {
    point node1;
    point node2;
    point node3;
    point node4;
    double area;
    double perimeter;
} quadrilateral;

float calculatePerimeter(quadrilateral quad);
float calculateArea(quadrilateral quad);

#endif