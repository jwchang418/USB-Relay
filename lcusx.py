from serial import Serial

class LUCSX():
    ch1_on_bytes = bytes([0xA1,0x01,0x01,0xA2])
    ch1_off_bytes = bytes([0xA1,0x01,0x00,0xA1])
    ch2_on_bytes = bytes([0xA2,0x01,0x01,0xA4])
    ch2_off_bytes = bytes([0xA2,0x01,0x00,0xA3])
    ch3_on_bytes = bytes([0xA3,0x01,0x01,0xA5])
    ch3_off_bytes = bytes([0xA3,0x01,0x00,0xA4])
    ch4_on_bytes = bytes([0xA4,0x01,0x01,0xA6])
    ch4_off_bytes = bytes([0xA4,0x01,0x00,0xA5])
    ch5_on_bytes = bytes([0xA5,0x01,0x01,0xA7])
    ch5_off_bytes = bytes([0xA5,0x01,0x00,0xA6])
    ch6_on_bytes = bytes([0xA6,0x01,0x01,0xA8])
    ch6_off_bytes = bytes([0xA6,0x01,0x00,0xA7])
    ch7_on_bytes = bytes([0xA7,0x01,0x01,0xA9])
    ch7_off_bytes = bytes([0xA7,0x01,0x00,0xA8])    
    ch8_on_bytes = bytes([0xA8,0x01,0x01,0xAA])
    ch8_off_bytes = bytes([0xA8,0x01,0x00,0xA9])


    def __init__(self,port_name = "COM4"):
        self.com = Serial(port=port_name, baudrate=9600)
        return

    # ch 1
    def ch1_on(self):
        try:
            write_buffer = self.ch1_on_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False

    def ch1_off(self):
        try:
            write_buffer = self.ch1_off_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False
    
    # ch 2
    def ch2_on(self):
        try:
            write_buffer = self.ch2_on_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False
    
    def ch2_off(self):
        try:
            write_buffer = self.ch2_off_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False
    
    # ch 3
    def ch3_on(self):
        try:
            write_buffer = self.ch3_on_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False

    def ch3_off(self):
        try:
            write_buffer = self.ch3_off_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False
    
    # ch 4
    def ch4_on(self):
        try:
            write_buffer = self.ch4_on_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False

    def ch4_off(self):
        try:
            write_buffer = self.ch4_off_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False
    
    # ch 5
    def ch5_on(self):
        try:
            write_buffer = self.ch5_on_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False

    def ch5_off(self):
        try:
            write_buffer = self.ch5_off_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False
    
    # ch 6
    def ch6_on(self):
        try:
            write_buffer = self.ch6_on_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False

    def ch6_off(self):
        try:
            write_buffer = self.ch6_off_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False
    
    # ch 7
    def ch7_on(self):
        try:
            write_buffer = self.ch7_on_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False

    def ch7_off(self):
        try:
            write_buffer = self.ch7_off_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False
    
    # ch 8
    def ch8_on(self):
        try:
            write_buffer = self.ch5_on_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False

    def ch8_off(self):
        try:
            write_buffer = self.ch8_off_bytes
            self.com.write(write_buffer)
            return True
        except:
            return False