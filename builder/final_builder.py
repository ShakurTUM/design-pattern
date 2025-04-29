import dataclasses
from typing import Optional

@dataclasses.dataclass
class Camera:
    ip_address: Optional[str]
    mac_address: Optional[str]
    connection_status: bool
    serial_number: Optional[str]
    streaming_url: Optional[str]
    username: Optional[str]
    password: Optional[str]


if __name__== "__main__":
    print("\nBuilder Pattern")
    print("=" * 50)

    camera = Camera(
        ip_address="12.34.5.6",
        mac_address="",
        connection_status=False,
        serial_number="432_u4324_32342_4324",
        streaming_url="http://localhost:9889",
        username="Cam1",
        password="XXXX",
    )
    print(f"camera: {camera.username}\n")
