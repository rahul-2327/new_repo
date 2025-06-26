import json
import sqlite3


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError as e:
        print("file not found error", e)
        return []


def save_data_helper(videos):
    with open('youtube.txt', 'w')as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print('*'*100)
    for idx,vid in enumerate(videos,start=1):
        print(f"{idx}. Name: {vid['name']}, Duration: {vid['time']}")

    print('*' * 100)


def add_video(videos):
    name = input("Enter Video name: ")
    time = input("Enter video time: ")
    videos.append({'name':name,'time':time})
    print(videos)
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)

    idx = int(input("Enter the video number to update: "))
    if 1 <= idx <= len(videos):
        new_name = input("Enter the new video name: ")
        new_time = input("Enter the new video time: ")

        videos[idx-1] = {
            'name' : new_name,
            'time' : new_time
        }
        save_data_helper(videos)
        print("Video update successfully")
    else:
        print("You enter wrong video number")





def delete_video(videos=[]):
    list_all_videos(videos)
    idx = int(input("Enter the video number to delete: "))

    if 1 <= idx <= len(videos):
        # videos.pop(idx-1)
        del videos[idx-1]
        save_data_helper(videos)
        print("Video deleted successfully")
    else:
        print("You entered Invalid video number")


def main():
    while True:
        videos = load_data()   
        print("\n Youtube Manager ")
        print("1. List all videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")




if __name__ == "__main__":
    main()