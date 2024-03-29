$fn=80;

// Box dimensions.
length = 220;
width = 100;
height = 58;
cornerRadius = 2.5;

// Button hole dimensions.
buttonHoleRadius = 12;

translate([2.5, 2.5, 0]){
    difference() {
        // Box.
        roundedBox(length, width, height, cornerRadius); 
        translate([2.5,2.5,2]) {
            roundedBox(length-5, width-5, height, cornerRadius); 
        }
        // Button hole 1.
        translate([47.5,175,-1]) {
            cylinder(5,buttonHoleRadius,buttonHoleRadius);
        }
        // Button hole 2.
        translate([47.5,110,-1]) {
            cylinder(5,buttonHoleRadius,buttonHoleRadius);
        }
        // Button hole 3.
        translate([47.5,45,-1]) {
            cylinder(5,buttonHoleRadius,buttonHoleRadius);
        }
        // Cable hole.
        translate([-5,110,57]) {
            rotate([0,90,0]) {
                cylinder(10,6,6);
            }
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