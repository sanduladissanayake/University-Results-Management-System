# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20221170         UoW No: w1954018
 
# Date: 5th of December 2022

#outcomes
progress = 0
trailer = 0
excluded = 0
retriever = 0


file = open("Test_Results.txt","a") #text file opening

#lists
progress_lst = []
trailer_lst = []
excluded_lst = []
retriever_lst = []

while True:
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



    pass_m = validation('pass')  #function call
    defer_m = validation('defer')
    fail_m = validation('fail')
    if pass_m + defer_m + fail_m != 120:  #conditions
        print('Total incorrect')
        continue
    else:
        if pass_m == 120 and defer_m == fail_m == 0:
            print('Progression Outcome: Progress')
            progress = progress + 1
            print("Progress")
            progress_lst.extend([pass_m,defer_m,fail_m])
           
        elif pass_m == 100 and pass_m > (defer_m + fail_m):
            print('Progression Outcome: Progress(module trailer)')
            trailer = trailer + 1
            print("Progress (module trailer)")
            trailer_lst.extend([pass_m,defer_m,fail_m])
            
        elif fail_m > (pass_m + defer_m):
            print('Progression Outcome: Exclude')
            excluded = excluded + 1
            print("Exclude")
            excluded_lst.extend([pass_m,defer_m,fail_m])
            
        else:
            print('Progression Outcome: Do not progress - module retriever ')
            retriever = retriever + 1
            print("Do not Progress – module retriever")
            retriever_lst.extend([pass_m,defer_m,fail_m])
            
    while True:
        option = input('''Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''').lower()
        if option != 'q' and option != 'y':
            print('Invalid choice please try again')
        else:
            break
    if option == 'y':
        continue
    else:
        option == 'q'
        print('--------------------------------------------------------------------------------------------------')
        print('Histogram')
        print('Progress ', progress, ' : ', + progress * '*')
        print('Trailer ', trailer, '  : ', + trailer * '*')
        print('Retriever ', retriever, ': ', + retriever * '*')
        print('Excluded ', excluded, ' : ', + excluded * '*')
        total = (progress + trailer + retriever + excluded)
        print()
        print(total, 'outcomes in total')
        print('--------------------------------------------------------------------------------------------------')


        while True:#printing lists
            if progress >= 1:
                
                print('Progress - ',end='')
                print(*progress_lst[0:3],sep = ',') ##https://flexiple.com/python/python-print-list/
                total_results = "%s - %d, %d, %d" % ('Progress' ,progress_lst[0],progress_lst[1],progress_lst[2])##https://www.udacity.com/blog/2020/11/python-string-format-whats-the-difference-between-s-and-d.html 
                file.write(f"\n{total_results}")        
                file.flush()
                del (progress_lst[0:3]) ##https://www.w3schools.com/python/ref_keyword_del.asp
                progress = progress - 1
                continue
            if trailer >= 1:
                print('Progress(module trailer) - ',end='')
                print(*trailer_lst[0:3],sep = ',')
                total_results = "%s - %d, %d, %d" % ("Progress(module trailer)" ,trailer_lst[0],trailer_lst[1],trailer_lst[2])
                file.write(f"\n{total_results}")
                del (trailer_lst[0:3])
                trailer = trailer - 1
                continue

            if retriever >= 1:
                print('Module retriever - ',end='')
                print(*retriever_lst[0:3],sep = ',')
                total_results = "%s - %d, %d, %d" % ("Module retriever" ,retriever_lst[0],retriever_lst[1],retriever_lst[2])
                file.write(f"\n{total_results}")
                
                del (retriever_lst[0:3])
                retriever = retriever - 1
                continue

            if excluded >= 1:
                print('Exclude - ',end='')
                print(*excluded_lst[0:3],sep = ',')
                total_results = "%s - %d, %d, %d" % ("Exclude" ,excluded_lst[0],excluded_lst[1],excluded_lst[2])
                file.write(f"\n{total_results}")

                del (excluded_lst[0:3])
                excluded = excluded - 1
                continue
            break
        break

file.close() #text file closing





