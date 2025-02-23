from CodeBase.AtGame.generate_qr_code import generate_qr_code
from CodeBase.ComeToTheGame.AdvertisingMaterial.generate_advertising_material import generate_advertising_material
from CodeBase.Communications.send_message import send_message


def come_to_the_game():
    print("Admin Panel Not Integrated into webGUI.")
    print("Before The Game:")
    print("0: Contact All Students for opt in to game based notifications.")
    print("1: Contact opted-in students about the upcoming game.")
    print("2: Generate advertising material.")
    print("During The Game:")
    print("3: Send push notification to game attendees due to delay")
    print("4: Send push notification to game staff.")
    print("5: Create QR code to show on the JumboTron.")
    choice = input("Pick a number: ")
    if choice == "0":
        send_message("one_time_student.json")
    elif choice == "1":
        send_message("notify_sports_based.json")
    elif choice == "2":
        url = input("Enter the URL of the advertising material img: ")
        mssg = input("Enter the message to put on the advertising material: ")
        generate_advertising_material(url, mssg)
    elif choice == "3":
        send_message("notify_sports_weather.json")
    elif choice == "4":
        send_message("notify_game_staff.json")
    elif choice == "5":
        url = input("Enter the URL of the qr code: ")
        generate_qr_code(url)


if __name__ == '__main__':
    come_to_the_game()