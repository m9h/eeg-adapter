// Headstage Aggregator PCB Mockup
// Dimensions: 20mm x 25mm (Target)
pcb_width = 20;
pcb_length = 25;
pcb_thickness = 1.6;
hole_dia = 1.8; // M1.6 clearance
hole_inset = 1.5;

module pcb() {
    color("green")
    difference() {
        cube([pcb_width, pcb_length, pcb_thickness]);
        // Holes
        translate([hole_inset, hole_inset, -1]) cylinder(h=pcb_thickness+2, d=hole_dia, $fn=20);
        translate([pcb_width-hole_inset, hole_inset, -1]) cylinder(h=pcb_thickness+2, d=hole_dia, $fn=20);
        translate([hole_inset, pcb_length-hole_inset, -1]) cylinder(h=pcb_thickness+2, d=hole_dia, $fn=20);
        translate([pcb_width-hole_inset, pcb_length-hole_inset, -1]) cylinder(h=pcb_thickness+2, d=hole_dia, $fn=20);
    }
}

// Basic case shell (Concept)
module case_shell() {
    wall = 1.0;
    color("gray", 0.5)
    difference() {
        translate([-wall, -wall, -wall]) cube([pcb_width+2*wall, pcb_length+2*wall, pcb_thickness+5]); 
        translate([0,0,0]) cube([pcb_width, pcb_length, 10]); // Internal cavity
    }
}

// Render
pcb();
translate([0,0, pcb_thickness]) case_shell();
