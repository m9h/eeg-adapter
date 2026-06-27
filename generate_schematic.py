import uuid

def generate_uuid():
    return str(uuid.uuid4())

def get_header():
    return f"""(kicad_sch (version 20211123) (generator "antigravity_script")
  (uuid {generate_uuid()})
  (paper "A2")
  (lib_symbols
    (symbol "Connector_Generic:Conn_02x32_Odd_Even" (pin_names (offset 1.016) hide) (in_bom yes) (on_board yes)
      (property "Reference" "J" (id 0) (at 1.27 2.54 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Value" "Conn_02x32_Odd_Even" (id 1) (at 1.27 -43.18 0)
        (effects (font (size 1.27 1.27)))
      )
      (property "Footprint" "" (id 2) (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (property "Datasheet" "~" (id 3) (at 0 0 0)
        (effects (font (size 1.27 1.27)) hide)
      )
      (symbol "Conn_02x32_Odd_Even_1_1"
        (rectangle (start -1.27 -41.91) (end 1.27 41.91)
          (stroke (width 0.254) (type default) (color 0 0 0 0))
          (fill (type background))
        )
      )
      {generate_connector_pins()}
    )
    (symbol "Device:R_Small" (pin_numbers hide) (pin_names (offset 0.254) hide) (in_bom yes) (on_board yes)
      (property "Reference" "R" (id 0) (at 0.762 0.508 0)
        (effects (font (size 1.27 1.27)) (justify left))
      )
      (property "Value" "R_Small" (id 1) (at 0.762 -1.016 0)
        (effects (font (size 1.27 1.27)) (justify left))
      )
      (symbol "R_Small_0_1"
        (rectangle (start -0.762 1.778) (end 0.762 -1.778)
          (stroke (width 0.2032) (type default) (color 0 0 0 0))
          (fill (type none))
        )
      )
      (symbol "R_Small_1_1"
        (pin passive line (at 0 2.54 270) (length 0.762)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "1" (effects (font (size 1.27 1.27))))
        )
        (pin passive line (at 0 -2.54 90) (length 0.762)
          (name "~" (effects (font (size 1.27 1.27))))
          (number "2" (effects (font (size 1.27 1.27))))
        )
      )
    )
  )
"""

