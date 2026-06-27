
import uuid

def generate_uuid():
    return str(uuid.uuid4())

def get_header():
    return f"""(kicad_sch (version 20211123) (generator "antigravity_script")
  (uuid {generate_uuid()})
  (paper "A4")
  (lib_symbols
    (symbol "Connector:USB3_B_Receptacle" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "J" (id 0) (at 0 7.62 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "USB3_B_Receptacle" (id 1) (at 0 -10.16 0)
        (effects (font (size 1.27 1.27)))
      )
      (symbol "USB3_B_Receptacle_1_1"
        (rectangle (start -5.08 6.35) (end 5.08 -8.89)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
        (pin power_out line (at 0 8.89 270) (length 2.54)
          (name "VBUS" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin bidir line (at -7.62 3.81 0) (length 2.54)
          (name "D-" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
        (pin bidir line (at -7.62 1.27 0) (length 2.54)
          (name "D+" (effects (font (size 1.27 1.27))))
          (number "3" (effects (font (size 1.27 1.27))))
        )
        (pin power_out line (at -7.62 -1.27 0) (length 2.54)
          (name "GND" (effects (font (size 1.27 1.27))))
          (number "4" (effects (font (size 1.27 1.27))))
        )
        (pin bidir line (at 7.62 3.81 180) (length 2.54)
          (name "SSTX-" (effects (font (size 1.27 1.27))))
          (number "5" (effects (font (size 1.27 1.27))))
        )
        (pin bidir line (at 7.62 1.27 180) (length 2.54)
          (name "SSTX+" (effects (font (size 1.27 1.27))))
          (number "6" (effects (font (size 1.27 1.27))))
        )
        (pin power_out line (at 7.62 -1.27 180) (length 2.54)
          (name "GND_DRAIN" (effects (font (size 1.27 1.27))))
          (number "7" (effects (font (size 1.27 1.27))))
        )
        (pin bidir line (at 7.62 -3.81 180) (length 2.54)
          (name "SSRX-" (effects (font (size 1.27 1.27))))
          (number "8" (effects (font (size 1.27 1.27))))
        )
        (pin bidir line (at 7.62 -6.35 180) (length 2.54)
          (name "SSRX+" (effects (font (size 1.27 1.27))))
          (number "9" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at 0 -11.43 90) (length 2.54)
          (name "SHIELD" (effects (font (size 1.27 1.27))))
          (number "10" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at 2.54 -11.43 90) (length 2.54)
          (name "SHIELD" (effects (font (size 1.27 1.27))))
          (number "11" (effects (font (size 1.27 1.27))))
        )
      )
    )
    (symbol "Connector:USB3_Micro_B_Plug" (pin_names (offset 1.016)) (in_bom yes) (on_board yes)
      (property "Reference" "J" (id 0) (at 0 7.62 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "USB3_Micro_B_Plug" (id 1) (at 0 -10.16 0)
        (effects (font (size 1.27 1.27)))
      )
      (symbol "USB3_Micro_B_Plug_1_1"
        (rectangle (start -5.08 6.35) (end 5.08 -8.89)
          (stroke (width 0.254) (type default))
          (fill (type background))
        )
        (pin power_out line (at 0 8.89 270) (length 2.54)
          (name "VBUS" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin bidir line (at -7.62 3.81 0) (length 2.54)
          (name "D-" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
        (pin bidir line (at -7.62 1.27 0) (length 2.54)
          (name "D+" (effects (font (size 1.27 1.27))))
          (number "3" (effects (font (size 1.27 1.27))))
        )
        (pin power_out line (at -7.62 -3.81 0) (length 2.54)
          (name "GND" (effects (font (size 1.27 1.27))))
          (number "4" (effects (font (size 1.27 1.27))))
        )
        (pin bidir line (at 7.62 3.81 180) (length 2.54)
          (name "SSTX-" (effects (font (size 1.27 1.27))))
          (number "5" (effects (font (size 1.27 1.27))))
        )
        (pin bidir line (at 7.62 1.27 180) (length 2.54)
          (name "SSTX+" (effects (font (size 1.27 1.27))))
          (number "6" (effects (font (size 1.27 1.27))))
        )
        (pin power_out line (at 7.62 -1.27 180) (length 2.54)
          (name "GND_DRAIN" (effects (font (size 1.27 1.27))))
          (number "7" (effects (font (size 1.27 1.27))))
        )
        (pin bidir line (at 7.62 -3.81 180) (length 2.54)
          (name "SSRX-" (effects (font (size 1.27 1.27))))
          (number "8" (effects (font (size 1.27 1.27))))
        )
        (pin bidir line (at 7.62 -6.35 180) (length 2.54)
          (name "SSRX+" (effects (font (size 1.27 1.27))))
          (number "9" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at 0 -11.43 90) (length 2.54)
          (name "SHIELD" (effects (font (size 1.27 1.27))))
          (number "10" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at -7.62 -1.27 0) (length 2.54)
           (name "ID" (effects (font (size 1.27 1.27))))
           (number "4_ID" (effects (font (size 1.27 1.27))))
        ) 
      )
    )
    (symbol "Device:R" (pin_names (offset 0)) (in_bom yes) (on_board yes)
       (property "Reference" "R" (id 0) (at 2.032 0 90) (effects (font (size 1.27 1.27))))
       (property "Value" "R" (id 1) (at 0 0 90) (effects (font (size 1.27 1.27))))
       (symbol "R_1_1"
         (rectangle (start -1.016 2.54) (end 1.016 -2.54) (stroke (width 0.254)) (fill (type none)))
         (pin passive line (at 0 3.81 270) (length 1.27) (name "~" (effects (font (size 1.27 1.27)) hide)) (number "1" (effects (font (size 1.27 1.27)) hide)))
         (pin passive line (at 0 -3.81 90) (length 1.27) (name "~" (effects (font (size 1.27 1.27)) hide)) (number "2" (effects (font (size 1.27 1.27)) hide)))
       )
    )
    (symbol "Device:C" (pin_names (offset 0)) (in_bom yes) (on_board yes)
       (property "Reference" "C" (id 0) (at 2.032 0 90) (effects (font (size 1.27 1.27))))
       (property "Value" "C" (id 1) (at 0 0 90) (effects (font (size 1.27 1.27))))
       (symbol "C_1_1"
         (polyline (pts (xy -2.032 0.762) (xy 2.032 0.762)) (stroke (width 0.508)))
         (polyline (pts (xy -2.032 -0.762) (xy 2.032 -0.762)) (stroke (width 0.508)))
         (pin passive line (at 0 3.81 270) (length 3.048) (name "~" (effects (font (size 1.27 1.27)) hide)) (number "1" (effects (font (size 1.27 1.27)) hide)))
         (pin passive line (at 0 -3.81 90) (length 3.048) (name "~" (effects (font (size 1.27 1.27)) hide)) (number "2" (effects (font (size 1.27 1.27)) hide)))
       )
    )
    (symbol "Device:LED" (pin_names (offset 0)) (in_bom yes) (on_board yes)
       (property "Reference" "D" (id 0) (at 2.032 0 90) (effects (font (size 1.27 1.27))))
       (property "Value" "LED" (id 1) (at 0 0 90) (effects (font (size 1.27 1.27))))
       (symbol "LED_1_1"
         (polyline (pts (xy -1.27 1.27) (xy 1.27 0) (xy -1.27 -1.27) (xy -1.27 1.27)) (stroke (width 0.254)) (fill (type none)))
         (polyline (pts (xy 1.27 1.27) (xy 1.27 -1.27)) (stroke (width 0.254)))
         (pin passive line (at -3.81 0 0) (length 2.54) (name "A" (effects (font (size 1.27 1.27)) hide)) (number "2" (effects (font (size 1.27 1.27)) hide)))
         (pin passive line (at 3.81 0 180) (length 2.54) (name "K" (effects (font (size 1.27 1.27)) hide)) (number "1" (effects (font (size 1.27 1.27)) hide)))
       )
    )
  )
"""

