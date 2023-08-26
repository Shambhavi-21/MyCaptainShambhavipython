import csv
def write_into_csv(info_list):
    csv_file=open('student_info.csv','a',newline='')
    writer=csv.writer(csv_file)
    if csv_file.tell() == 0:
        writer.writerow(["Name","Age","Contact_Number","E-mail ID"])
    writer.writerow(info_list)

if __name__=='__main__':
    condition = True

    while(condition):
        student_info=input("enter student info. in this format(Name Age Contact_number E-mail_ID):")
        print("Entered info."+student_info)

        student_info_list=student_info.split(' ')
        print("split up info. is:"+str(student_info_list))

        print("\nEntered info. is:\nName: {}\nAge: {}\nContact_Number: {}\nE-mail ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        choice_check = input("Is the entered info. correct? (yes/no):")
        if choice_check == "yes":
            write_into_csv(student_info_list)

            condition_check = input("Enter (yes/no) if you want to enter information for another student:")
            if condition_check == "yes":
                condition = True
            elif condition_check == "no":
                condition = False
        elif choice_check == "no":
            print("\nPlease enter the correct values!" )