// ZEO-ARCHITECT // MASTER COPY // ERBG V1
// DIMENSIONAL GATEWAY ARRAY

module Field_Ring(radius) {
    // Generates the Negative Energy torus
    rotate_extrude(convexity = 10, $fn = 100)
    translate([radius, 0, 0])
    circle(r = 5, $fn = 100);
}

module Singularity_Core() {
    // The containment unit for the artificial horizon
    difference() {
        sphere(r=20, $fn=100);
        cylinder(h=50, r=10, center=true); // The Throat
    }
}

module Timeline_Stabilizers() {
    // Anchors the gate to Earth-1
    for(i=[0:120:360]) {
        rotate([0, 0, i])
        translate([100, 0, -50])
        cylinder(h=100, r1=10, r2=5);
    }
}

// ASSEMBLY
union() {
    // Primary Ring (The Doorframe)
    color("cyan") Field_Ring(radius=150);
    
    // Secondary Compression Ring
    color("blue") translate([0,0,20]) Field_Ring(radius=140);

    // The Active Core (Do not touch when active)
    translate([0,0,0]) Singularity_Core();
    
    Timeline_Stabilizers();
}

// WARNING: ENSURE 'ZPM' IS AT 100% BEFORE INITIALIZING.
// PARTIAL POWER MAY RESULT IN SPAGHETTIFICATION.
