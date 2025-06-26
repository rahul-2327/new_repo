import sqlite3

con = sqlite3.connect("youtube_videos.db")
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name,time))
    con.commit() # type: ignore


def update_videos(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id=?",(new_name,new_time,video_id))
    con.commit()#type:ignore

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos where id = ?",(video_id,))
    con.commit()#type:ignore

    




def main():
    while True:

        print("\nYoutube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_videos(name,time)
                # name = input("Enter the name of the video: ")
                # time = input("Enter the time of the video: ")
                # sql ='''
                #     INSERT INTO videos()
                # '''
            case '3':
                video_id = input("Enter video ID to update: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time")
                update_videos(video_id,name,time) # type: ignore

            case '4':

                video_id = input("Enter the video Id to delete: ")
                delete_videos(video_id) # type: ignore

            case '5':
                print("Thank you for using the application!!!")
                break
            case _:
                print("Invalid choice, please enter correct choice")
    
    cursor.close()
    con.close()




if __name__ == "__main__":
    main()