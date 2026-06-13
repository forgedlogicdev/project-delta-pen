// Project Delta Pen (DP-1) - Ergonomic Handheld Chassis
// Tolerances and variables optimized for FSR strip insertion and NEMA 8 motor alignment.

$fn = 100;

// Pen dimensions
pen_length = 120;
pen_diameter = 18;
grip_taper = 14;

// Motor mounting base
motor_width = 20.5; // NEMA 8
motor_hole_spacing = 16.0;

module main_chassis() {
    difference() {
        // Main cylindrical handle
        union() {
            cylinder(h=pen_length - 20, d=pen_diameter, center=true);
            translate([0, 0, (pen_length/2) - 10])
                cylinder(h=20, d1=pen_diameter, d2=grip_taper, center=true);
        }
        
        // Coaxial wire feed guide channel (3mm PTFE path)
        cylinder(h=pen_length + 2, d=3.2, center=true);
        
        // FSR Sensor Recess (1mm deep indentation for flush fit)
        translate([0, (pen_diameter/2) - 0.5, 10])
            cube([6, 1.2, 50], center=true);
    }
}

main_chassis();
