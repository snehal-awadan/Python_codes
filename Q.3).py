# Q.3)

class Friend:
    def __init__(self, friend_id, name, hobby):
        self.friend_id = friend_id
        self.name = name
        self.hobby = hobby

def display_all_friends(friends):
    print("\n--- All Friends ---")
    for friend in friends:
        print(f"ID: {friend.friend_id}, Name: {friend.name}, Hobby: {friend.hobby}")

def search_by_id(friends, friend_id):
    for friend in friends:
        if friend.friend_id == friend_id:
            print("\n--- Friend Found ---")
            print(f"ID: {friend.friend_id}, Name: {friend.name}, Hobby: {friend.hobby}")
            return
    print("\nFriend not found!")

def search_by_name(friends, name):
    for friend in friends:
        if friend.name.lower() == name.lower():
            print(f"ID: {friend.friend_id}, Name: {friend.name}, Hobby: {friend.hobby}")
        else:
            print("not found")
            
def display_friends_with_hobby(friends, hobby):
    found = False
    print(f"\n--- Friends with Hobby: {hobby} ---")
    for friend in friends:
        if friend.hobby.lower() == hobby.lower():
            print(f"ID: {friend.friend_id}, Name: {friend.name}, Hobby: {friend.hobby}")
            found = True
    if not found:
        print("No friends found with that hobby!")

def main():
    friends = []
    while True:
        print("\n--- Menu ---")
        print("1. Add Friend")
        print("2. Display All Friends")
        print("3. Search by ID")
        print("4. Search by Name")
        print("5. Display Friends with a particular Hobby")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            friend_id = input("Enter ID: ")
            name = input("Enter Name: ")
            hobby = input("Enter Hobby: ")
            friend = Friend(friend_id, name, hobby)
            friends.append(friend)
            print("Friend added successfully!")
            
        elif choice == '2':
            display_all_friends(friends)
            
        elif choice == '3':
            friend_id = input("Enter ID to search: ")
            search_by_id(friends, friend_id)
            
        elif choice == '4':
            name = input("Enter Name to search: ")
            search_by_name(friends, name)
            
        elif choice == '5':
            hobby = input("Enter Hobby to search: ")
            display_friends_with_hobby(friends, hobby)
            
        elif choice == '6':
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()


