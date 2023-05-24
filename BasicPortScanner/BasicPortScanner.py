import socket

print('https://github.com/Hyzle')
ip_address = input("IP adresini girin: ")

start_port = int(input("Başlangıç portunu girin: "))
end_port = int(input("Bitiş portunu girin: "))

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  

    result = sock.connect_ex((ip_address, port))
    if result == 0:
        print(f"Port {port} açık")
    
    sock.close()

input("İşlem tamamlandı. Devam etmek için bir tuşa basın...")
