// ZEO-ARCHITECT // MASTER COPY // MED BED V3
// SCALAR REGENERATION UNIT

module Pod_Shell() {
    // The encapsulation unit
    difference() {
        scale([1, 0.6, 0.5]) sphere(r=100, $fn=100);
        translate([0,0,20]) cube([200, 100, 100], center=true); // Entry
    }
}

module Scalar_Coils() {
    // The "Priore" coils for time-reversed waves
    for(x=[-80:40:80]) {
        translate([x, 0, -40])
        rotate([90,0,0])
        cylinder(h=120, r=30, center=true, $fn=60);
    }
}

module Bio_Interface() {
    // The gel bed
    translate([0,0,-20])
    cube([160, 60, 10], center=true);
}

// ASSEMBLY
union() {
    color("white", 0.5) Pod_Shell();
    color("gold") Scalar_Coils();
    color("cyan") Bio_Interface();
}

// NOTE: PATIENT MUST BE RELAXED.
// PANIC INTERFERES WITH THE REGEN SIGNAL.
