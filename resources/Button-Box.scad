$fn=200;

// Box dimensions.
length = 230;
width = 135;
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
        translate([50,180,-1]) {
            cylinder(5,buttonHoleRadius,buttonHoleRadius);
        }
        // Button hole 2.
        translate([50,115,-1]) {
            cylinder(5,buttonHoleRadius,buttonHoleRadius);
        }
        // Button hole 3.
        translate([50,50,-1]) {
            cylinder(5,buttonHoleRadius,buttonHoleRadius);
        }
        // Cable hole.
        translate([-5,82.5,30]) {
            rotate([0,90,0]) {
                cylinder(10,4,4);
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