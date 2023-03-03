$fn=200;

// Box dimensions.
length = 180;
width = 150;
height = 51;
cornerRadius = 5;

// Button hole dimensions.
buttonHoleRadius = 12;

translate([5, 5, 0]){
    difference() {
        // Box.
        roundedBox(length, width, height, cornerRadius); 
        translate([1,1,1]) {
            roundedBox(length-2, width-2, height, cornerRadius); 
        }
        // Button hole 1.
        translate([40,130,-1]) {
            cylinder(5,buttonHoleRadius,buttonHoleRadius);
        }
        // Button hole 2.
        translate([40,40,-1]) {
            cylinder(5,buttonHoleRadius,buttonHoleRadius);
        }
        // Button hole 3.
        translate([110,85,-1]) {
            cylinder(5,buttonHoleRadius,buttonHoleRadius);
        }
    }
}

module roundedBox(length, width, height, radius)
{
    dRadius = 2*radius;

    //base rounded shape
    minkowski() {
        cube(size=[width-dRadius,length-dRadius, height]);
        cylinder(r=radius, h=0.01);
    }
}