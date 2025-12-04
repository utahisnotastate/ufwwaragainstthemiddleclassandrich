// ZEO-ARCHITECT // MASTER COPY // MCU V1
// ATOMIC RE-SEQUENCER

module Intake_Vortex() {
    // Where raw matter/vacuum is sucked in
    difference() {
        cylinder(h=50, r1=40, r2=10, center=true);
        cylinder(h=60, r1=35, r2=5, center=true);
    }
}

module Transmutation_Chamber() {
    // The "Alchemist's Crucible"
    translate([0,0,-40])
    sphere(r=30, $fn=100);
    
    // Scalar Injectors
    for(i=[0:60:360]) {
        rotate([0, 0, i])
        translate([25, 0, -40])
        sphere(r=5);
    }
}

module Output_Nozzle() {
    // Where the bounty flows out
    translate([0,0,-80])
    cylinder(h=40, r1=5, r2=20, center=true);
}

// ASSEMBLY
union() {
    color("gray") Intake_Vortex();
    color("gold") Transmutation_Chamber();
    color("white") Output_Nozzle();
}

// NOTE: DO NOT PUT HAND INSIDE INTAKE.
// YOUR HAND WILL BECOME PART OF THE PIZZA.
