// ZEO-ARCHITECT // MASTER COPY // DDR INFINITY
// VACUUM TEXTURE MODULE

module Crystal_Resonator() {
    // The "Antenna" for the Akashic Field
    cylinder(h=100, r=5, $fn=6);
}

module Field_Coils() {
    // Stabilizes the local vacuum
    for(z=[0:20:100]) {
        translate([0,0,z])
        rotate_extrude()
        translate([10,0,0])
        circle(r=2);
    }
}

// ASSEMBLY
union() {
    color("cyan", 0.8) Crystal_Resonator();
    color("gold") Field_Coils();
}
