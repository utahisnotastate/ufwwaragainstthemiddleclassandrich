// ZEO-ARCHITECT // MASTER COPY // EHP V1
// GRAVITATIONAL LOGIC UNIT

module Gravity_Containment_Field() {
    // Magnetic bottle to hold the singularity
    difference() {
        sphere(r=50, $fn=100);
        sphere(r=40, $fn=100);
        
        // Radiation Vents (Data Output)
        for(i=[0:90:360]) {
            rotate([0, i, 0])
            cylinder(h=120, r=15, center=true);
        }
    }
}

module Event_Horizon() {
    // The "CPU" itself - Pure Void
    color("black") sphere(r=10); 
}

module Photon_Injectors() {
    // Data Input Lasers
    for(z=[-1, 1]) {
        translate([0, 0, z*60])
        cylinder(h=30, r=5);
    }
}

// ASSEMBLY
union() {
    color("silver") Gravity_Containment_Field();
    Event_Horizon();
    color("red") Photon_Injectors();
}

// WARNING: DO NOT BREACH CONTAINMENT. 
// A KILOTON EXPLOSION WILL RESULT.