def generate_wire(x1, y1, x2, y2):
    return f"""
  (wire (pts (xy {x1} {y1}) (xy {x2} {y2}))
    (stroke (width 0) (type solid) (color 0 0 0 0))
    (uuid {generate_uuid()})
  )"""

def generate_label(text, x, y, orientation=0):
    return f"""
  (label "{text}" (at {x} {y} {orientation})
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid {generate_uuid()})
  )"""

def generate_schematic():
    content = get_header()
    
    # Coordinates
    x_in = 50.8
    y_center = 80.0
    x_out = 150.8
    
    # Input Connector
    content += f"""
  (symbol (lib_id "Connector:USB3_B_Receptacle") (at {x_in} {y_center} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (uuid {generate_uuid()})
    (property "Reference" "J1" (id 0) (at {x_in} {y_center - 12} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB3_B_IN" (id 1) (at {x_in} {y_center + 12} 0) (effects (font (size 1.27 1.27))))
  )"""
  
    # Output Connector
    content += f"""
  (symbol (lib_id "Connector:USB3_Micro_B_Plug") (at {x_out} {y_center} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (uuid {generate_uuid()})
    (property "Reference" "J2" (id 0) (at {x_out} {y_center - 12} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "USB3_Micro_B_OUT" (id 1) (at {x_out} {y_center + 12} 0) (effects (font (size 1.27 1.27))))
  )"""
  
    # Wiring / Net Labels
    
    # J1 Connections
    # Right Side Pins (5,6,7,8,9)
    right_pins = {5: 3.81, 6: 1.27, 7: -1.27, 8: -3.81, 9: -6.35}
    for p, y_off in right_pins.items():
        start_x = x_in + 7.62
        abs_y = y_center - y_off
        content += generate_wire(start_x, abs_y, start_x + 5.08, abs_y)
        sig_name = [n for n,s in [(5,"SSTX-"),(6,"SSTX+"),(7,"GND"),(8,"SSRX-"),(9,"SSRX+")] if n==p][0]
        content += generate_label(sig_name, start_x + 5.08, abs_y, 0)
        
    # J1 Left Side Pins (2,3,4)
    left_pins = {2: 3.81, 3: 1.27, 4: -1.27}
    for p, y_off in left_pins.items():
        start_x = x_in - 7.62
        abs_y = y_center - y_off
        content += generate_wire(start_x, abs_y, start_x - 5.08, abs_y)
        sig_name = [n for n,s in [(2,"D-"),(3,"D+"),(4,"GND")] if n==p][0]
        content += generate_label(sig_name, start_x - 5.08, abs_y, 180) 
        
    # J2 Connections (Output)
    # J2 Left Side Pins (2,3,4)
    for p, y_off in left_pins.items():
        start_x = x_out - 7.62
        abs_y = y_center - y_off
        content += generate_wire(start_x, abs_y, start_x - 5.08, abs_y)
        sig_name = [n for n,s in [(2,"D-"),(3,"D+"),(4,"GND")] if n==p][0]
        content += generate_label(sig_name, start_x - 5.08, abs_y, 180)
        
    # J2 Right Side Pins (5,6,7,8,9)
    for p, y_off in right_pins.items():
        start_x = x_out + 7.62
        abs_y = y_center - y_off
        content += generate_wire(start_x, abs_y, start_x + 5.08, abs_y)
        sig_name = [n for n,s in [(5,"SSTX-"),(6,"SSTX+"),(7,"GND"),(8,"SSRX-"),(9,"SSRX+")] if n==p][0]
        content += generate_label(sig_name, start_x + 5.08, abs_y, 0)

    # SHIELD (Pin 10, 11)
    # J1 Shield
    content += generate_wire(x_in, y_center + 11.43, x_in, y_center + 15.0)
    content += generate_label("SHIELD", x_in, y_center + 15.0, 270)
    
    # J2 Shield
    content += generate_wire(x_out, y_center + 11.43, x_out, y_center + 15.0)
    content += generate_label("SHIELD", x_out, y_center + 15.0, 270)
    
    # GND to SHIELD Bleed Circuit
    x_gnd = 100.0
    y_gnd = 100.0
    
    # R1
    content += f"""
  (symbol (lib_id "Device:R") (at {x_gnd} {y_gnd} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (uuid {generate_uuid()})
    (property "Reference" "R1" (id 0) (at {x_gnd+2} {y_gnd} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "1M" (id 1) (at {x_gnd+2} {y_gnd+2} 0) (effects (font (size 1.27 1.27))))
  )""" 
    
    # C1
    content += f"""
  (symbol (lib_id "Device:C") (at {x_gnd+10} {y_gnd} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (uuid {generate_uuid()})
    (property "Reference" "C1" (id 0) (at {x_gnd+12} {y_gnd} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "10nF" (id 1) (at {x_gnd+12} {y_gnd+2} 0) (effects (font (size 1.27 1.27))))
  )"""
    
    # Connect Tops to GND
    content += generate_wire(x_gnd, y_gnd - 3.81, x_gnd+10, y_gnd - 3.81) 
    content += generate_wire(x_gnd, y_gnd - 3.81, x_gnd, y_gnd - 6.0) 
    content += generate_label("GND", x_gnd, y_gnd - 6.0, 90)
    
    # Connect Bottoms to SHIELD
    content += generate_wire(x_gnd, y_gnd + 3.81, x_gnd+10, y_gnd + 3.81) 
    content += generate_wire(x_gnd, y_gnd + 3.81, x_gnd, y_gnd + 6.0) 
    content += generate_label("SHIELD", x_gnd, y_gnd + 6.0, 270)

    # LED Circuit
    content += generate_wire(x_out, y_center - 8.89, x_out, y_center - 15.0) 
    content += generate_label("VBUS_OUT", x_out, y_center - 15.0, 90)
    
    x_led = 130.0
    y_led = 60.0 
    
    # R2
    content += f"""
  (symbol (lib_id "Device:R") (at {x_led} {y_led} 90) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (uuid {generate_uuid()})
    (property "Reference" "R2" (id 0) (at {x_led} {y_led-2} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "1k" (id 1) (at {x_led} {y_led+2} 0) (effects (font (size 1.27 1.27))))
  )""" 
    
    # LED D1
    content += f"""
  (symbol (lib_id "Device:LED") (at {x_led + 10} {y_led} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (uuid {generate_uuid()})
    (property "Reference" "D1" (id 0) (at {x_led+10} {y_led-2} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "GREEN" (id 1) (at {x_led+10} {y_led+2} 0) (effects (font (size 1.27 1.27))))
  )""" 
    
    # Wiring LED
    # VBUS_OUT -> R2.2 (Left) -> R2.1 (Right) -> D1.2 (Anode, Left) -> D1.1 (Cathode, Right) -> GND
    
    content += generate_label("VBUS_OUT", x_led - 5.0, y_led, 180)
    content += generate_wire(x_led - 5.0, y_led, x_led - 3.81, y_led) # To R2 (Left, Pin 2)
    
    # R2 (Right, Pin 1) at x_led + 3.81
    # D1 (Left, Pin 2/Anode) at (x_led+10) - 3.81 = x_led + 6.19
    content += generate_wire(x_led + 3.81, y_led, x_led + 6.19, y_led) # R2 to D1
    
    # D1 (Right, Pin 1/Cathode) at (x_led+10) + 3.81 = x_led + 13.81
    content += generate_wire(x_led + 13.81, y_led, x_led + 16.0, y_led) # D1 to GND
    content += generate_label("GND", x_led + 16.0, y_led, 0)

    content += "\n)"
    return content

if __name__ == "__main__":
    sch_content = generate_schematic()
    output_path = "USB3_Data_Interposer/USB3_Data_Interposer.kicad_sch"
    with open(output_path, "w") as f:
        f.write(sch_content)
    print(f"Generated {output_path}")
