# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:
    
    play sound "audio/bag_sound.mp3" loop fadein 0.5
   
    # Show a background.
    scene bg
    show player happy
    
    # Introduction
    Annie "Welcome to Financia! I'm Annie, guiding you through mastering budgeting. Navigate finances, make informed decisions, manage expenses, and achieve savings goals with my insights. Let's thrive financially together!"
   
    
    # Greeting and player introduction
    $ name=renpy.input("What is your name?")
    Annie "Nice to meet you, [name]! Join Advait's journey in budgeting and financial planning. Learn key financial skills, overcome challenges, and achieve your goals together. Let's boost your financial confidence!"

    hide player happy
    menu:
        Annie "Choose Advait's role and shape his financial journey. Whether student, intern, or employee, guide him to navigate challenges and achieve financial goals. Your decisions matter!"

        "Student":
            play sound "audio/button.mp3"
            
            jump student_role
        "Employee":
            play sound "audio/button.mp3"
            
            jump employee_role

# Student Path
label student_role:
    
    # Introduction to student path
    scene village
    show boy college
    
    
    Annie "Meet Advait, a village boy embracing city college life. With enthusiasm, he aims to save $800 by semester's end. Guide his financial journey and witness his growth."

    show screen starting
    Annie "Let's take a look at Advait's current expense statistics:"

    
    
    hide screen starting
    menu:
        Annie "Choose Advait's career path: freelancing, startup intern, or educational mentor. Your choices shape his journey, balancing work-life, skill growth, and financial stability towards his goals."
        "Freelancer":
            
            play sound "audio/button.mp3"
            jump freelancer_path
        "Intern at Startup":
           
            play sound "audio/button.mp3"
            jump intern_path
        "Educational Mentor":
            
            play sound "audio/button.mp3"
            jump mentor_path
    hide boy college

# Freelancer Path
label freelancer_path:
    scene freelance
    
    Annie "Advait dives into freelancing alongside college. Balancing projects with studies, he manages expenses and seeks success. Support his juggle of commitments towards financial and academic goals."
    
    default income = 0
    default college_fees = 3000
    default groceries = 500
    default  misc_expenses = 1000
    default total_expenses = college_fees + groceries + misc_expenses
    default target_amount = 500
    default total_savings = 0
    
    # Day 1
    scene home
    Annie "On Day 1, Advait faces the daunting task of finding an affordable place to stay in the bustling city. Emotions run high as he seeks a balance between comfort, cost, and convenience."
   
    
    menu:
        Annie "Based on Advait's situation, what would you recommend as the best course of action for him to take?"
        "Rent the cheaper apartment for $1000":
            
            play sound "audio/button.mp3"
            $ rent = 1000
            $ total_expenses += rent
            
            jump apartment_fire
        "Rent a better apartment for $2000":
            
            play sound "audio/button.mp3"
            $ rent = 2000
            $ total_expenses += rent
            play sound "audio/thunder.mp3"
            scene fire
            "He took a beeter apartment and it covered fire insurance, he will not have to loose $1500"
            
       

    # Apartment Fire Event
    label apartment_fire:
        
        play sound "audio/thunder.mp3"
        scene fire
        "Disaster hits! A fire erupts in Advait's apartment. Without insurance, he faces $1500 in damages. If only he had chosen a better housing option, this could have been avoided."

        
        $ total_expenses += 1500
        $ renpy.pause()

    # Networking Event
    scene friends
    
    Annie "Arnav, Advait's supportive friend, encourages him to attend a networking event at the AMEX office. This could be a golden opportunity for Advait to expand his professional network and open doors to new opportunities."
    menu:
        "Attend friend's event at AMEX office":
            
            play sound "audio/button.mp3"
            
            jump amex_event
        "Do not attend any event":
            play sound "audio/button.mp3"
            
            Annie "Regrettably, Advait decides to skip the networking event, missing a valuable chance to connect with professionals and potentially enhance his career prospects."

    label amex_event:
        scene event
        menu:
            "Network actively":
                play sound "audio/button.mp3"
                play sound "audio/crowd.mp3" 
                
                $ networking = 4000
                $ income += networking
                "Advait leaves a lasting impression at the event, securing projects worth $4000 through his networking efforts!"
                
            "Network casually":
                play sound "audio/button.mp3"
                pause 0.3 
                play sound "audio/crowd.mp3" noloop fadein 0.3
                
                $ networking = 1000
                $ income += networking
                "Advait builds few valuable connections and secures $1000 in new project opportunities through his networking efforts."
            "Decide not to attend":
                play sound "audio/button.mp3"
             
                scene sad
                "Advait decides not to attend, missing the chance to broaden his network and potentially advance his career."
        $ renpy.pause()

    # Day 2
    scene prof
    Annie "On Day 2, Advait's professor presents him with a chance to assist on a project, offering a valuable opportunity to deepen his academic and professional skills."
    menu:
        "Help professor with extra work":
            play sound "audio/button.mp3"
            
            jump professor_help
        "Decline professor's offer":
            play sound "audio/button.mp3"
           
            "Aman declines the professor's offer."
    
    label professor_help:
        

        menu:
            "Do a poor job":
                play sound "audio/button.mp3"
                
                scene sad
                "The professor is disappointed with Advait's work, leading to missed chances for positive recognition and further opportunities."
            "Do an excellent job":
                play sound "audio/button.mp3"
               
                
                $ income += 4000
                scene prof_happy
                "Impressed by Advait's dedication and quality of work, the professor recommends him, leading to Advait earning $4000."
                
        $ renpy.pause()

    # End of Month
    label end_of_month:
        
        scene bg 
        show player happys at left
        show boy colleges at right
        $ total_savings = income - total_expenses
        show screen summ

        if total_savings >= target_amount:
            screen stara
            play sound "audio/crowd.mp3" noloop fadein 0.3
            
            "Fantastic! Advait exceeded his savings goal and achieved a 5-star rating."
        elif total_savings == target_amount:
            screen staro
            play sound "audio/crowd.mp3" noloop fadein 0.3
            pause 
            "Well done! Aman saved the target amount and earned 4 stars."
        elif total_savings > 0:
            
            "Great job! Advait reached his savings target and earned a 4-star rating."
        elif total_savings == 0:
            
            "Advait broke even with his expenses, earning 2 stars."
        else:
            
            "Advait ended up in debt this month, earning 1 star."
        hide screen summ
        menu:
            "Choose an option"
            "Replay with the same role":
                play sound "audio/button.mp3"
                
                jump start
            "Try a different role":
                play sound "audio/button.mp3"
                
                jump start