def generate_connector_pins():
    pins = ""
    y_start = 40.64
    pin_spacing = 2.54
    for i in range(1, 65):
        y = y_start - ((i-1) // 2) * pin_spacing
        x = -5.08 if i % 2 != 0 else 5.08
        angle = 0 if i % 2 != 0 else 180
        pins += f"""
      (symbol "Conn_02x32_Odd_Even_1_1"
        (pin passive line (at {x} {y} {angle}) (length 3.81)
          (name "{i}" (effects (font (size 1.27 1.27))))
          (number "{i}" (effects (font (size 1.27 1.27))))
        )
      )"""
    return pins

def generate_schematic():
    content = get_header()
    
    # Grid settings
    x_start = 50.8
    y_start = 50.8
    
    # We need 4 connectors for 256 channels
    # Each connector handles 64 channels
    
    chan_counter = 1
    
    for conn_idx in range(4):
        conn_x = x_start + (conn_idx * 80.0)
        conn_y = y_start + 60.0
        
        # Place Connector
        content += f"""
  (symbol (lib_id "Connector_Generic:Conn_02x32_Odd_Even") (at {conn_x} {conn_y} 0) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (uuid {generate_uuid()})
    (property "Reference" "J{conn_idx+1}" (id 0) (at {conn_x} {conn_y - 45} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "Molex_SlimStack_64" (id 1) (at {conn_x} {conn_y + 45} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "Connector_Molex:Molex_SlimStack_502430-6410_2x32_P0.40mm_Vertical" (id 2) (at {conn_x} {conn_y} 0)
      (effects (font (size 1.27 1.27)) hide)
    )
  )"""

        # Place Resistors and Wires for this connector
        # 64 pins per connector.
        # Odd pins (1, 3, 5...) on left side of connector glyph
        # Even pins (2, 4, 6...) on right side of connector glyph
        
        # Connector pin coordinates based on the symbol definition above
        # The symbol pin definitions in generating logic:
        # i=1 -> y=40.64
        # i=3 -> y=40.64 - 2.54 
        # etc.
        # pin_y = 40.64 - ((pin_num-1)//2 * 2.54)
        
        # Left side (Odd pins)
        for pin in range(1, 65, 2):
            rel_y = 40.64 - ((pin-1)//2 * 2.54)
            abs_y = conn_y - rel_y # In KiCad SCH, Y increases downwards usually? 
            # Wait, symbol coord system: +Y is UP in symbol editor usually, but in schematic placement?
            # Standard library symbols usually have pin 1 at top.
            # Let's assume the symbol definition I emitted:
            # (start -1.27 -41.91) (end 1.27 41.91) -> it's centered on (0,0) with height ~84mm? No units are likely 50mil or mm.
            # 1.27 is 50mil. 41.91 is ~1650mil.
            # KiCad files use mm as base unit in modern versions, I think. Header says (generator "kicad_sch").
            # Coordinate space is usually (at X Y R).
            # Let's adhere to the symbol definition I created in `get_header`.
            
            # Pin placement in symbol:
            # y = y_start - ...
            # y_start = 40.64
            # So pin 1 is at +40.64 relative to symbol center.
            # If symbol is at (conn_x, conn_y), then pin 1 is at (conn_x - 5.08, conn_y - 40.64) (Note: Y axis direction)
            # In KiCad file format, Y increases downwards.
            # If I defined pin at +40.64 in symbol, and placed symbol at Y, then on screen it appears at Y - 40.64.
            
            # Let's map Channel names.
            current_chan = chan_counter
            chan_counter += 1
            
            pin_y_offset = 40.64 - ((pin-1)//2 * 2.54)
            # Pin pos in schematic space
            pin_x_sch = conn_x - 5.08 # Left side
            pin_y_sch = conn_y - pin_y_offset
            
            # Resistor pos (to the left of the connector)
            res_x = pin_x_sch - 15.0 
            res_y = pin_y_sch
            
            # Add Resistor
            content += f"""
  (symbol (lib_id "Device:R_Small") (at {res_x} {res_y} 90) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (uuid {generate_uuid()})
    (property "Reference" "R{current_chan}" (id 0) (at {res_x} {res_y - 2} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "5k" (id 1) (at {res_x} {res_y + 2} 0)
      (effects (font (size 1.27 1.27)))
    )
  )""" # Rotated 90 deg. Pin 1 (top in normal) is now Left? Or Right?
       # R_Small: Pin 1 at 0, 2.54. Pin 2 at 0, -2.54.
       # Rotated 90: Pin 1 at -2.54, 0. Pin 2 at 2.54, 0.
       # So Pin 2 (Right) should connect to Connector Pin (Left).
       # Pin 1 (Left) should connect to Input Label.
       
       # Wire from Resistor Pin 2 to Connector Pin
            w_x1 = res_x + 2.54
            w_y1 = res_y
            w_x2 = pin_x_sch
            w_y2 = pin_y_sch
            
            content += f"""
  (wire (pts (xy {w_x1} {w_y1}) (xy {w_x2} {w_y2}))
    (stroke (width 0) (type solid) (color 0 0 0 0))
    (uuid {generate_uuid()})
  )"""

            # Label at Input (Resistor Pin 1)
            label_x = res_x - 2.54
            label_y = res_y
            label_name = f"CH{current_chan}"
            
            content += f"""
  (label "{label_name}" (at {label_x} {label_y} 180)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid {generate_uuid()})
  )"""
        
        # Right side (Even pins)
        for pin in range(2, 65, 2):
            pin_y_offset = 40.64 - ((pin-1)//2 * 2.54) # Integer division shares row
            # Pin pos in schematic space
            pin_x_sch = conn_x + 5.08 # Right side
            pin_y_sch = conn_y - pin_y_offset
            
            current_chan = chan_counter
            chan_counter += 1
            
            # Resistor pos (to the right of the connector)
            res_x = pin_x_sch + 15.0 
            res_y = pin_y_sch
            
            # Add Resistor
            content += f"""
  (symbol (lib_id "Device:R_Small") (at {res_x} {res_y} 90) (unit 1)
    (in_bom yes) (on_board yes) (dnp no) (uuid {generate_uuid()})
    (property "Reference" "R{current_chan}" (id 0) (at {res_x} {res_y - 2} 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "5k" (id 1) (at {res_x} {res_y + 2} 0)
      (effects (font (size 1.27 1.27)))
    )
  )""" 
            # Rotated 90: Pin 1 at -2.54, 0. Pin 2 at 2.54, 0.
            # We want Pin 1 (Left) to connect to Connector (Right).
            # Pin 2 (Right) to connect to Label.
            
            # Wire from Resistor Pin 1 to Connector Pin
            w_x1 = res_x - 2.54
            w_y1 = res_y
            w_x2 = pin_x_sch
            w_y2 = pin_y_sch
            
            content += f"""
  (wire (pts (xy {w_x1} {w_y1}) (xy {w_x2} {w_y2}))
    (stroke (width 0) (type solid) (color 0 0 0 0))
    (uuid {generate_uuid()})
  )"""
  
            # Label at Input (Resistor Pin 2)
            label_x = res_x + 2.54
            label_y = res_y
            label_name = f"CH{current_chan}"
            
            content += f"""
  (label "{label_name}" (at {label_x} {label_y} 0)
    (effects (font (size 1.27 1.27)) (justify left))
    (uuid {generate_uuid()})
  )"""

    content += "\n)"
    return content

if __name__ == "__main__":
    sch_content = generate_schematic()
    with open("HD_Sensor_Interface/HD_Sensor_Interface.kicad_sch", "w") as f:
        f.write(sch_content)
