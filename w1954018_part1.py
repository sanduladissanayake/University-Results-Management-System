# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20221170         UoW No: w1954018
 
# Date: 5th of December 2022

#outcomes
progress = 0
trailer = 0
excluded = 0
retriever = 0


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
           
        elif pass_m == 100 and pass_m > (defer_m + fail_m):
            print('Progression Outcome: Progress(module trailer)')
            trailer = trailer + 1
            
        elif fail_m > (pass_m + defer_m):
            print('Progression Outcome: Exclude')
            excluded = excluded + 1
            
        else:
            print('Progression Outcome: Do not progress - module retriever ')
            retriever = retriever + 1
            
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
        break
    break
