import os
import logging


# File handler and stream handler setup
logger = logging.getLogger("File_Manager_Logger")
logger.setLevel(logging.DEBUG)

if logger.hasHandlers():
    logger.handlers.clear()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)  
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler("file_manager.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


class FileManager:
    def create_file(self,filename):
        try:

            with open(filename, 'x') as f:
                logger.info(f"File '{filename}' created successfully.")
                print(f"File '{filename}'  created successfully!")

        except FileExistsError:
            logger.warning(f"File '{filename}' already exists.")
            print(f"File '{filename}' already exists!")

        except Exception as e:
            logger.error(f"Unexpected error while creating file : {e}")
            print(f"Unexpected error : {e}")


    def view_all_files(self):
        try:

            files = os.listdir()
            if not files:
                logger.info("No files found in the directory.")
                print("No file found!")

            else:
                print("Files in directory!")
                for file in files:
                    print(file)
                logger.info("Listed all files.")

        except Exception as e:
            logger.error(f"Unexpected error while viewing files : {e}")
            print(f"Unexpected error : {e}")


    def delete_file(self,filename):
        try:

            os.remove(filename)
            logger.info(f"File '{filename}' deleted.")
            print(f"'{filename}' has been deleted successfully!")
        
        except FileNotFoundError:
            logger.info(f"Attempted to delete non existent file '{filename}'.")
            print("File not found!")

        except Exception as e:
            logger.error(f"Unexpected error while deleting file : {e}")
            print(f"Unexpected error : {e}")


    def read_file(self,filename):
        try:

            with open(filename,'r') as f:
                content = f.read()
                logger.info(f"Read file '{filename}'.")
                print(f"Content of '{filename}' : \n{content }")

        except FileNotFoundError:
            logger.error(f"File '{filename}' not found for reading.")
            print(f"'{filename}' doesn't exist!")
        
        except Exception as e:
            logger.error(f"Unexpected error occurred while reading file : {e}")
            print(f"Unexpected error : {e}")


    def edit_file(self,filename):
        try:

            with open(filename,'a') as f:
                content = input("Enter data to add = ")
                f.write(content + "\n")
                logger.info(f"Appended content to '{filename}'")
                print(f"Content added to '{filename}' successfully!")
        
        except FileNotFoundError:
            logger.warning(f"File '{filename}' not found for editing.")
            print(f"'{filename}' doesn't exist!")
        
        except Exception as e:
            logger.error(f"Unexpected error occured while editing file : {e}")
            print(f"Unexpected error : {e}")


    def run(self):
        while True:
            print("File Management System")
            print("1: Create file")
            print("2: View all files")
            print("3: Delete file")
            print("4: Read file")
            print("5: Edit file")
            print("6: Exit")

            try:
                choice = int(input("Enter your choice(1-6) = "))

                if choice == 1:
                    filename = input("Enter the file-name to create = ")
                    self.create_file(filename)

                elif choice == 2:
                    self.view_all_files()

                elif choice == 3:
                    filename = input("Enter the file-name to delete = ")
                    self.delete_file(filename)

                elif choice == 4:
                    filename = input("Enter the file-name to read = ")
                    self.read_file(filename)

                elif choice == 5:
                    filename = input("Enter the file-name to edit = ")
                    self.edit_file(filename)

                elif choice == 6 :
                    print("Closing the system...")
                    break

                else:
                    print("Invalid input!")

            except ValueError as ve:
                logger.warning(f"Invalid menu input : {ve}")
                print(f"Enter only numbers between 1 to 6")


if __name__ == "__main__":
    FileManager().run()