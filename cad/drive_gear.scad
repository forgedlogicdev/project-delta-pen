// Project Delta Pen (DP-1) - V-Groove Stepper Drive Gear
// Designed to clamp onto a 5mm NEMA 8 stepper shaft and grip TIG filler wire.

$fn = 80;

gear_diameter = 12;
gear_thickness = 8;
bore_diameter = 5.0; // standard motor shaft
groove_depth = 1.0;
groove_angle = 90; // 90 degree V-groove

module drive_gear() {
    difference() {
        // Outer wheel body
        cylinder(h=gear_thickness, d=gear_diameter, center=true);
        
        // Motor shaft bore
        cylinder(h=gear_thickness + 2, d=bore_diameter, center=true);
        
        // V-Groove path for the wire
        rotate_extrude() {
            translate([gear_diameter/2, 0, 0])
                rotate([0, 0, 45])
                    square([groove_depth * sqrt(2), groove_depth * sqrt(2)], center=true);
        }
        
        // Set screw M3 thread hole
        translate([0, 0, 0])
            rotate([90, 0, 0])
                cylinder(h=gear_diameter + 2, d=2.5, center=true);
    }
}

drive_gear();
