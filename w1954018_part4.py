# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20221170          UoW No: w1954018
 
# Date: 6th of December 2022

#outcomes
progress = 0
trailer = 0
excluded = 0
retriever = 0

final_results = {} #dictionary


#lists
progress_lst = []
trailer_lst = []
excluded_lst = []
retriever_lst = []


def validation(message):  #user defined functions
    while True:
        credit = 0
        try:
            print('Please enter your credit at', message, ': ', end='')
            credit = int(input())
        except ValueError:
            print('Integer Required')
            continue
        if credit not in range(0, 121, 20):
            print('Out of range\n')
            continue
        else:
            return credit

def marks_dict(count,mark_list,output):
    while True:
        if count > 0:
            mark_list.extend([pass_m, defer_m, fail_m,student_ID]) ##https://www.freecodecamp.org/news/append-in-python-how-to-append-to-a-list-or-an-array/           
            tot_marks = "%s - %d, %d, %d" % (output, mark_list[0], mark_list[1], mark_list[2]) ##https://www.udacity.com/blog/2020/11/python-string-format-whats-the-difference-between-s-and-d.html 
            final_results.update({mark_list[3]: tot_marks})
            del mark_list[3]
            del (mark_list[0:3])
            count = count - 1
            continue
        else:
            break
while True:
    student_ID = input('Enter your student ID : ')
    pass_m = validation('pass')  #function call
    defer_m = validation('defer')
    fail_m = validation('fail')
    if pass_m + defer_m + fail_m != 120:
        print('Total incorrect')
    else:
        if pass_m == 120 and defer_m == fail_m == 0:
            print('Progression Outcome: Progress')
            progress = progress + 1
            print("Progress")
            marks_dict(progress,progress_lst,"Progress")
            
        elif pass_m == 100 and pass_m > (defer_m + fail_m):
            print('Progression Outcome: Progress(module trailer)')
            trailer = trailer + 1
            print("Progress (module trailer)")
            marks_dict(trailer,trailer_lst,"Progress (module trailer)")
            
        elif fail_m > (pass_m + defer_m):
            print('Progression Outcome: Exclude')
            excluded = excluded + 1
            print("Exclude")
            marks_dict(excluded,excluded_lst,"Exclude")
            
        else:
            print('Progression Outcome: Do not progress - module retriever ')
            retriever = retriever + 1
            print("Do not Progress – module retriever")
            marks_dict(retriever,retriever_lst,"Module retriever")
            
    while True:
        option = input('''Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''').lower()
        if option != 'q' and option != 'y':
            print('Invalid choice please try again')
        else:
            break
    if option == 'y':
        print()
    elif option == 'q':
        print("\nPart 4 :")
        print(' '.join("{}: {}".format(k, v) for k, v in final_results.items()))##https://stackoverflow.com/questions/8519599/python-dictionary-to-string-custom-format
        break