# Intern Path
label intern_path:

    # Introduction to intern path
    "As an intern at a startup, Aman receives a fixed monthly stipend."

    $ income = 300
    $ college_fees = 500
    $ public_transport = 50
    $ eating_out = 100
    $ dorm_fees = 300
    
    while True:
        menu:
            "Apply for a higher-paying job":
                $ new_income = 400
                $ income = new_income
                "Aman's new monthly stipend is $[new_income]!"
            "Check savings":
                $ savings = income - (college_fees + public_transport + eating_out + dorm_fees)
                "Aman's savings: $[savings]"
            "End Month":
                jump end_of_month

# Mentor Path
label mentor_path:

    # Introduction to mentor path
    "As an educational mentor, Aman earns a fixed monthly income."

    $ income = 250
    $ college_fees = 500
    $ public_transport = 50
    $ eating_out = 100
    $ dorm_fees = 300
    
    while True:
        menu:
            "Take on extra tutoring sessions":
                $ extra_income = 50
                $ income += extra_income
                "Aman earned an extra $50 this month!"
            "Check savings":
                $ savings = income - (college_fees + public_transport + eating_out + dorm_fees)
                "Aman's savings: $[savings]"
            "End Month":
                jump end_of_month

# Employee Path
label employee_role:

    # Introduction to employee path
    "As an employee at an MNC, Aman has a fixed monthly salary."

    $ income = 2000
    $ monthly_bills = 800
    $ kids_school_fees = 300
    $ grocery_bills = 400
    $ target_amount = renpy.input("Enter Aman's target amount to be saved.")

    while True:
        menu:
            "Ask for a raise at work":
                $ raise_amount = 200
                $ income += raise_amount
                "Aman's new monthly salary is $[income]!"
            "Check savings":
                $ savings = income - (monthly_bills + kids_school_fees + grocery_bills)
                "Aman's savings: $[savings]"
            "End Month":
                jump end_of_month

# Random Events
label random_event:

    $ event_type = randint(1, 3)

    if event_type == 1:
        "Aman faces unexpected medical bills this month, increasing expenses by $200."
        $ total_expenses += 200

    elif event_type == 2:
        "Aman's vehicle needs servicing, increasing expenses by $100."
        $ total_expenses += 100

    elif event_type == 3:
        "Aman finds a part-time job opportunity, increasing income by $100."
        $ income += 100

    "Press any key to continue."
    $ renpy.pause()
