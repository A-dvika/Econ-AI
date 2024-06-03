screen ui:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle  "button"
        action ShowMenu("summ")

screen summ:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30    
        hbox:
            spacing 40
            
            vbox:
                spacing 10
                text "End of the month summary:" size 40
                text "Total Income: [income]" size 40
                text "Total Expenses: [total_expenses]" size 40
                text "Total Saved: [total_savings]" size 40
                text "Target Savings: [target_amount]" size 40

screen starting:
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30    
        hbox:
            spacing 40
            
            vbox:
                spacing 10
                text "Start of the month summary:" size 40
                text "Total Income: [income]" size 40
                text "Total Expenses: [total_expenses]" size 40
                text "Total Saved: [total_savings]" size 40
                text "Target Savings: [target_amount]" size 40
            
                