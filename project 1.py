import csv
def write_into_file(info):
 with open('student_info.csv','a',newline='') as csv_file:
    writer=csv.writer(csv_file)
    if csv_file.tell()==0:
        writer.writerow(["rollno","name","contact no","college name","emailid"])
    writer.writerow(info)

condition=True
while(condition):
        student_info=input("enter rollno,name,contactno,collegename,emailid :")
        student_info_list=student_info.split(' ')
        print("\nrollno: {}\nname: {}\ncontactno:{}\ncollegename: {}\nemailid: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4]))
        check=input("type ( yes or no )if given values are entered correctly:")
        if check=='yes':
            write_into_file(student_info_list)
            iswant=input("type (yes or no) to give details of another student:")
            if iswant=='yes':
                condition=True
            elif iswant=='no':
                condition=False
        elif check=='no':
            print("re enter values")
           
  OUTPUT:
rollno	name	contact no	college name	emailid
50	   sita	  76543123	  nitap	        s.com
60	   rama	  123432123	  nitk	        r.com

enter rollno,name,contactno,collegename,emailid :50 sita 76543123 nitap s.com
rollno: 50
name: sita
contactno:76543123
collegename: nitap
emailid: s.com
type ( yes or no )if given values are entered correctly:yes
type (yes or no) to give details of another student:yes
enter rollno,name,contactno,collegename,emailid :60 rama 123432123 nitk r.com

rollno: 60
name: rama
contactno:123432123
collegename: nitk
emailid: r.com
type ( yes or no )if given values are entered correctly:yes
type (yes or no) to give details of another student:no
