class Camera:
    def __init__(self, ip_address, mac_address, serial_number, streaming_url, user, password, connection_status) -> None:
        self.ip_address = ip_address
        self.mac_address = mac_address
        self.serial_number = serial_number
        self.streaming_url = streaming_url
        self.user = user
        self.password = password
        self.connection_status = connection_status


class CameraBuilder:
    def __init__(self) -> None:
        self.ip_address = None
        self.mac_address = None
        self.serial_number = None
        self.streaming_url = None
        self.user = None
        self.password = None
        self.connection_status = None
    
    def set_ip_address(self, ip_address):
        self.ip_address = ip_address
        return self
    
    def set_serial_number(self, serial_number):
        self.serial_number = serial_number
        return self
    
    def set_mac_address(self, mac_address):
        self.mac_address = mac_address
        return self

    def set_streaming_url(self, streaming_url):
        self.streaming_url = streaming_url
        return self
    
    def set_user(self, user):
        self.user = user
        return self

    def set_password(self, password):
        self.password = password
        return self
    
    def set_connection_status(self, connection_status):
        self.connection_status = connection_status
        return self

    def build(self) -> Camera:
        return Camera(
            self.ip_address,
            self.mac_address,
            self.serial_number,
            self.streaming_url,
            self.user,
            self.password,
            self.connection_status
            
        )

if __name__== "__main__":
    print("\nBuilder Pattern")
    print("=" * 50)

    builer = CameraBuilder()
    build_camera = builer.set_ip_address("12.34.5.6") \
                    .set_mac_address("") \
                    .set_serial_number("uuid_432_324_3123") \
                    .set_streaming_url("http://localhost:9001") \
                    .set_user("Cam2") \
                    .set_password("XXXXX") \
                    .set_connection_status(True) \
                    .build()

    print(f"build_camera: {build_camera.user}\n")

    generic_camera = Camera(
        "12.34.5.6",
        "",
        "432_u4324_32342_4324",
        "http://localhost:9889",
        "Cam1",
        "XXXX",
        False,
    )
    print(f"generic_camera: {generic_camera.user}")


